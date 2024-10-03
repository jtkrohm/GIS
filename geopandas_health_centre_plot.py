import geopandas as gpd
import os
import json
import matplotlib
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
from geodatasets import get_path

# Specify the relevant file paths within the downloads folder

source_folder = os.path.expanduser("~/Documents\Career\AI\Data Science\GIS\GIS_Project_Data")
# OR os.path.expanduser("~") + '/Downloads/' +'/Documents/' + '/Career/' + '/AI/' + '/Data Science/' + '/GIS/' + '/Project Files'
file_path_country = os.path.join(source_folder, 'geoBoundaries-GRD-ADM1-all', "geoBoundaries-GRD-ADM1.shp")
# https://www.geoboundaries.org/countryDownloads.html


geojson_file_path_all = os.path.join(source_folder, "health_centre_data.geojson")


# Read Geojson file
world = gpd.read_file(file_path_country)
gdf_all = gpd.read_file(geojson_file_path_all)
# filtered_schools = gdf_all.loc[gdf_all['SchoolType'] == 'Primary']
print(gdf_all)

ax = world.plot(color='white', edgecolor='black')
gdf_all.plot(ax=ax, markersize=10, legend=True,  column='Ownership', categorical=True)
# filtered_schools.plot(ax=ax, markersize=10, legend=True,  column='SchoolType', categorical=True)
plt.title('Health Institution Locations in Grenada', loc="center")
plt.show()
