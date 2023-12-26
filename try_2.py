import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import folium

# Create a Dash web application
app = dash.Dash(__name__)

# Initial coordinates
initial_latitude = 37.7749
initial_longitude = -122.4194

# Create an empty Folium map
folium_map = folium.Map(location=[initial_latitude, initial_longitude], zoom_start=12)

# Add a marker with a popup to the Folium map
folium.Marker(location=[initial_latitude, initial_longitude], popup="Details when hovering").add_to(folium_map)

# Convert the Folium map to HTML
folium_map.save("updated_map.html")

# Define the layout of the Dash application
app.layout = html.Div([
    html.Div([
        dcc.Input(id='latitude-input', type='number', value=initial_latitude, step=0.0001),
        dcc.Input(id='longitude-input', type='number', value=initial_longitude, step=0.0001),
        html.Button('Update Map', id='update-button'),
    ]),
    html.Div([
        html.Iframe(id='map-iframe', srcDoc=open('initial_map.html', 'r').read(), width='100%', height='600'),
    ]),
])

# Define callback to update the map when the button is clicked
@app.callback(
    Output('map-iframe', 'srcDoc'),
    [Input('update-button', 'n_clicks')],
    [dash.dependencies.State('latitude-input', 'value'),
     dash.dependencies.State('longitude-input', 'value')]
)
def update_map(n_clicks, latitude, longitude):
    # Create a new Folium map centered at the updated location
    updated_folium_map = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker with a popup to the updated Folium map
    folium.Marker(location=[latitude, longitude], popup="Details when hovering").add_to(updated_folium_map)

    # Save the updated Folium map to HTML
    updated_folium_map.save("updated_map.html")

    # Return the updated HTML content for the iframe
    return open('updated_map.html', 'r').read()

# Run the Dash application
if __name__ == '__main__':
    
    app.run_server(debug=True)
