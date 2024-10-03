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
file_path_base_map = os.path.join(source_folder, 'geoBoundaries-GRD-ADM1-all', "geoBoundaries-GRD-ADM1.shp")
# https://www.geoboundaries.org/countryDownloads.html


geojson_file_path = os.path.join(source_folder, "all_school_data.geojson")


# Read Geojson file
world = gpd.read_file(file_path_base_map)
gdf_all = gpd.read_file(geojson_file_path)
filtered_schools = gdf_all.loc[gdf_all['SchoolType'] == 'Primary School']
print(filtered_schools)

ax = world.plot(color='white', edgecolor='black')
# gdf_all.plot(ax=ax, markersize=10, legend=True,  column='SchoolType', categorical=True)
filtered_schools.plot(ax=ax, markersize=10, legend=True,  column='SchoolType', categorical=True)
plt.title('School Locations in Grenada', loc="center")
plt.show()
