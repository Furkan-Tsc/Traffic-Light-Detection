from ultralytics import YOLO
import cv2
import time
import torch
from ultralytics.nn.tasks import DetectionModel

#kamera ayarları
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera açılamadı")

#önceden eğitilmiş modeli yükle
torch.serialization.add_safe_globals([DetectionModel])
try:
    model = YOLO("v9_64_epochs.pt")
    model.to('cuda') #cuda kullanarak fpsi büyük oranda arttırma (nvidia gpu için)
except Exception as e:
    print(f"Hata: {e}")

classNames = model.names #modeldeki isimler

#fps için değişkenler
prev_frame_time = 0
new_frame_time = 0

while True:
    success, img = cap.read()
    if not success:
        print("Kare okunamadı")
        break
    
    #modeli başlat
    results = model(img, stream=True, half=True)
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #kararlılık kontrolü
            confidence = box.conf[0].item()
            if confidence < 0.45: #0.45den küçükse umursama
                continue
            
            x1, y1, x2, y2 = map(int, box.xyxy[0]) #kordinatları çek
            
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3) #kutu çizimi
            
            #doğru sınıfı seç ve yaz
            cls = int(box.cls[0])
            text = f"{classNames[cls]} {confidence:.2f}"
            
            #yazıyı ekrana ekle
            cv2.putText(img, text, (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    new_frame_time = time.time() #fps hesaplama
    
    #zero division hatasını önlemek için kontrol (fps = 1/diff(geçen süre) diff 0 olur ise x/0 = tanımsız = zerodivisionerror a sebep olur)
    diff = new_frame_time - prev_frame_time
    if diff > 0:
        fps = 1 / diff
    else:
        fps = 0
        
    prev_frame_time = new_frame_time
    
    #fpsi ekrana yaz
    cv2.putText(img, f"FPS: {int(fps)}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    cv2.imshow('Webcam', img)
    
    #q tuşu ile sonlandır
    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty('Webcam', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
