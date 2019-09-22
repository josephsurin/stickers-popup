from gi.repository import Gtk

from stickers_grid import stickers_grid

def stickers_notebook(stickers_data):
    notebook = Gtk.Notebook()
    for sd in stickers_data:
        title_img = Gtk.Image.new_from_file(sd['stickers_data'][0]['preview_file'])
        notebook.append_page(stickers_grid(sd['stickers_data']), title_img)
    return notebook
