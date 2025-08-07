import numpy as np
import cv2
import pytest
from utils import draw_box

def test_draw_box_creates_rectangle():
    """
    Unit test for draw_box function in utils.py.
    Checks if a rectangle is drawn on the image.
    """
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    box = (10, 10, 20, 20)
    draw_box(img, box, color=(255, 0, 0), thickness=2)
    # Check if at least one pixel in the rectangle area is colored (not black)
    assert np.any(img[10:30, 10:30] != 0)