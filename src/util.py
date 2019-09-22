# CONSTANTS DEFINITIONS

KEYCODES = {
    'h': 43, 'j': 44, 'k': 45, 'l': 46, 'space': 65
}
CHILDREN_PER_LINE = 6
PREVIEW_WIDTH = 64
PREVIEW_HEIGHT = 64
DEF_WIDTH = 560
DEF_HEIGHT = 350

from os import path, listdir

def is_img(f):
    _, e = path.splitext(f)
    return e[1:].lower() in ['png', 'jpg', 'jpeg', 'gif']

def get_stickers_data(stickers_dir):
    '''
    stickers_dir should only contain directories.
    each directory should contain the preview images and a folder named f
    which contains the full images whose names are the same as its preview
    image's name except the string _f is appended to the basename of the full
    image filename.
    returns a list in the form:
    [
        {
            "folder",
            "stickers_data": [
                {
                    "preview_file",
                    "sticker_file"
                }
            ]
        }
    ]
    '''
    o = []
    sticker_dirs = listdir(stickers_dir)
    for sticker_dir in sticker_dirs:
        sobj = { 'folder': sticker_dir, 'stickers_data': [] }
        for f in (a for a in listdir(path.join(stickers_dir, sticker_dir)) if is_img(a)):
            fname, fext = path.splitext(f)
            sdata = {
                'preview_file': path.abspath(path.join(stickers_dir, sticker_dir, f)),
                'sticker_file': path.abspath(path.join(stickers_dir, sticker_dir, 'f', fname + '_f' + fext))
            }
            sobj['stickers_data'].append(sdata)
        o.append(sobj)
    return o
