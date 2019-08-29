#!/usr/bin/python36
import requests
import json
from sys import argv
import xlwt, os
import datetime
from dateutil import parser
import variables

# Check id chata, and if find in the list nothing to do
def checkIdChata(rid):
     listsId = variables.listId
     return rid in listsId

# Added user token and id
headers = {
    'X-Auth-Token': variables.token,
    'X-User-Id': variables.userid,
    'Content-type': 'application/json',
}
# change to localzone
delta = datetime.timedelta(hours=5)
# todays date
now = datetime.date.today()
# path where to save
newpath = "/mnt/messages/"+str(datetime.date.today().year)+"/"+str(datetime.date.today().month)+"/"+str(datetime.date.today().day)#+datetime.datetime.strftime(now,"%Y-%m-%d")
# if path is not exist then create
if not os.path.exists(newpath):
    os.makedirs(newpath)

# took every direct messages in server
# request to rocket.chat server
resp =  requests.get(variables.address+'/im.list.everyone', headers=headers,)
# if responce is ok
if resp.status_code == requests.codes.ok:
    # responce to json
    r_all = resp.json()
    # take every direct chat which updated today, convert it to json from string
    out = json.loads(json.dumps([x for x in r_all['ims'] if datetime.datetime.date(parser.parse(x['_updatedAt'])) == now]))
    for obj in out:
        if not checkIdChata(obj['_id']):
                # take id param from json
                params = (
                    ('roomId', obj['_id']),
                )
                # took every message from chat id
                response = requests.get(variables.address+'/im.messages.others', headers=headers, params=params)
                if response.status_code == requests.codes.ok:
                    r = response.json()
                    # took only todays messages from chat
                    out_m = json.loads(json.dumps([x_m for x_m in r['messages'] if datetime.datetime.date(parser.parse(x_m['ts'])) == now]))
                    i=1
                    # create excel book
                    wb = xlwt.Workbook()
                    ws = wb.add_sheet('List1')
                    ws.write(0,0,'Date')
                    ws.write(0,1,'Time')
                    ws.write(0,2,'FIO')
                    ws.write(0,3,'Message')
                    for obj_mes in out_m:
                       # get time from json
                       times = datetime.datetime.strptime(obj_mes['ts'][obj_mes['ts'].find('T')+1:obj_mes['ts'].find('Z')-4],"%H:%M:%S")
                       ws.write(i,0,obj_mes['ts'][0:obj_mes['ts'].find('T')])
                       ws.write(i,1,str(datetime.datetime.time(times+delta)))
                       ws.write(i,2,obj_mes['u']['name'])
                       ws.write(i,3,obj_mes['msg'])
                       i = i + 1
                    # save file if today was some messages
                    if out_m:
                        wb.save(newpath+"/"+obj['usernames'][0]+"-"+obj['usernames'][1]+".xls")
