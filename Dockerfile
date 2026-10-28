#hangi temel imaji kullanacagimiz secelim
#python 3.11 kullanalim
FROM python:3.11-slim


#container icinde calisma klasorunu belirle

WORKDIR /app

#requirements.txt
COPY requirements.txt .

# gerekli python kutuphanelerinin kurulumu yap
RUN pip install --no-cache-dir -r requirements.txt

#projedeki diger dosyalari container icine kopyalama 
COPY . .

# container ayaga kalkince hangi komut calissin onu soyluyoruz 
#fastapi uvicorn ile 8000 de calissin
#0.0.0.0 da yazmamizin sebebi ise container disinda erisile bilmesi olmali
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]









