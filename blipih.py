#!/usr/bin/env python

import time
import unicornhat as unicorn
import re

# Setup Unicorn Hat
unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

# Readfile
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# Defining Colors
red = 255,0,0 # blocked
green = 0,255,0 # cached
blue = 0,0,255 # secure

yellow = 255,255,0 # forwarded
cyan = 0,255,255 # query
pink = 255,0,255 # insecure

orange = 255,128,0 # reply
ltgreen = 128,255,0 # dhcp
ltcyan = 0,255,128 # unused
ltblue = 0,128,255 # unused
ltpink = 128,0,255 # unused

fuchsia = 255,0,127 # unused
white = 255,255,255 # dnssec

# Delay between LED updates
delaytime = 0.05


if __name__ == '__main__':
    logfile = open("/var/log/pihole.log","r")
    loglines = follow(logfile)
    while True:
        for y in range(height):
            for x in range(width):
                for line in loglines:
                    if re.match("(.*)dnssec(.*)*", line):
                        unicorn.set_pixel(x,y,white)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)query(.*)*", line):
                        unicorn.set_pixel(x,y,cyan)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)forwarded(.*)*", line):
                        unicorn.set_pixel(x,y,yellow)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)reply(.*)*", line):
                        unicorn.set_pixel(x,y,orange)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)gravity.list(.*)*", line):
                        unicorn.set_pixel(x,y,red)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)cached(.*)*", line):
                        unicorn.set_pixel(x,y,green)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)DHCP(.*)*", line):
                        unicorn.set_pixel(x,y,ltgreen)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)validation result is SECURE(.*)*", line):
                        unicorn.set_pixel(x,y,blue)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
                    if re.match("(.*)validation result is INSECURE(.*)*", line):
                        unicorn.set_pixel(x,y,pink)
                        unicorn.show()
                        time.sleep(delaytime)
                        break
        unicorn.clear()
