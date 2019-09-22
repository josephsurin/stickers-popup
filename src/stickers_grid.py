from functools import partial
from enum import Enum

from gi.repository import Gtk

from sticker_button import sticker_button
from util import CHILDREN_PER_LINE, KEYCODES

def stickers_grid(stickers_data):
    state = {
        'idx': 0
    }

    scrolled = Gtk.ScrolledWindow()
    scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    grid = Gtk.FlowBox()
    grid.set_row_spacing(0)
    grid.set_column_spacing(0)
    grid.set_homogeneous(True)
    grid.set_max_children_per_line(CHILDREN_PER_LINE)
    grid.set_min_children_per_line(CHILDREN_PER_LINE)
    grid.set_selection_mode(Gtk.SelectionMode.SINGLE)
    for s in stickers_data:
        preview = s['preview_file']
        sticker = s['sticker_file']
        grid.add(sticker_button(preview, sticker))

    grid.set_activate_on_single_click(True)
    grid.connect('key_press_event', partial(handle_keypress, state))
    grid.connect('selected_children_changed', partial(handle_change, state))
    scrolled.add(grid)

    return scrolled

def handle_keypress(state, grid, e):
    keycode = e.hardware_keycode
    if keycode == KEYCODES['h']:
        try_idx = state['idx'] - 1
    elif keycode == KEYCODES['j']:
        try_idx = state['idx'] + CHILDREN_PER_LINE 
    elif keycode == KEYCODES['k']:
        try_idx = state['idx'] - CHILDREN_PER_LINE 
    elif keycode == KEYCODES['l']:
        try_idx = state['idx'] + 1
    elif keycode == KEYCODES['space']:
        return grid.get_selected_children()[0].get_child().activate()
    else:
        return None

    try_child = grid.get_child_at_index(try_idx)
    if try_child is not None:
        grid.select_child(try_child) 
        try_child.grab_focus()
        state['idx'] = try_idx

def handle_change(state, grid):
    state['idx'] = grid.get_selected_children()[0].get_index()
