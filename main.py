import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Veri dosyasını oku
df = pd.read_csv("depremveri.csv")  # CSV dosyanın adı bu olmalı

# Harita oluştur
harita = folium.Map(location=[40.9, 29.3], zoom_start=7)
marker_cluster = MarkerCluster().add_to(harita)

# Noktaları işle
for i, row in df.iterrows():
    lokasyon = [row["lat"], row["lon"]]
    popup_icerik = f"Tarih: {row['tarih']}<br>Büyüklük: {row['buyukluk']}<br>Derinlik: {row['derinlik']} km"
    folium.Marker(location=lokasyon, popup=popup_icerik).add_to(marker_cluster)

# Haritayı HTML olarak kaydet
harita.save("index.html")

print("✅ Harita başarıyla oluşturuldu.")
