from ultralytics import YOLO

def main():
    # 1. Önceden eğitilmiş bir YOLOv8 modelini yükle.
    model = YOLO('yolov8n.pt')

    # 2. Modeli kendi veri setinle eğit.
    results = model.train(data=r'C:/Users/Acar/Desktop/opencv/shipdataset/data.yaml', epochs=150, imgsz=640)

    # Eğitim bittikten sonra sonuçları ekrana yazdırabiliriz.
    print("Eğitim tamamlandı!")
    print(results)

if __name__ == '__main__':
    main()