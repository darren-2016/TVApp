############################################################
# AppleTV Controller Application
# 

import asyncio
from pyatv import helpers

@asyncio.coroutine
def print_what_is_playing(atv):
    playing = yield from atv.metadata.playing()
    print('Currently playing:')
    print(playing)

@asyncio.coroutine
def pause(atv):
    pause = yield from atv.remote_control.pause()
    print ('Currently paused')

@asyncio.coroutine
def play(atv):
    play = yield from atv.remote_control.play()
    print ('Currently paused')
  

helpers.auto_connect(print_what_is_playing)

#helpers.auto_connect(pause)

helpers.auto_connect(play)

