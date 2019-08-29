# Rocket.Chat History

It takes messages from direct message, groups and channels of Rocket.chat and saves them to excel files

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python >= 3.6
Python module:
1) requests
2) xlwt
```
pip3 install requests xlwt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Cloning repo

```sh
$ git clone https://github.com/beremtl/rchistory
```

Change file name `variables.py.EXAMPLE` to `variables.py`

```sh
$ mv variables.py.EXAMPLE variables.py
```
Change variables in file `variables.py`

Also you can change folder for savings files

## Deployment

You can put this scripts in your `crontab`.
```
*/30 * * * * root /etc/scripts/messagesOfTheDay.py
```
It meens that script will be started every 30 minutes

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Alex Sapon** - *GPP* - [PurpleBooth](https://github.com/beremtl)

See also the list of [contributors](https://github.com/beremtl/rchistory/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* **"He who is not courageous enough to take risks will accomplish nothing in life."** (*Muhammad Ali*)
* **"Genius is one percent inspiration and ninety-nine percent perspiration"** (*Thomas A. Edison*)

Thank you for reading this!You are the best!
