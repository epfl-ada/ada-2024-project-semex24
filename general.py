# analysis_functions.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

file_path = './data/movies_dataset.tsv'
movies_df = pd.read_csv(file_path, sep='\t')

import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_10_countries(movies_df):
 
    # Count different countries
    country_counts = movies_df['Movie countries'].explode().value_counts()  # Unpacks multiple countries per row
    top_10_countries = country_counts.head(10)

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_countries.index, y=top_10_countries.values)
    plt.title('Top 10 Countries with the Most Movies')
    plt.xlabel('Country')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()
