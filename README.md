# Python ile Trafik Işığı Tespiti

Bu uygulama kameradan gelen görüntüdeki trafik ışıklarını gerçek zammanlı olarak tanır ve ekranda gösterir.

### Özellikleri
* **Canlı Tespit:** Açtığınız anda kameradan trafik ışıklarını bulmaya başlar.
* **FPS:** Sol üst köşede sistemin anlık hızını gösterir.
* **GPU Performansı:** NVIDIA ekran kartı var ise çok daha performanslı çalışır (CUDA).
* **Teknolojiler:** YOLOv9 modeli kullanılmış ve OpenCV desteklidir.

### Kurulum
Çalıştırmak için şu komut ile gereksinimleri yüklemelisin:

```bash
pip install ultralytics opencv-python torch
```

### Çalıştırma
v9_64_epochs.pt dosyasını kodun olduğu klasöre koy. Ve Python dosyanı çalıştır.

### Örnekler

![test](https://github.com/user-attachments/assets/31b8e4a4-268e-4174-af9b-2b2f014b8765)

<img width="1120" height="651" alt="image" src="https://github.com/user-attachments/assets/9b0f589a-84b5-4611-a7eb-ff9e2f830fde" />

<img width="1274" height="747" alt="image" src="https://github.com/user-attachments/assets/cb0f1ed1-4d03-4cf7-969e-a9f1bb381a0d" />

