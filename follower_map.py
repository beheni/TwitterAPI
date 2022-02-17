import json
import folium
from geopy.geocoders import Nominatim

def loading_from_json(path_to_file: str) -> dict:
    """
Deserializes json file into python object
    """
    with open(path_to_file) as file:
        data = json.load(file)
    return data

def get_location_dict(all_data: dict) -> dict:
    """
Rearranges data in order to get only user's name and location in a dict
Args:
    all_data (dict): deserialized from a json file
Returns:
    dict: {"user name": "location"}
    """
    dict_name_location = {}
    list_users_data = all_data["users"]
    for user in list_users_data: #user is a dict here
        #user name
        dict_name_location[user["name"]] = user["location"] #user location
    return dict_name_location

def get_coordanates_geopy(dict_name_location: dict) -> dict:
    """
Gets latitude and longitude of every user's location
Args:
    dict_name_location (dict): {"user name": "location"}
Returns:
    dict: {"user name": (latitude, longitude)}
    """
    list_to_remove = []
    geolocator = Nominatim(user_agent="friends_map")
    for name, location in dict_name_location.items():
        try:
            coord = geolocator.geocode(location)
            dict_name_location[name] = (coord.latitude, coord.longitude)
        except AttributeError:
            list_to_remove.append(name)
    
    for wrong_location in list_to_remove:
        while wrong_location in dict_name_location:
            dict_name_location.pop(wrong_location)
    return dict_name_location

def generating_map(dict_name_coordinates: dict):
    """
Generates an HTLM map with markers on the locations of accounts which user follows
Args:
    dict_name_coordinates (dict): {"user name": (latitude, longitude)}
Returns:
    None
    """
    map = folium.Map(tiles="cartodbdark_matter", control_scale=True, location = [30.4501, 15.5234], zoom_start = 3)
    fg = folium.FeatureGroup(name="Following users")
    circle_markers = folium.FeatureGroup(name = "Circle markers")
    for name, coords in dict_name_coordinates.items():
        fg.add_child(folium.Marker(location = [coords[0], coords[1]], popup = name, icon = folium.Icon(icon = "bird", color = "green")))
        circle_markers.add_child(folium.CircleMarker(location = [coords[0], coords[1]], radius = 15, color = "orange", fill_color = "orange"))
    
    map.add_child(fg)
    map.add_child(circle_markers)
    map.add_child(folium.LayerControl())
    map.save('Map.html')



if __name__ == "__main__":
    generating_map(get_coordanates_geopy(get_location_dict(loading_from_json("new.json"))))

