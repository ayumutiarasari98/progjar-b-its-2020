# Tugas 10: Asynchronous Processing - Backend Server

1. Jalankan async_server.py pada port 9002, 9003, 9004, 9005 (lihat pada BackendList)
![runserver](https://user-images.githubusercontent.com/56009915/81650778-67f17180-945c-11ea-87a8-85f2e8795a4c.PNG)

2. Jalankan file lb.py, jalankan di port 44444
![runlb](https://user-images.githubusercontent.com/56009915/81650789-69bb3500-945c-11ea-827b-e9960c2ab08b.PNG)

3. Jalankan browser, akseslah http://localhost:44444/page.html
![browser4444](https://user-images.githubusercontent.com/56009915/81650794-6b84f880-945c-11ea-8cf4-299a71187a88.PNG)
![browser4444 network](https://user-images.githubusercontent.com/56009915/81650802-6cb62580-945c-11ea-9a4a-9562a4c3147f.PNG)

4. Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian
![log program tugas10](https://user-images.githubusercontent.com/56009915/81650818-7049ac80-945c-11ea-9296-e8c3e5a8f72b.PNG)

5. Lakukan performance test seperti pada tugas 9, bandingkan penggunaan load balancer dengan async_server dengan server_thread_http pada folder progjar5
dan buatlah tabel hasilnya:
</br>
async_server.py</br>

![asynser](https://user-images.githubusercontent.com/56009915/81650838-75a6f700-945c-11ea-8d15-5cde42a30a8f.PNG)

server_async_http.py</br>
![asynchttp](https://user-images.githubusercontent.com/56009915/81650851-78095100-945c-11ea-8ca6-f6d628eba7c8.PNG)

server_thread_http.py</br>
![threadhttp](https://user-images.githubusercontent.com/56009915/81650863-7b044180-945c-11ea-8697-4453e2538139.PNG)
