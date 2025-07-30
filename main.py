import pandas as pd
import folium
from math import radians, cos, sin, asin, sqrt

MARMARA_LAT = 40.9
MARMARA_LON = 29.1

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6371 * c
    return km

df = pd.read_csv("depremler.csv")

df["uzaklik_km"] = df.apply(lambda row: haversine(MARMARA_LON, MARMARA_LAT, row["longitude"], row["latitude"]), axis=1)
df["tahmini_stres_artisi"] = df["mag"] / (df["uzaklik_km"] + 1)**2

m = folium.Map(location=[MARMARA_LAT, MARMARA_LON], zoom_start=2, tiles="cartodbpositron")

folium.Marker(
    location=[MARMARA_LAT, MARMARA_LON],
    popup="Marmara Bölgesi",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5 + row["mag"],
        color="crimson",
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['location']}<br>Büyüklük: {row['mag']}<br>Uzaklık: {row['uzaklik_km']:.0f} km<br>Stres: {row['tahmini_stres_artisi']:.1e}"
    ).add_to(m)

m.save("index.html")
print("✅ Harita oluşturuldu.")
