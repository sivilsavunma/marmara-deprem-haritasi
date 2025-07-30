import pandas as pd
import folium
from geopy.distance import geodesic

url = (
    "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?"
    "starttime=2000-01-01&endtime=2025-07-30&minmagnitude=7"
    "&orderby=time&format=csv"
)
df = pd.read_csv(url)

marmara_coords = (40.85, 29.35)

df["MarmaraUzaklikKM"] = df.apply(
    lambda row: geodesic((row["latitude"], row["longitude"]), marmara_coords).km,
    axis=1
)

m = folium.Map(location=marmara_coords, zoom_start=3, tiles="CartoDB positron")

folium.CircleMarker(
    location=marmara_coords,
    radius=6,
    color='red',
    fill=True,
    fill_color='red',
    popup="Marmara Fayı"
).add_to(m)

for _, row in df.iterrows():
    try:
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=4 + row["mag"] / 1.5,
            color="blue",
            fill=True,
            fill_color="blue",
            fill_opacity=0.5,
            popup=folium.Popup(
                f"<b>{row['place']}</b><br>"
                f"Büyüklük: {row['mag']}<br>"
                f"Uzaklık: {round(row['MarmaraUzaklikKM'], 1)} km"
            , max_width=250)
        ).add_to(m)
    except:
        continue

m.save("index.html")
