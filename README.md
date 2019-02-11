
# Blinken Pi-hole
The Blinken [Pi-hole](https://pi-hole.net) service shows visually various information of individual DNS requests on a [Unicorn HAT](https://github.com/pimoroni/unicorn-hat).

[Pi-hole](https://pi-hole.net) is a DNS sinkhole aka *A BLACK HOLE FOR INTERNET ADVERTISEMENTS*.

The [Unicorn HAT](https://github.com/pimoroni/unicorn-hat) is a LED matrix of 64 (8 x 8) RGB LEDs.

![GitHub Logo](images/blinkenpihole.gif)

## Colors

The display will show the following colors

* red - blocked
* green - cached
* blue - secure
* yellow - forwarded
* cyan - query
* pink - insecure
* orange - reply
* ltgreen - dhcp
* white - dnssec-query

## Requirements

* Raspberry Pi (tested with a Raspberry Pi 3B)
* Python 2.7 (tested with 2.7.13)
* Pi-hole installed
* unicornhat

## Install unicorn hat

```sh
$ sudo apt-get install python-pip python-dev
$ sudo pip install unicornhat
```

## Attention!
`unicornhat` needs root access to function. Therefore this service runs as root user.

## Installation

```sh
$ sudo cp blipih.py /usr/local/sbin
$ sudo chmod 744 /usr/local/sbin/blipih.py
$ sudo cp blipih.service /lib/systemd/system/blipih.service
$ sudo chmod 644 /lib/systemd/system/blipih.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable blipih.service
```

## Change Crontab to restart the Blinken Pi-hole service after the daily logrotate

Open crontab file `/etc/cron.d/pihole` look for `pihole flush once quiet`

```sh
# Pi-hole: Flush the log daily at 00:00
#          The flush script will use logrotate if available
#          parameter "once": logrotate only once (default is twice)
#          parameter "quiet": don't print messages
00 00   * * *   root    PATH="$PATH:/usr/local/bin/" pihole flush once quiet
```

and add the following to `/etc/cron.d/pihole`. The job should start one minute after the `pihole flush once quiet`

```sh
#
# Restart the Blinken Pi-hole service after the logrotate
00 01	* * *	root /bin/systemctl restart blipih.service
```

**Check after each `pihole -up` that this entry still exists**
