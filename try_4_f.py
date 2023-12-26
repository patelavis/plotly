import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster

# Create a Dash web application
app = dash.Dash(__name__)

geolocator = Nominatim(user_agent="my_geocoder")

# Initial coordinates
initial_latitude = 22.3511148
initial_longitude = 78.6677428

# location = geolocator.geocode('India')

# Create an empty Folium map
# my_map = folium.Map(location=[location.latitude, location.longitude], zoom_start=5)
my_map = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=5)
    
# Add a marker with a popup to the map
marker = folium.Marker(location=[initial_latitude, initial_longitude], popup=folium.Popup(f"India", parse_html=True))
marker.add_to(my_map)
my_map.save("updated_map.html")

# Define the layout of the Dash application
app.layout = html.Div([
    html.Div([
        dcc.Input(id='location-text-input', type='text', value=''),
        # dcc.Input(id='latitude-input', type='number', value=initial_latitude, step=0.0001),
        # dcc.Input(id='longitude-input', type='number', value=initial_longitude, step=0.0001),
        html.Button('Update Map', id='update-button'),
    ]),
    html.Div([
        html.Iframe(id='map-iframe', srcDoc=open('updated_map.html', 'r').read(), width='100%', height='600'),
    ]),
])

# Define callback to update the map when the button is clicked
@app.callback(
    Output('map-iframe', 'srcDoc'),
    [Input('update-button', 'n_clicks')],
    [dash.dependencies.State('location-text-input', 'value')],
)
def update_map(n_clicks, location_name):
    # Create a new Folium map centered at the updated location
    location = geolocator.geocode(location_name)
    
    if location:
        # print(f"\nLocation Name: {pprint(location.raw)}\n")
        # print("Latitude, Longitude:", (location.latitude, location.longitude))
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
        my_map.save("updated_map.html")
        return open('updated_map.html', 'r').read()
    else:
        print("Location not found.")
        return open('updated_map.html', 'r').read()

# Run the Dash application
if __name__ == '__main__':
    app.run_server(debug=True)







# import dash
# from dash import dcc, html
# import folium
# from folium.plugins import MarkerCluster

# # Create a Plotly Dash web application
# app = dash.Dash(__name__)

# # Create a Folium map
# m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)

# # Add some markers to the map
# marker_cluster = MarkerCluster().add_to(m)
# folium.Marker([37.7749, -122.4194], popup='San Francisco').add_to(marker_cluster)
# folium.Marker([34.0522, -118.2437], popup='Los Angeles').add_to(marker_cluster)

# # Convert the Folium map to raw HTML
# folium_map_html = m.get_root().render()

# # Define the layout of the Plotly Dash app
# app.layout = html.Div([
#     dcc.Markdown(f"**Folium Map**"),
#     dcc.Markdown(folium_map_html, dangerously_allow_html=True)
# ])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)


# import dash
# from dash import dcc, html, Input, Output
# import folium
# from folium.plugins import MarkerCluster

# # Create a Plotly Dash web application
# app = dash.Dash(__name__)

# # Initial map with a default location
# initial_location = [37.7749, -122.4194]
# m = folium.Map(location=initial_location, zoom_start=10)

# # Marker cluster for the map
# marker_cluster = MarkerCluster().add_to(m)

# # Define the layout of the Plotly Dash app
# app.layout = html.Div([
#     dcc.Input(id='location-input', type='text', placeholder='Enter location (lat, lon)'),
#     html.Button('Update Map', id='update-button', n_clicks=0),
#     html.Div(id='folium-map')
# ])

# # Callback to update the Folium map when the button is clicked
# @app.callback(
#     Output('folium-map', 'children'),
#     [Input('update-button', 'n_clicks')],
#     [dash.dependencies.State('location-input', 'value')]
# )

# def update_folium_map(n_clicks, location_input):
#     # Parse the entered location (assuming input in the format "lat, lon")
#     try:
#         lat, lon = map(float, location_input.split(','))
#     except:
#         lat, lon = initial_location

#     # Clear existing markers
#     marker_cluster.clear_markers()

#     # Add a marker for the new location
#     folium.Marker([lat, lon], popup=f'Location: {lat}, {lon}').add_to(marker_cluster)

#     # Get the updated HTML code of the Folium map
#     folium_map_html = m.get_root().render()

#     return [html.Iframe(srcDoc=folium_map_html, width='100%', height='600')]

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
