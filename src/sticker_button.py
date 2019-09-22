from functools import partial
from gi.repository import Gtk, GdkPixbuf, Gdk
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

def sticker_button(preview_file, sticker_file):
    preview_img = Gtk.Image.new_from_file(preview_file)
    button = Gtk.Button()
    button.set_image(preview_img)
    button.connect('clicked', partial(copy_sticker_to_clipboard, sticker_file))
    button.sticker_file = sticker_file
    return button

def copy_sticker_to_clipboard(sticker_file, widget):
    s_img = GdkPixbuf.Pixbuf.new_from_file(sticker_file)
    clipboard.set_image(s_img)
    print('setting image to clipboard', sticker_file)
