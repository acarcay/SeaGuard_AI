import cv2
import os

# --- AYARLAR ---
# Görüntülerin ve etiketlerin bulunduğu klasörler
images_path = 'C:/Users/Acar/Desktop/shipdataset/test/images'
labels_path = 'C:/Users/Acar/Desktop/shipdataset/test/labels'

# Kontrol etmek istediğin dosyanın adı (uzantısız)
# Buraya kendi dosya adlarından birini yaz
file_name = '0__20161102_180658_0e26__-122-32843644745485_37-73923054907409_png_jpg.rf.2e9e6b63dbb70338c8ff3b2e6f2a84c7'

# --- KOD ---
# Dosya yollarını oluştur
image_file = os.path.join(images_path, file_name + '.jpg')
label_file = os.path.join(labels_path, file_name + '.txt')

# Görüntüyü yükle
image = cv2.imread(image_file)
if image is None:
    print(f"Hata: Görüntü yüklenemedi! Dosya yolu doğru mu? -> {image_file}")
else:
    # Görüntünün boyutlarını al
    h, w, _ = image.shape

    # Etiket dosyasını oku
    with open(label_file, 'r') as f:
        for line in f.readlines():
            # Satırdaki verileri ayır (class_id, x_center, y_center, width, height)
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center_norm = float(parts[1])
            y_center_norm = float(parts[2])
            width_norm = float(parts[3])
            height_norm = float(parts[4])

            # Normalize edilmiş koordinatları piksel koordinatlarına çevir
            box_w = int(width_norm * w)
            box_h = int(height_norm * h)
            box_x = int((x_center_norm * w) - (box_w / 2))
            box_y = int((y_center_norm * h) - (box_h / 2))

            # Kutuyu çiz
            cv2.rectangle(image, (box_x, box_y), (box_x + box_w, box_y + box_h), (0, 255, 0), 2)
            
            # Sınıf ID'sini yaz
            cv2.putText(image, str(class_id), (box_x, box_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Sonucu göster
    cv2.imshow('Etiketli Goruntu', image)
    cv2.waitKey(0) # Bir tuşa basana kadar bekle
    cv2.destroyAllWindows()