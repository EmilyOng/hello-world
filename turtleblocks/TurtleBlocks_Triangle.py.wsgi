#!/usr/bin/env python
# -*- coding: utf-8 -*-

_INSTALL_PATH = '/usr/share/sugar/activities/TurtleArt.activity'
_ALTERNATIVE_INSTALL_PATH = \
    '/usr/local/share/sugar/activities/TurtleArt.activity'

import os, sys, dbus
paths = []
paths.append('../%s.activity')
paths.append(os.path.expanduser('~') + '/Activities/%s.activity')
paths.append('/usr/share/sugar/activities/%s.activity')
paths.append('/usr/local/share/sugar/activities/%s.activity')
paths.append(
    '/home/broot/sugar-build/build/install/share/sugar/activities/%s.activity')

flag = False
for path in paths:
    for activity in ['TurtleBots', 'TurtleBlocks']:
        p = path % activity
        if os.path.exists(p):
            flag = True
            sys.path.insert(0, p)

if not flag:
    print 'This code require the Turtle Blocks/Bots activity to be installed.'
    exit(1)

from time import *
from random import uniform
from math import *

from pyexported.window_setup import *


tw = get_tw()

BOX = {}
ACTION = {}


def start():
    tw.start_plugins()
    global_objects = tw.get_global_objects()
    turtles = tw.turtles
    turtle = turtles.get_active_turtle()
    canvas = tw.canvas
    logo = tw.lc

    turtle.arc(45.0, 0.0)
    turtle.forward(100.0)
    turtle.arc(90.0, 0.0)
    turtle.forward(100.0)
    turtle.arc(135.0, 0.0)
    turtle.forward(130.0)
    yield True
ACTION["start"] = start


if __name__ == '__main__':
    tw.lc.start_time = time()
    tw.lc.icall(start)
    gobject.idle_add(tw.lc.doevalstep)
    gtk.main()
