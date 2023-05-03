import folium # Define el mapa mundial centrado alrededor de Lima, Perú con un zoom bajo - Latitud, Longitud
world_map = folium.Map(location=[-12.0431800, -77.0282400], zoom_start=11) 

# mostrando el mapa
world_map