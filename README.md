# 🎯 YOLO'ya Giriş — Nesne Tespiti

Ultralytics YOLOv8 ile ilk nesne tespiti denemelerim. 
Hazır (COCO ile eğitilmiş) model kullanarak fotoğraf ve canlı kamerada tespit.

## 📂 Dosyalar
- `tespit.py` — Bir fotoğrafta nesne tespiti + güven eşiği (conf=0.5)
- `webcam.py` — Canlı kamerada gerçek zamanlı tespit (~33 FPS, CPU)
- `test.jpg` / `sonuc.jpg` — Örnek girdi ve tespit çıktısı

## 🧠 Öğrendiklerim
- Hazır model sadece COCO'nun 80 sınıfını tanır (makas ✓, kalem ✗)
- Güven skoru (confidence) düşükse model emin değildir; eşikle elenir
- YOLO gerçek zamanlı çalışır — CPU'da bile ~30 ms/kare

## 🚀 Çalıştırma
```bash
pip install ultralytics
python tespit.py
python webcam.py
```

## 🛠️ Teknolojiler
Python · Ultralytics YOLOv8 · OpenCV