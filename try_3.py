from geopy.geocoders import Nominatim
from pprint import pprint
import folium

geolocator = Nominatim(user_agent="my_geocoder")

def get_coordinates(location_name):
    # location_name = "1600 Amphitheatre Parkway, Mountain View, CA"
    
    # Perform geocoding using Nominatim
    location = geolocator.geocode(location_name)
    
    if location:
        print(f"\nLocation Name: {pprint(location.raw)}\n")
        print("Latitude, Longitude:", (location.latitude, location.longitude))
        splited_address = str(location.address).split(',')
        length_add = len(splited_address)
        if length_add == 1: zoom_start = 5
        elif length_add == 2: zoom_start = 7
        elif length_add == 3: zoom_start = 9
        elif length_add == 4: zoom_start = 11
        elif length_add == 5: zoom_start = 12
        elif length_add == 6: zoom_start = 13
        elif length_add >= 7: zoom_start = 15
        
        my_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=zoom_start)
    
        # Add a marker with a popup to the map
        marker = folium.Marker(location=[location.latitude, location.longitude], popup=folium.Popup(f"{location.address}", parse_html=True))
        marker.add_to(my_map)
        return my_map
    else:
        print("Location not found.")
        