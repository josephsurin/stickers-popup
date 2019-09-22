from gi.repository import Gtk, GdkPixbuf, Gdk

from stickers_grid import stickers_grid
from util import PREVIEW_WIDTH, KEYCODES

def stickers_notebook(stickers_data):
    notebook = Gtk.Notebook()
    notebook.set_scrollable(True)
    notebook.set_tab_pos(Gtk.PositionType.RIGHT)
    for sd in stickers_data:
        title_img_pb = GdkPixbuf.Pixbuf.new_from_file_at_scale(sd['stickers_data'][0]['preview_file'], PREVIEW_WIDTH//2, -1, True)
        title_img = Gtk.Image.new_from_pixbuf(title_img_pb)
        notebook.append_page(stickers_grid(sd['stickers_data']), title_img)

    notebook.connect('key_press_event', handle_keypress)

    return notebook

def handle_keypress(notebook, e):
    if e.state == Gdk.ModifierType.SHIFT_MASK:
        keycode = e.hardware_keycode
        if keycode == KEYCODES['k']:
            notebook.prev_page()
        elif keycode == KEYCODES['j']:
            notebook.next_page()
