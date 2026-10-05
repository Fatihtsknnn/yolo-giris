from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("test.jpg",conf=0.5)

for kutu in results[0].boxes:
    sinif_id = int(kutu.cls[0])
    sinif_adi = model.names[sinif_id]
    guven = float(kutu.conf[0])
    print(f"Bulundu: {sinif_adi}-> güven: {guven:.2f}")


results[0].save(filename="sonuc.jpg")    