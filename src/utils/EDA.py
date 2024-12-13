# analysis_functions.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Patch

# Function of missing valuess
def plot_missing_values(movies_df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(movies_df.isnull(), cbar=False, cmap='autumn', yticklabels=False )
    plt.title('Missing Values in the Dataset', pad=20)
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    legend_elements = [Patch(facecolor='yellow', edgecolor='black', label='Missing Value')]
    plt.legend(handles=legend_elements, loc='upper left')
    plt.show()

#function of categories
def number_categories(movies_df):
    all_genres = set()
    for genres_list in movies_df['genres']:
        if isinstance(genres_list, list):
            all_genres.update(genres_list)

    all_genres_list = sorted(all_genres)

    print("Number of genres:", len(all_genres_list))
    print(*all_genres_list, sep='\n')

# Function to plot top movie-producing countries
def plot_top_10_countries(movies_df):
    country_counts = movies_df['countries'].explode().value_counts()
    top_10_countries = country_counts.head(10)

    plt.figure(figsize=(12, 8))
    sns.barplot(
        x=top_10_countries.index, 
        y=top_10_countries.values, 
        palette=['#f0390f', '#f8c03f', '#1ecbe1', '#0fa4a8', '#e0e0e0']
    )

    plt.title('Top 10 Countries with the Most Movies', pad=20)
    plt.xlabel('Country', labelpad=10)
    plt.ylabel('Number of Movies', labelpad=10)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

# Function to plot the most popular movie languages
def plot_popular_languages(movies_df):
    
    movies_df['languages'] = movies_df['languages'].apply(
        lambda x: [
            y if y == 'Silent film' else 
            y[:-8] + 'Language' if y.lower().endswith('language') else  
            y + ' Language'  
            for y in x] if isinstance(x, list) else x
    )
    
    language_counts = movies_df['languages'].explode().value_counts()
    top_10_languages = language_counts.head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_languages.index, 
                y=top_10_languages.values, 
                palette=['#f0390f', '#f8c03f', '#1ecbe1', '#0fa4a8', '#e0e0e0']
    )
    plt.title('Top 10 Languages with the Most Movies')
    plt.xlabel('Language')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()


# Function to plot movie budgets in log scale 
def plot_log_scale_budget_distribution(movies_df):
    plt.figure(figsize=(12, 8))
    sns.histplot(
        np.log1p(movies_df['budget']), 
        bins=30, 
        kde=True, 
        color='#f0390f'
    )

    plt.title('Distribution of Movie Budgets', pad=20)
    plt.xlabel('Budget (Log Scale)', labelpad=10)
    plt.ylabel('Frequency', labelpad=10)
    plt.xticks(
        ticks=np.log1p([1e4, 1e5, 1e6, 1e7, 1e8, 1e9]), 
        labels=[f'{int(x):,}' for x in [1e4, 1e5, 1e6, 1e7, 1e8, 1e9]],
        rotation=45
    )

    plt.tight_layout()
    plt.show()

# Function to plot the distribution of movie revenues
def plot_revenue_distribution(movies_df):
    plt.figure(figsize=(15, 6))
    sns.histplot(
        np.log1p(movies_df['revenue']), 
        bins=30, 
        kde=True, 
        color='#f0390f'
    )

    plt.title('Distribution of Movie Revenues', pad=20)
    plt.xlabel('Revenue (Log Scale)', labelpad=10)
    plt.ylabel('Frequency', labelpad=10)
    plt.xticks(
        ticks=np.log1p([1e4, 1e5, 1e6, 1e7, 1e8, 1e9]), 
        labels=[f'{int(x):,}' for x in [1e4, 1e5, 1e6, 1e7, 1e8, 1e9]],
        rotation=45
    )

    plt.tight_layout()
    plt.show()

# Function to plot the distribution of movies over the years
def plot_movies_over_years(movies_df):
    df_filtered = movies_df.dropna(subset=['release_year'])
    df_filtered = df_filtered[df_filtered['release_year'] >= 1800]
    
    plt.figure(figsize=(10, 6))
    sns.histplot(df_filtered['release_year'], bins=30, kde=True, color='#f0390f')
    plt.title('Distribution of Movie Release Years', pad=20)
    plt.xlabel('Release Year', labelpad=10)
    plt.ylabel('Frequency', labelpad=10)
    plt.tight_layout()
    plt.show()

# Function to plot the top 10 most popular movie genres
def plot_top_10_genres(movies_df):

    genre_counts = {}

    for genre_list in movies_df['genres'].dropna():
        for genre in genre_list:
            genre = genre.strip()
            if genre in genre_counts:
                genre_counts[genre] += 1
            else:
                genre_counts[genre] = 1

    most_common_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    print("10 Most Popular Genres:")
    for genre, count in most_common_genres:
        print(f"{genre}: {count}")
        
    
    plt.figure(figsize=(10, 6))
    genres, counts = zip(*most_common_genres)
    sns.barplot(x=genres, y=counts, palette=['#f0390f', '#f8c03f', '#1ecbe1', '#0fa4a8', '#e0e0e0'])
    plt.title('Top 10 Most Popular Genres', pad=20)
    plt.xlabel('Genre', labelpad=10)
    plt.ylabel('Count', labelpad=10)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    
# Function to plot the populartity distribution
def plot_popularity(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(np.log1p(movies_df['popularity']), bins=30, kde=True, color='#f0390f')
    plt.title('Distribution of Movie Popularity Scores', pad=20)
    plt.xlabel('Popularity Score (Log Scale)', labelpad=10)
    plt.ylabel('Frequency', labelpad=10)
    plt.xticks(
        ticks=np.log1p([1e1, 1e2, 1e3]), 
        labels=[f'{int(x):,}' for x in [1e1, 1e2, 1e3]],
        rotation=45
    )
    plt.tight_layout()
    plt.show()