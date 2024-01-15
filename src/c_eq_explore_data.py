from pathlib import Path
import json
import plotly.express as px

"""Convert the json string into something more readable"""
json_data = Path('eq_data/eq_data_30_day_m1.geojson')
# saved json to a python object for usage

contents = json_data.read_text()
# converts the data on the file to a string
json_data_as_dictionary = json.loads(contents)
# converts the string into a dictionary (more so as a json object, similar to other languages like java)
# as we know, json's are just giant dictionaries (which could have nested dictionaries within)

json_data_formatted = Path('eq_data/eq_data_30_day_m1_readable.json')
# file path for where we'll save the reformated json (to make it more readable)
readable_contents = json.dumps(json_data_as_dictionary, indent=4)
# reorganizes the data to a more readable format (where nested elements have an indentation of 4 spaces (a tab))

json_data_formatted.write_text(readable_contents)
# writes the reorganized json to the file specified

"""A note that VS code actually does this for us when you save...but just in case you're not using vs code :D"""


"""Actually processing the JSON data"""

# Getting all of the individual earthquakes in the data set
all_eq_dictionaries = json_data_as_dictionary['features']
# in the eq json, 'features' is an array with various dictionaries in it, each one representing an earthquake
# we take all of those and put them here in the all_eq_dictionaries
# meaning all_eq_dictionaries is now a list full of dictionaries, that were found inside the features array/list

print(len(all_eq_dictionaries))
# print out the number of earthquakes found in the 'features' list in the dictionary

mags, lons, lats, titles = [], [], [], []
for indiv_eq in all_eq_dictionaries:
    mags.append(indiv_eq['properties']['mag'])
# loops through each individual earthquake
# goes into the properties key of each earthquake (the value is another dictionary of the various eq properties)
# looks for the mag key inside of properties
# appends the value of mag to mags
    lons.append(indiv_eq['geometry']['coordinates'][0])
    lats.append(indiv_eq['geometry']['coordinates'][1])
#same as above but gets the longitude/latitude too from all_eq_dictionaries
    titles.append(indiv_eq['properties']['title'])
    # same as above but gets title of each eq


print(mags[:10])
# prints the first 10 mags (mags contains all magnitudes from the json)

print(lons[:10])
print(lats[:10])
# prints longitude and latitude, first 10 values


"""Generate world map of earthquakes"""
title = 'Global Earthquakes'

fig = px.scatter_geo(lon=lons, lat=lats, title=title,
                    color=mags,
                    color_continuous_scale='Viridis',
                    labels={'color':'Magnitude'},
                    projection='natural earth',
                    # adds colors to the points
                    # viridis is the color scale from dark blue to bright yellow
                        # others exist too, see them via: px.colors.named_colorscales()
                    # color is chosen based on earthquake magnitude
                    hover_name=titles,
                    ).update_traces(
    marker=dict(size=4))
# creates a scatter diagram with the world map as the canvas, putting points based on their longitude and latitude
# update_traces changes sizes of the points

fig.show()
# generates the diagram

fig.write_html("worldwide_eqs.html")
# saves the generated html file

