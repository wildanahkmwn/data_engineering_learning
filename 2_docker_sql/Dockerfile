# image docker dasar
FROM python

#menjalankan instalasi library yang di butuhkan di image ini
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

# mengatur direktori kerja didalam container
WORKDIR /app

# menyalin skrip ke container. Nama pertama adalah file sumber dan nama kedua adalah file tujuan
COPY data-loading-parquet.py data-loading-parquet.py

# mendefinisikan apa yang akan di lakukan pertama kali ketika container dijalankan
# dalam contoh ini, kita akan menjalankan skrip pipeline.py
ENTRYPOINT [ "python","data-loading-parquet.py" ]