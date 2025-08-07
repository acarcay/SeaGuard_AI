import os

# --- BURAYI KENDİNE GÖRE DÜZENLE ---
# Etiketlerinin bulunduğu klasörün yolunu buraya yaz.
# Hem train hem de test klasörlerini kontrol etmen gerekebilir.
# Önce biriyle başla, sonra diğerini kontrol et.
# LABELS_DIR = "C:/Users/Acar/Desktop/opencv/shipdataset/train/labels"
LABELS_DIR = "C:/Users/Acar/Desktop/opencv/shipdataset/test/labels"
# ------------------------------------

def find_malformed_labels(labels_directory):
    """
    Verilen klasördeki etiket dosyalarını kontrol eder ve 5'ten farklı sayıda
    değer içeren satırları bulup raporlar.
    """
    problem_files = 0
    problem_lines = 0
    print(f"'{labels_directory}' klasörü taranıyor...")

    if not os.path.isdir(labels_directory):
        print(f"HATA: Belirtilen klasör bulunamadı: {labels_directory}")
        return

    for filename in os.listdir(labels_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(labels_directory, filename)
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                
                is_problem_file = False
                for i, line in enumerate(lines):
                    # Satırı boşluklara göre ayır ve eleman sayısını kontrol et
                    parts = line.strip().split()
                    if len(parts) > 0 and len(parts) != 5:
                        if not is_problem_file:
                            print(f"\n--- Sorunlu Dosya: {file_path} ---")
                            is_problem_file = True
                            problem_files += 1

                        print(f"  -> Satır {i+1}: {len(parts)} eleman içeriyor. (İçerik: {line.strip()})")
                        problem_lines += 1
            
            except Exception as e:
                print(f"Dosya okunurken hata oluştu: {file_path} - Hata: {e}")

    print("\n--- Tarama Tamamlandı ---")
    if problem_lines > 0:
        print(f"Toplam {problem_files} dosyada {problem_lines} sorunlu satır bulundu.")
    else:
        print("Tüm etiket dosyaları doğru formatta. (Her satır 5 elemanlı)")

if __name__ == "__main__":
    find_malformed_labels(LABELS_DIR)