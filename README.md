# The Literary Bot
A simple Raspberry Pi twitter bot that posts self-generated haikus.

## Table of Contents
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)

## Technologies Used
- raspberry pi 3
- python - version 3.8.10
- twython - version 3.7.0

## Features
Posts a self generated hiaku daily

## Setup
#### Register to use the Twitter API
- Sign up for a developer account [here](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

#### Keys
Your secrets exist in a config.py file or directly inside main.py
```
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'
```

#### Setting up Raspberry Pi
- Make sure your Raspberry Pi is up to date by running the following commands \
`sudo apt-get update` \
`sudo apt-get upgrade` 

- Install the tools needed. Run the following commands in the terminal \
`sudo apt-get install python-setuptools` \
`sudo easy_install pip` \
`sudo pip install twython`


- The folder exists on your Raspberry Pi. Make the script executable by running in the terminal \
`sudo chmod -x /your/file/path/main.py`

- Automate the Twitter Bot. Edit the crontab by running \
`sudo crontab -e`

- At the bottom of the file include
`0 17 * * * python /your/file/path/main.py`

To save, **Ctrl** + **X** + **Y** and hit **Enter**

A useful tool for Cron format can be found [here](http://www.nncron.ru/help/EN/working/cron-format.htm)
