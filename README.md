# Python ile Trafik Işığı Tespiti

Bu uygulama kameradan gelen görüntüdeki trafik ışıklarını gerçek zammanlı olarak tanır ve ekranda gösterir.

### Özellikleri
* **Canlı Tespit:** Açtığınız anda kameradan trafik ışıklarını bulmaya başlar.
* **FPS:** Sol üst köşede sistemin anlık hızını gösterir.
* **GPU Performansı:** NVIDIA ekran kartı var ise çok daha performanslı çalışır (CUDA).
* **Teknolojiler:** YOLOv9 modeli kullanılmış ve OpenCV desteklidir.

### 🛠️ Kurulum
Çalıştırmak için şu komut ile gereksinimleri yüklemelisin:

```bash
pip install ultralytics opencv-python torch
```

### Çalıştırma
v9_64_epochs.pt dosyasını kodun olduğu klasöre koy.

Python dosyanı çalıştır.
