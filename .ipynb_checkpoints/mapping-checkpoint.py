import geopandas as gpd
import folium
import mapclassify
import matplotlib.pyplot as plt
import pandas as pd

class Mapping: 
                              
    def plot_df(self, df, column, cmap_colors): 
        
        #load county data
        geo_data = gpd.read_file(
            'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/US-counties.geojson')
        geo_data.id = geo_data.id.astype(str).astype(int)

        #shifting state/county codes from objects to integers

        geo_data['COUNTY'] = geo_data.COUNTY.astype(str).astype(int)
        geo_data['STATE'] = geo_data.STATE.astype(str).astype(int)
        
        #merge geodata and df
        merged_df = pd.merge(geo_data, df, left_on='COUNTY', right_on='County Code')
        merged_df["black_alone_percent"] = merged_df["Black Alone (F) %"] + merged_df["Black Alone (M) %"]

        fig, ax = plt.subplots(1,1)
        #ax.set_xlim(-130, -60)
        #ax.set_ylim(20, 55)
        plt.xlim(-130, -60)
        merged_df.plot(column=column, ax=ax, legend=True, cmap=cmap_colors)

        
