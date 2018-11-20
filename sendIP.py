#!/usr/bin/env python3

import time
import requests
import json
import os
from subprocess import check_output

# Giving the device time to boot and connect to network (10 seconds)
time.sleep(10)

# Define access token to send to desired device
ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

# Function which uses pushbullet api to send notification
def pushMessage(title, body):
        data = {"type": "note", "title": title, "body": body}

        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN,
                         'Content-Type': 'application/json'})
        if resp.status_code != 200:
                raise Exception('Something wrong')
        else:
                print('complete sending')

# Function will retrieve the time as well as IP address. Will send notification if IP address is found.
def sendMessage():
        now = time.strftime("%A, %X")
        wifi_ip = check_output(['hostname', '-I'])
        # Python3 returns the data as bytes, must convert the ip address to string
        # python2 works fine just using the wifi_ip variable
        add = wifi_ip.decode('UTF-8', 'ignore')
        if wifi_ip is not None:
                pushMessage("Hello Adrian ", "Ip address is: " + add + "At the time of: " + now)

sendMessage()
