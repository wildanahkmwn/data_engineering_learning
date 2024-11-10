# image docker dasar
FROM python

#menjalankan instalasi library yang di butuhkan di image ini
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

# mengatur direktori kerja didalam container
WORKDIR /app

# menyalin skrip ke container. Nama pertama adalah file sumber dan nama kedua adalah file tujuan
COPY ingest_data.py ingest_data.py

# mendefinisikan apa yang akan di lakukan pertama kali ketika container dijalankan
# dalam contoh ini, kita akan menjalankan skrip pipeline.py
ENTRYPOINT [ "python","ingest_data.py" ]