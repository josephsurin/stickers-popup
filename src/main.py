#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from os import path

from util import get_stickers_data, DEF_WIDTH, DEF_HEIGHT
# from stickers_grid import stickers_grid
from stickers_notebook import stickers_notebook

class StickersWindow(Gtk.Window):

    def __init__(self, stickers_data):
        Gtk.Window.__init__(self, title='stickers')
        self.set_role('stickers')

        self.set_default_size(DEF_WIDTH, DEF_HEIGHT)
        self.set_size_request(DEF_WIDTH, DEF_HEIGHT)

        # position at bottom right of screen
        wa = self.get_display().get_primary_monitor().get_workarea()
        sw, sh = wa.width, wa.height
        ww, wh = self.get_size()
        self.move(sw - ww, sh - wh)

        self.add(stickers_notebook(stickers_data))

        # self.add(stickers_grid(stickers_data[0]['stickers_data']))

stickers_data = get_stickers_data(path.abspath(path.join(path.dirname(path.realpath(__file__)), '../stickers')))
win = StickersWindow(stickers_data)
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
