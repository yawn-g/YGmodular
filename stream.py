from twython import TwythonStreamer
from twython import Twython
from gpiozero import LED
from time import sleep

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

pin0 = LED(17)
pin1 = LED(4)
pin2 = LED(27)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            print("@%s: %s" % (username, tweet))
            if '0H' in data['text']:
                print('Pin 0 set HIGH by @'+username)
                pin0.on()
            if '0L' in data['text']:
                pin0.off()
                print('Pin 0 set LOW by @'+username)
            if '1H' in data['text']:
                pin1.on()
                print('Pin 1 set HIGH by @'+username)
            if '1L' in data['text']:
                pin1.off()
                print('Pin 1 set LOW by @'+username)
            if '2H' in data['text']:
                pin2.on()
                print('Pin 2 set HIGH by @'+username)
            if '2L' in data['text']:
                pin2.off()
                print('Pin 2 set LOW by @'+username)

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#twitter.update_status(status='I am listening. Tweet me \"nH\" or \"nL\" to set pin n (0, 1 or 2) High or Low.')

stream.statuses.filter(track="yglisten")

