name: Günlük Harita Güncellemesi

on:
  schedule:
    - cron: '0 6 * * *'  # Her gün sabah 06:00'da çalışır (UTC)
  workflow_dispatch:     # Manuel başlatmak için

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Depoyu klonla
      uses: actions/checkout@v3

    - name: Python kur
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Paketleri yükle
      run: |
        pip install -r requirements.txt

    - name: Haritayı oluştur
      run: |
        python harita_olustur.py

    - name: Haritayı GitHub’a kaydet
      run: |
        git config user.name "github-
