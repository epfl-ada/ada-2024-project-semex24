# analysis_functions.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_missing_values(movies_df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(movies_df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title('Missing value in the dataset')
    plt.show()

# 1. Function to plot top movie-producing countries
def plot_top_10_countries(movies_df):
    country_counts = movies_df['countries'].explode().value_counts() #since we can have more than 1 country in countries column
    top_10_countries = country_counts.head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_countries.index, y=top_10_countries.values)
    plt.title('Top 10 Countries with the Most Movies')
    plt.xlabel('Country')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

# 2. Function to plot the most popular movie languages
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

# 3. Function to plot the distribution of movie budgets
def plot_budget_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(np.log1p(movies_df['budget']), bins=30, kde=True)
    plt.title('Distribution of Movie Budgets')
    plt.xlabel('Log of budget')
    plt.ylabel('Frequency')
    plt.xticks(ticks=np.log1p([1e4,1e5,1e6, 1e7, 1e8, 1e9]), labels=[f'{int(x)}' for x in [1e4,1e5,1e6, 1e7, 1e8, 1e9]])
    plt.show()


# 4. Function to plot movie budgets in log scale (handling zero budgets)
def plot_log_scale_budget_distribution(movies_df):
    log_budgets = movies_df['Budget'].replace(0, np.nan)
    log_budgets = np.log10(log_budgets.dropna()) 

    plt.figure(figsize=(10, 6))
    sns.histplot(log_budgets, bins=50, kde=True)
    plt.title('Distribution of Movie Budgets (Log Scale)')
    plt.xlabel('Log(Budget)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# 5. Function to describe budget statistics
def describe_budget(movies_df):
    return movies_df['Budget'].describe()

# 6. Function to plot the distribution of movie revenues
def plot_revenue_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['Revenue'], bins=50, kde=True)
    plt.title('Distribution of Movie Revenues')
    plt.xlabel('Revenue')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# 7. Function to plot the distribution of movies over the years
def plot_movies_over_years(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['Release Year'], bins=50, kde=True)
    plt.title('Distribution of Movies Through the Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.tight_layout()
    plt.show()

# 8. Function to plot the top 10 most popular movie genres
def plot_top_10_genres(movies_df):
    genre_counts = movies_df['Genres'].str.split(',').explode().str.strip().value_counts()
    top_10_genres = genre_counts.head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_10_genres.index, y=top_10_genres.values)
    plt.title('Top 10 Most Popular Movie Genres')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 9. Function to plot the distribution of popularity scores
def plot_popularity_distribution(movies_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(movies_df['Popularity'], bins=50, kde=True)
    plt.title('Distribution of Popularity Scores')
    plt.xlabel('Popularity Score')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
