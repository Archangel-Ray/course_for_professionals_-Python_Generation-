'''
This module provides function to load, save and display images. It also provides the function char_to_array(), which converts a character into an image (in 3d np.ndarray) and is_emoji() to check if the given character is a supported emoji

The data EMO and EMO_UNICODE stores sets of all supported emojis
'''

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
import pickle

with open('data/emoji.pickle', 'rb') as f:
    EMO, EMO_UNICODE = pickle.load(f)

def load(path):
    '''
    Get an image in the form of 3d numpy array from the given path

    Parameters
    ----------
    path : string
        file directory location of the image

    Returns
    -------
    img : 3d numpy array with dtype np.uint8
        image

    '''
    img = Image.open(path, 'r')
    img = np.asarray(img, dtype = np.uint8)
    return img.copy()

def show(img):
    '''
    Show the image

    Parameters
    ----------
    img : 3d numpy array with dtype np.uint8
        image to show

    Returns
    -------
    None.

    '''
    plt.axis('off')
    plt.imshow(img)
    plt.show()
   # ?????


def save(img, path):
    '''
    Save the image to the given path

    Parameters
    ----------
    img : 3d numpy array with dtype np.uint8
        image to save
    path : string
        path for which the image to save
    Returns
    -------
    None.
    '''

    img = Image.fromarray(np.uint8(img.copy())).convert('RGB')
    img.save(path)

def _denoise(img, text_colour, bg_colour):
    '''
    ** internal use, please do not use it **
    make the image to have only two colours
    '''
    is_text = np.abs(img - text_colour).sum(axis = 2) < np.abs(img - bg_colour).sum(axis = 2)
    img_copy = img.copy()
    img_copy[is_text] = text_colour
    img_copy[~is_text] = bg_colour
    return img_copy

def is_emoji(ch):
    '''
    Check if the given character is a supported emoji

    Parameters
    ----------
    ch : character with length 1

    Returns
    -------
    bool. True if it is a supported emoji

    '''
    return (ch in EMO) or (ch in EMO_UNICODE)

def _strip_space(img, text_colour, ch, space = 5):
    '''
    ** internal use, please do not use it **
    remove unnecessary space for characters
    '''
    if ch == ' ':
        return img[:,:img.shape[1]//2]
    not_bg = (img == text_colour).all(axis = 2)
    col = not_bg.any(axis = 0)
    start_idx =  (col).argmax(axis=0) - space
    end_idx = col[::-1].argmax(axis=0) - space
    return img[:,start_idx:-end_idx]

def char_to_array(ch, text_colour = (255, 255, 255), bg_colour = (0, 0, 0)):
    '''
    Get an image for the given character in the form of 3d numpy array

    Parameters
    ----------
    ch : string with len 1
        It represent a character to be represented as an image (in 3d np.ndarray). To be shown properly, the character must either represent an emoji or some simple characters with 32 <= ord(ch) <= 126
    text_colour : tuple with 3 integers in the range [0, 255]
        It represents the colour of the character (if it is not an emoji)
    bg_colour : tuple with 3 integers in the range [0, 255]
        It represents the background colour of the image. Background colour and text colour cannot be the same
    raise : TypeError if ch is not string with len 1
    raise : ValueError if the background and the text have the same colour
    raise : Exception for other errors

    Returns
    -------
    3d np.ndarray with dtype np.uint8 for the image representation of the given character
    '''
    if text_colour == bg_colour:
        raise ValueError('text colour and background colour cannot be the same')
    if not (is_emoji(ch) or 32 <= ord(ch) <= 126):
        raise ValueError('the character must be a supported emoji or symbol')
    try:
        font_file = "data/NotoColorEmoji.ttf" if is_emoji(ch) else "data/InputSans-Regular.ttf"
        fnt = ImageFont.truetype(font_file, size = 109, layout_engine = ImageFont.LAYOUT_RAQM)
        im = Image.new("RGB", (130, 130), color = bg_colour)
        draw = ImageDraw.Draw(im)
        w, h = draw.textsize(ch, font = fnt)
        draw.text(((130-w)//2, (130-h)//2), ch, fill = text_colour, embedded_color=True, font=fnt)
        img = np.asarray(im)
        if not is_emoji(ch):
            img = _denoise(img, text_colour, bg_colour)
            return _strip_space(img, text_colour, ch)
        return img.copy()
    except TypeError:
        raise TypeError('only work for string with length 1')
    except:
        raise Exception('the function does not work on your computer, please contact the lecturer')

def text_to_array(text, text_colour, bg_colour):   
    res = []
    for i in text:
        res.append(char_to_array(i, text_colour, bg_colour))
    return np.hstack(res)




