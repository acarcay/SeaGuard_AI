import os
from ultralytics import YOLO

def evaluate_model(model_path, data_yaml, split='test'):
    """
    Loads a trained YOLO model and evaluates it on the specified dataset split.

    Args:
        model_path (str): Path to the trained model (e.g., 'runs/detect/train/weights/best.pt').
        data_yaml (str): Path to the data.yaml file.
        split (str, optional): Dataset split to evaluate on ('test' or 'val').

    Returns:
        dict: Dictionary containing precision, recall, and mAP metrics.
    """
    try:
        model = YOLO(model_path)
    except (FileNotFoundError, IOError) as e:
        print(f"Model file not found or could not be loaded: {e}")
        return None

    try:
        # Run validation
        results = model.val(data=data_yaml, split=split)
        
        # Get the metrics dictionary using the correct method
        metrics_dict = results.results_dict

        # Create the report using the correct keys from the new dictionary
        report = {
            "precision": metrics_dict['metrics/precision(B)'],
            "recall": metrics_dict['metrics/recall(B)'],
            "mAP50": metrics_dict['metrics/mAP50(B)'],
            "mAP50-95": metrics_dict['metrics/mAP50-95(B)']
        }
        
        print("\nValidation Results:")
        for k, v in report.items():
            print(f"    {k.upper()}: {v:.4f}")
        return report
        
    except Exception as e:
        print(f"An error occurred during validation: {e}")
        return None

if __name__ == "__main__":
    MODEL_PATH = "C:/Users/Acar/Desktop/opencv/runs/detect/train12/weights/best.pt"
    DATA_YAML = "C:/Users/Acar/Desktop/opencv/data.yaml"
    
    evaluate_model(MODEL_PATH, DATA_YAML, split='test')