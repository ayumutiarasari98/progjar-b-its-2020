# Tugas 7: Performance Test Web Server

link dokumentasi: [Dokumentasi Tugas 7](https://github.com/ayumutiarasari98/progjar-b-its-2020/blob/master/Tugas7/05111740000149.pdf)

1. Buka terminal, lalu jalankan ab -n 10 -c 1,5,10 http://127.0.0.1:10001/
![percobaan1](https://user-images.githubusercontent.com/56009915/79076389-f8d11200-7d23-11ea-84b1-6cc5288e3f74.PNG)
![percobaan1-2](https://user-images.githubusercontent.com/56009915/79076390-fa9ad580-7d23-11ea-8ff4-a927298830dc.PNG)

2. Jalankan ab -n 50 -c 1,10,30,50 http://127.0.0.1:10001/
![percobaan2](https://user-images.githubusercontent.com/56009915/79076394-fff82000-7d23-11ea-8640-91a94b565c1c.PNG)
![percobaan2-2](https://user-images.githubusercontent.com/56009915/79076395-025a7a00-7d24-11ea-9fb8-2db0f10bd02d.PNG)

3. Jalankan ab -n 100 -c 1,10,50,100 http://127.0.0.1:10001/
![percobaan3](https://user-images.githubusercontent.com/56009915/79076399-02f31080-7d24-11ea-8f2d-35e3fa7e9b44.PNG)
![percobaan3-2](https://user-images.githubusercontent.com/56009915/79076400-04243d80-7d24-11ea-872b-add71b7f0941.PNG)
