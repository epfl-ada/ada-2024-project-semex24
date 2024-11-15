# analysis_functions.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Function of missing values

def plot_missing_values(movies_df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(movies_df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Missing value in the dataset')
    plt.show()

#function of categories

def number_categories(movies_df):
    all_genres = set()
    for genres_list in movies_df['genres']:
        if isinstance(genres_list, list):
            all_genres.update(genres_list)

    all_genres_list = sorted(all_genres)

    print("Number of genres:", len(all_genres_list))
    print(all_genres_list)

# Function to plot top movie-producing countries
def plot_top_10_countries(movies_df):
    country_counts = movies_df['countries'].explode().value_counts() 
    top_10_countries = country_counts.head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_countries.index, y=top_10_countries.values)
    plt.title('Top 10 Countries with the Most Movies')
    plt.xlabel('Country')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

# Function to plot the most popular movie languages
def plot_popular_languages(movies_df):
    
    movies_df['languages'] = movies_df['languages'].apply(
        lambda x: [
            y if y == 'Silent film' else  # leave 'Silent film' unchanged
            y[:-8] + 'Language' if y.lower().endswith('language') else  # if it ends in 'language' make it 'Language'
            y + ' Language'  # add ' Language' if it doesn't end with 'language'
            for y in x] if isinstance(x, list) else x
    )
    # Now do the same plot again
    language_counts = movies_df['languages'].explode().value_counts()
    top_10_languages = language_counts.head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_languages.index, y=top_10_languages.values)
    plt.title('Top 10 Languages with the Most Movies')
    plt.xlabel('Language')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

# Function to plot the distribution of movie budgets
def plot_budget_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['budget'], bins=30, kde=True)
    plt.title('Distribution of Movie Budgets')
    plt.xlabel('budget')
    plt.ylabel('Frequency')
    plt.show()


# Function to plot movie budgets in log scale (handling zero budgets)
def plot_log_scale_budget_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(np.log1p(movies_df['budget']), bins=30, kde=True)
    plt.title('Distribution of Movie Budgets')
    plt.xlabel('Log of budget')
    plt.ylabel('Frequency')
    plt.xticks(ticks=np.log1p([1e4,1e5,1e6, 1e7, 1e8, 1e9]), labels=[f'{int(x)}' for x in [1e4,1e5,1e6, 1e7, 1e8, 1e9]])
    plt.show()


# Function to plot the distribution of movie revenues
def plot_revenue_distribution(movies_df):
    plt.figure(figsize=(15, 6))
    sns.histplot(np.log1p(movies_df['revenue']), bins=30, kde=True)
    plt.title('Distribution of Movie Revenues')
    plt.xlabel('Log of revenue')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()


# 7. Function to plot the distribution of movies over the years
def plot_movies_over_years(movies_df):
    df_filtered = movies_df.dropna(subset=['release_year'])

    df_filtered = df_filtered[df_filtered['release_year'] >= 1800]

    plt.figure(figsize=(10, 6))
    sns.histplot(df_filtered['release_year'], bins=30, kde=True)
    plt.title('Distribution of Movie Release Years')
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
    sns.barplot(x=genres, y=counts)
    plt.title('Top 10 Most Popular Genres')
    plt.xlabel('Genre')

# Function to plot the distribution of popularity scores
def plot_popularity_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['popularity'], bins=30, kde=True)
    plt.title('Distribution of Movie popularity Scores')
    plt.xlabel('popularity Score')
    plt.ylabel('Frequency')
    

def plot_popularity(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['popularity'], bins=30, kde=True)
    plt.title('Distribution of Movie popularity Scores')
    plt.xlabel('popularity Score')
    plt.ylabel('Frequency')