import cv2
import os
from utils import draw_box, put_text

class InferenceEngine:
    """
    Class for performing object detection on an image and returning the results.
    """

    def __init__(self, model_path=None):
        """
        Initializes the InferenceEngine class and loads the model.

        Args:
            model_path (str, optional): Path to the model file.
        """
        try:
            self.model_path = model_path
            # Example: self.model = load_model(model_path)
        except (FileNotFoundError, IOError) as e:
            print(f"Error occurred while loading the model: {e}")
            self.model_path = None

    def predict(self, image, label_file):
        """
        Returns detection results from the image and label file.

        Args:
            image (numpy.ndarray): Input image.
            label_file (str): Path to the label file.

        Returns:
            list: List of detection results, each in the format {'class_id': int, 'box': (x, y, w, h)}.
        """
        results = []
        try:
            h, w, _ = image.shape
            with open(label_file, 'r') as f:
                for line in f.readlines():
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    x_center_norm = float(parts[1])
                    y_center_norm = float(parts[2])
                    width_norm = float(parts[3])
                    height_norm = float(parts[4])
                    box_w = int(width_norm * w)
                    box_h = int(height_norm * h)
                    box_x = int((x_center_norm * w) - (box_w / 2))
                    box_y = int((y_center_norm * h) - (box_h / 2))
                    results.append({'class_id': class_id, 'box': (box_x, box_y, box_w, box_h)})
        except (FileNotFoundError, IOError) as e:
            print(f"Error occurred while reading the label file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during prediction: {e}")
        return results

# --- SETTINGS ---
images_path = 'C:/Users/Acar/Desktop/shipdataset/test/images'
labels_path = 'C:/Users/Acar/Desktop/shipdataset/test/labels'
file_name = '0__20161102_180658_0e26__-122-32843644745485_37-73923054907409_png_jpg.rf.2e9e6b63dbb70338c8ff3b2e6f2a84c7'

image_file = os.path.join(images_path, file_name + '.jpg')
label_file = os.path.join(labels_path, file_name + '.txt')

try:
    image = cv2.imread(image_file)
    if image is None:
        print(f"Error: Image could not be loaded! Is the file path correct? -> {image_file}")
    else:
        engine = InferenceEngine()
        results = engine.predict(image, label_file)
        for res in results:
            draw_box(image, res['box'])
            put_text(image, str(res['class_id']), (res['box'][0], res['box'][1] - 10))
        cv2.imshow('Labeled Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
except (cv2.error, AttributeError) as e:
    print("An error occurred in camera or image processing. Camera connection could not be verified.")
    print(f"Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")