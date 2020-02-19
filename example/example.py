import sys
import os
import logging
import wakeonlan

sys.path.append('../')

from samsungtvws import SamsungTVWS

# Increase debug level
logging.basicConfig(level=logging.INFO)

# Normal constructor
tv = SamsungTVWS('192.168.xxx.xxx')

# Autosave token to file 
token_file = os.path.dirname(os.path.realpath(__file__)) + '/tv-token.txt'
tv = SamsungTVWS(host='192.168.xxx.xxx', port=8002, token_file=token_file)

# Toggle power
tv.shortcuts().power()

# Power On
wakeonlan.send_magic_packet('CC:6E:A4:xx:xx:xx')

# Open web in browser
tv.open_browser('https://duckduckgo.com/')

# View installed apps (Spotify)
apps = tv.app_list()
logging.info(apps)

# Open apps (Spotify)
tv.run_app('3201606009684')

# Get device info (device name, model, supported features..)
info = tv.rest_device_info()
logging.info(info)
