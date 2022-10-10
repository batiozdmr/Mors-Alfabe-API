# Case Kurulum Dokümantasyonu

1. Venv Sanal Ortam kurulumu 
```python
python -m venv tutorial-env
```
2. Venv Sanal Ortam Aktifleştirme
```python
cd tutorial-env\Scripts\activate.bat
```
3. Gerekli Dosyaların Yüklenmesi
```python
pip install -r requirements.txt
```
4. DB Tablo Oluşturulması 1
```python 
python manage.py makemigrations
```
5. DB Tablo Oluşturulması 2
```python 
python manage.py migrate
```
6. Proje Çalıştırılması
```python 
python manage.py runserver
```
7. Web Sayfasına Gidin
http://127.0.0.1:8000/


![enter image description here](https://rubasoft.s3.eu-central-1.amazonaws.com/media/upload/userFormUpload/KkqwBoyoPeq4Q3sDtUZje5NPeLqSHxSt.png)
