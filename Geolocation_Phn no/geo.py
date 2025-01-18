import folium.map
import geocoder,folium

ip=geocoder.ip("me")

address=ip.latlng
mymap=folium.Map(location=address,zoom_start=12)
folium.Circle(address,radius=100).add_to(mymap)

map_name=input("Enter a Map Name=")

Map_save=mymap.save(f"{map_name}.html")