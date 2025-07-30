name: Günlük Harita Güncellemesi

on:
  schedule:
    - cron: '0 6 * * *'  # Her gün sabah 09:00'da (UTC+3)
  workflow_dispatch:

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
        python main.py

    - name: Haritayı GitHub’a kaydet
      run: |
        git config user.name github-actions
        git config user.email github-actions@github.com
        git add .
        git commit -m "Harita otomatik güncellendi"
        git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git HEAD:main
