import cv2

def draw_box(image, box, color=(0, 255, 0), thickness=2):
    """
    Draws a bounding box on the image.

    Args:
        image (numpy.ndarray): The image.
        box (tuple): Bounding box coordinates in (x, y, w, h) format.
        color (tuple, optional): Box color (B, G, R).
        thickness (int, optional): Line thickness.

    Returns:
        None
    """
    try:
        x, y, w, h = box
        cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)
    except Exception as e:
        print(f"Error occurred while drawing box: {e}")

def put_text(image, text, org, color=(0, 255, 0), font_scale=0.9, thickness=2):
    """
    Puts text on the image.

    Args:
        image (numpy.ndarray): The image.
        text (str): Text to be written.
        org (tuple): Starting point of the text (x, y).
        color (tuple, optional): Text color (B, G, R).
        font_scale (float, optional): Font scale.
        thickness (int, optional): Text thickness.

    Returns:
        None
    """
    try:
        cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
    except Exception as e:
        print(f"Error occurred while putting text: {e}")