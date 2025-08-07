# Satellite Ship Detection using YOLOv8

![Project Banner]()

A robust deep learning model for the real-time detection of ships in satellite imagery. This project demonstrates an end-to-end computer vision pipeline, from data preparation and model training to final evaluation on a held-out test set. The model is built using the YOLOv8 architecture and is trained on a custom dataset.

## Key Features

- **Custom-Trained Model:** Utilizes a YOLOv8s model fine-tuned on a specific satellite imagery dataset for high-accuracy ship detection.
- **End-to-End Pipeline:** Covers the complete machine learning lifecycle: data analysis, training, validation, and unbiased testing.
- **Performance Analysis:** Employs standard object detection metrics, including Precision, Recall, and mean Average Precision (mAP), to rigorously evaluate model performance.
- **Data-Centric Approach:** Showcases an iterative development process, where training was extended from 50 to 150 epochs to significantly improve model accuracy and generalization.

## Demo

Here is a sample prediction from the final model on a test image it has never seen before.

![Prediction Example]()
*The model successfully identifies a ship with high confidence.*

## Model Performance

The model was trained for 150 epochs, and the weights from the epoch with the best validation performance were selected for final testing. The results below show the final, unbiased performance on the **Test Set** compared to the performance on the **Validation Set**.

| Metric        | Validation Set Score | **Final Test Set Score** |
|---------------|:--------------------:|:------------------------:|
| **Precision** | 0.586                | **0.698** |
| **Recall** | 0.489                | **0.550** |
| **mAP50** | 0.501                | **0.577** |
| **mAP50-95** | 0.287                | **0.330** |

The significantly higher performance on the test set indicates strong generalization capabilities.

## Technology Stack

- **Python 3.13**
- **PyTorch 2.7**
- **Ultralytics YOLOv8**
- **OpenCV** for image processing
- **NumPy** for numerical operations

## Setup and Installation

To get this project up and running on your local machine, follow these steps.

**1. Clone the repository:**
```bash
git clone [https://github.com/](https://github.com/)<SENIN-KULLANICI-ADIN>/<PROJE-ADIN>.git
cd <PROJE-ADIN>

**2. Create and activate a virtual environment:**
```bash
# For Windows
python -m venv .venv
.\.venv\Scripts\activate

# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

**3. Install dependencies:**
```bash
pip install -r requirements.txt

**4. Download the Dataset:**
The custom ship dataset used for this project is not included in the repository due to its size. 
You can download it from the link below.
Dataset: [https://universe.roboflow.com/stillwater81/ship-image-detection]

**5. Download Pre-trained Weights:**
The final trained model weights (best.pt) can be downloaded from:

Model Weights: [https://drive.google.com/file/d/1DT1JwAZLYx4NenlKfl3X-9k558HjHuMw/view?usp=sharing]

Usage
You can use the provided scripts and YOLO's CLI to train, validate, or make predictions with the model.

Training:
To train the model from scratch, use the following command:

```bash

yolo detect train data=data.yaml model=yolov8s.pt epochs=150 imgsz=640
Validation / Testing:
To evaluate the final model on the test set, run:

```bash

yolo detect val model=weights/best.pt data=data.yaml split=test
Inference:
To make a prediction on a new image:

```bash

yolo detect predict model=weights/best.pt source='path/to/your/image.jpg'

