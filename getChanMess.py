#!/usr/bin/python36

import requests, json, xlwt, os, datetime
from dateutil import parser
import variables

def checkIdChata(rid):
     listsId = []
     return rid in listsId

headers = {
    'X-Auth-Token':variables.token,
    'X-User-Id': variables.userid,
    'Content-type': 'application/json',
}
delta = datetime.timedelta(hours=variables.deltahour)
now = datetime.date.today()
newpath = "/mnt/messages/channels"
if not os.path.exists(newpath):
    os.makedirs(newpath)

resp =  requests.get(variables.adress+'/channels.list', headers=headers,)
if resp.status_code == requests.codes.ok:
    r_all = resp.json()
    for obj in r_all['channels']:
            data = '{ "roomId": "%s", "joinCode": "1234" }'%(obj['_id'])
            data1 = '{ "roomId": "%s" }'%(obj['_id'])

            resp1 = requests.post(variables.address+'/channels.join', headers=headers, data=data)
            if not resp1.status_code == requests.codes.ok:
                print(resp1.raise_for_status())
            params = (
                ('roomId', obj['_id']),
            )
            response = requests.get(variables.address+'/channels.messages', headers=headers, params=params)
            if response.status_code == requests.codes.ok:
                 r = response.json()
                 i=1
                 wb = xlwt.Workbook()
                 ws = wb.add_sheet('Лист1')
                 ws.write(0,0,'Дата')
                 ws.write(0,1,'Время')
                 ws.write(0,2,'ФИО')
                 ws.write(0,3,'Сообщение')
                 for obj_mes in r['messages']:
                    # get time from json
                    times = datetime.datetime.strptime(obj_mes['ts'][obj_mes['ts'].find('T')+1:obj_mes['ts'].find('Z')-4],"%H:%M:%S")
                    ws.write(i,0,obj_mes['ts'][0:obj_mes['ts'].find('T')])
                    ws.write(i,1,str(datetime.datetime.time(times+delta)))
                    ws.write(i,2,obj_mes['u']['name'])
                    if ('file' in obj_mes):
                        ws.write(i,3,obj_mes['file']['name'])
                    else:
                        ws.write(i,3,obj_mes['msg'])
                    i = i + 1
                 wb.save(newpath+"/"+obj['name']+".xls")
            resp2 = requests.post(variables.address+'/channels.leave', headers=headers, data=data1)
            if resp2.status_code == requests.codes.ok:
                print(resp2.raise_for_status())
