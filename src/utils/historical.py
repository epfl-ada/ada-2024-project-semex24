import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from numpy.polynomial import Polynomial

def comparison_genres_war_periods(movies_df):
    # We first made dataframes per period (WW1, nonwar, WW2)
    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    # Then we obtained the counts for each movie genre
    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    non_war_genre_counts = non_war_movies_df['genres'].explode().value_counts()

    # And finaly we plotted all the genres with their respectime amount of movies
    genre_comparison_df = pd.DataFrame({'WW1': ww1_genre_counts, 'Non-War': non_war_genre_counts, 'WW2': ww2_genre_counts}).fillna(0)
    genre_comparison_df.plot(
        kind='bar', 
        figsize=(14, 7), 
        color=['#f0390f', '#f8c03f', '#1ecbe1'], 
        edgecolor='none',
        logy=True
    )
    plt.title("Comparison of Genres During WW1, Non-War Period, and WW2", pad=20)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Frequency of Movies (Log Scale)", labelpad=10)
    plt.legend(["WW1", "Non-War (1920-1938)", "WW2"], title="Periods")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def percentage_genres_war_periods(movies_df):
    # Now we repeated the steps from above but, obtained the percentages of each genre and plotted them

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    non_war_genre_counts = non_war_movies_df['genres'].explode().value_counts()

    # We calculated the percentages by dividing all the counts by the sum of each genre
    ww1_genre_percentages = (ww1_genre_counts / ww1_genre_counts.sum()) * 100
    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    non_war_genre_percentages = (non_war_genre_counts / non_war_genre_counts.sum()) * 100

    genre_comparison_df = pd.DataFrame({
        'WW1': ww1_genre_percentages,
        'Non-War': non_war_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    genre_comparison_df.plot(
        kind='bar', 
        figsize=(14, 7), 
        color=['#f0390f', '#f8c03f', '#1ecbe1'], 
        edgecolor='none', 
        logy=True
    )
    plt.title("Percentage of Genres During WW1, Non-War Period, and WW2", pad=20)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Percentage of Movies (Log Scale)", labelpad=10)
    plt.legend(["WW1", "Non-War (1920-1938)", "WW2"], title="Periods")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def percentage_genres_war_periods_all_movies(movies_df):
    # We repeated the process from above with the difference of getting all the movies instead of only movies from 1920-1938

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    all_movies_df = movies_df

    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    all_genre_counts = all_movies_df['genres'].explode().value_counts()

    ww1_genre_percentages = (ww1_genre_counts / ww1_genre_counts.sum()) * 100
    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    all_genre_percentages = (all_genre_counts / all_genre_counts.sum()) * 100

    genre_comparison_percent_df = pd.DataFrame({
        'WW1': ww1_genre_percentages,
        'All Movies': all_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    genre_comparison_percent_df.plot(
        kind='bar', 
        figsize=(14, 7), 
        color=['#f0390f', '#f8c03f', '#1ecbe1'], 
        edgecolor='none', 
        logy=True
    )
    plt.title("Percentage of Genres During WW1, All Movies, and WW2", pad=20)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Percentage of Movies (Log Scale)", labelpad=10)
    plt.legend(["WW1", "All Movies", "WW2"], title="Periods")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def genres_over_time(movies_df):
    # We first separate the movies by genre and get the amount for each one

    movies_exploded_df = movies_df.explode('genres')
    genre_counts_by_year = movies_exploded_df.groupby('release_year')['genres'].value_counts().unstack(fill_value=0)

    # Then we obtained the percentage relative to all the movies for each genre
    genre_percentage_by_year = genre_counts_by_year.div(genre_counts_by_year.sum(axis=1), axis=0) * 100

    plt.figure(figsize=(14, 7))

    for genre in genre_percentage_by_year.columns:
        plt.plot(genre_percentage_by_year.index, genre_percentage_by_year[genre], label=genre)

    plt.title("Percentage of Genres Over Time (Respect to All Movies)", pad=20)
    plt.xlabel("Year", labelpad=10)
    plt.ylabel("Percentage of Movies", labelpad=10)
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout()

    plt.show()



def number_movies(movies_df):
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(movie_count_by_year.index, movie_count_by_year.values, marker='o', linestyle='-', color='#f0390f')
    plt.xlabel('Year of Release', labelpad=10)
    plt.ylabel('Number of Movies', labelpad=10)
    plt.title('Number of Movies Released by Year', pad=15)
    plt.grid(visible=True, linestyle='--', linewidth=0.7, alpha=0.7)
    plt.tight_layout()
    plt.show()


def number_movies_1900_1950(movies_df):
    # We created a dataframe only for movies between 1900-1950 and repeated the steps from above
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    filtered_movie_count = movie_count_by_year[(movie_count_by_year.index >= 1900) & (movie_count_by_year.index <= 1950)]

    plt.figure(figsize=(10, 5))
    plt.plot(filtered_movie_count.index, filtered_movie_count.values, marker='o', color='#f0390f')
    plt.xlabel('Year of release')
    plt.ylabel('Number of movies')
    plt.title('Number of movies released by year (1900-1950)')
    plt.grid(True)
    plt.show()

def number_movies_war(movies_df):
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    # Getting the amount of movies for each war
    movies_1914_1919 = movie_count_by_year[(movie_count_by_year.index >= 1914) & (movie_count_by_year.index <= 1918)].sum()
    movies_1939_1945 = movie_count_by_year[(movie_count_by_year.index >= 1939) & (movie_count_by_year.index <= 1945)].sum()

    print(f"Number of movies from 1914 to 1919: {movies_1914_1919}")
    print(f"Number of movies from 1939 to 1945: {movies_1939_1945}")


def genre_comparison_war_period(movies_df):
    # WW2 and Non-War period genre comparison (Frequency)
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    non_war_genre_counts = non_war_movies_df['genres'].explode().value_counts()

    genre_comparison_df = pd.DataFrame({
        'Non-War': non_war_genre_counts,
        'WW2': ww2_genre_counts
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_df.plot(kind='bar', color=['#f0390f', '#f8c03f', '#1ecbe1'])
    plt.title("Comparison of Genres During WW2 and Non-War Period", pad=15)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Frequency of Movies", labelpad=10)
    plt.legend(["Non-War (1920-1938)", "WW2"])
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

    # WW2 and Non-War period genre comparison (Percentage)
    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]

    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    non_war_genre_percentages = (non_war_genre_counts / non_war_genre_counts.sum()) * 100

    genre_comparison_percent_df = pd.DataFrame({
        'Non-War': non_war_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_percent_df.plot(kind='bar', color=['#f0390f', '#f8c03f', '#1ecbe1'])
    plt.title("Percentage of Genres During WW2 and Non-War Period", pad=15)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Percentage of Movies", labelpad=10)
    plt.legend(["Non-War (1920-1938)", "WW2"])
    plt.tight_layout()
    plt.yscale('log')
    plt.show()

    # WW2 and All Movies genre comparison (Percentage)
    all_movies_df = movies_df
    all_genre_counts = all_movies_df['genres'].explode().value_counts()

    all_genre_percentages = (all_genre_counts / all_genre_counts.sum()) * 100

    genre_comparison_percent_all_df = pd.DataFrame({
        'All Movies': all_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_percent_all_df.plot(kind='bar', color=['#f0390f', '#f8c03f', '#1ecbe1'])
    plt.title("Percentage of Genres of All Movies and WW2 Movies", pad=15)
    plt.xlabel("Genres", labelpad=10)
    plt.ylabel("Percentage of Movies", labelpad=10)
    plt.legend(["All Movies", "WW2"])
    plt.tight_layout()
    plt.yscale('log')
    plt.show()




def war_movies_timeline(movies_df):
    # Filter for War movies and calculate counts by year
    war_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    # Calculate the percentage of War movies
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Total movies and War movies
    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies', linewidth=2)
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='#f8c03f', label='War Movies', linewidth=2)

    # Set the primary axis labels and colors
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Total Number of Movies / War Movies', color='#f0390f', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#f0390f')
    ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Percentage of War movies on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='#1ecbe1', label='% War Movies', linestyle='--', linewidth=2)
    ax2.set_ylabel('Percentage of War Movies', color='#1ecbe1', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    # Highlight WW1 and WW2 periods
    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.5, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.5, label="WW2 Period (1939-1945)")

    # Add a title and legends
    plt.title('Total Movies, War Movies, and Percentage of War Movies Released by Year', fontsize=14, pad=15)
    ax1.legend(loc='upper left', fontsize=10)
    ax2.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.show()



def war_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    war_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_war_movies = len(war_movies_df)

    total_war_percentage = (total_war_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_war_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    ww2_war_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    non_war_war_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]

    ww1_war_percentage = (len(ww1_war_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_war_percentage = (len(ww2_war_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_war_percentage = (len(non_war_war_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of War Movies in the Entire Dataset: {total_war_percentage:.2f}%")
    print(f"Percentage of War Movies During WW1 (1914-1918): {ww1_war_percentage:.2f}%")
    print(f"Percentage of War Movies During WW2 (1939-1945): {ww2_war_percentage:.2f}%")
    print(f"Percentage of War Movies During Non-War Period (1920-1938): {non_war_war_percentage:.2f}%")


def crime_movies_timeline(movies_df):
    # Filter for Crime movies and calculate counts by year
    crime_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]
    crime_movie_count_by_year = crime_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    crime_percentage_by_year = (crime_movie_count_by_year / total_movies_by_year) * 100

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Plot total movies and Crime movies
    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies', linewidth=2)
    ax1.plot(crime_movie_count_by_year.index, crime_movie_count_by_year.values, color='#f8c03f', label='Crime Movies', linewidth=2)

    # Set the primary axis labels and colors
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Total Number of Movies / Crime Movies', color='#f0390f', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#f0390f')
    ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    # Create the secondary axis for percentage of Crime movies
    ax2 = ax1.twinx()
    ax2.plot(crime_percentage_by_year.index, crime_percentage_by_year.values, color='#1ecbe1', label='% Crime Movies', linestyle='--', linewidth=2)
    ax2.set_ylabel('Percentage of Crime Movies', color='#1ecbe1', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    # Highlight WW1 and WW2 periods
    rect1 = ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.5, label="WW1 Period (1914-1918)")
    rect2 = ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.5, label="WW2 Period (1939-1945)")

    # Add legends for both axes
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Add title and layout adjustments
    plt.title('Total Movies, Crime Movies, and Percentage of Crime Movies Released by Year', fontsize=14, pad=15)
    plt.tight_layout()
    plt.show()



def crime_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    crime_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_crime_movies = len(crime_movies_df)

    total_crime_percentage = (total_crime_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_crime_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]
    ww2_crime_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]
    non_war_crime_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]

    ww1_crime_percentage = (len(ww1_crime_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_crime_percentage = (len(ww2_crime_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_crime_percentage = (len(non_war_crime_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of Crime Movies in the Entire Dataset: {total_crime_percentage:.2f}%")
    print(f"Percentage of Crime Movies During WW1 (1914-1918): {ww1_crime_percentage:.2f}%")
    print(f"Percentage of Crime Movies During WW2 (1939-1945): {ww2_crime_percentage:.2f}%")
    print(f"Percentage of Crime Movies During Non-War Period (1920-1938): {non_war_crime_percentage:.2f}%")


def mystery_movies_timeline(movies_df):
    #Used the same code as before but now for Mystery movies
    mystery_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]
    mystery_movie_count_by_year = mystery_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    mystery_percentage_by_year = (mystery_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies', linewidth=2)
    ax1.plot(mystery_movie_count_by_year.index, mystery_movie_count_by_year.values, color='#f8c03f', label='Mystery Movies', linewidth=2)

    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Total Number of Movies / Mystery Movies', color='#f0390f', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#f0390f')
    ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

    ax2 = ax1.twinx()
    ax2.plot(mystery_percentage_by_year.index, mystery_percentage_by_year.values, color='#1ecbe1', label='% Mystery Movies', linestyle='--', linewidth=2)
    ax2.set_ylabel('Percentage of Mystery Movies', color='#1ecbe1', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')


    rect1 = ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.5, label="WW1 Period (1914-1918)")
    rect2 = ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.5, label="WW2 Period (1939-1945)")


    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')


    plt.title('Total Movies, Mystery Movies, and Percentage of Mystery Movies Released by Year', fontsize=14, pad=15)
    plt.tight_layout()
    plt.show()



def mystery_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    mystery_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_mystery_movies = len(mystery_movies_df)

    total_mystery_percentage = (total_mystery_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_mystery_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]
    ww2_mystery_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]
    non_war_mystery_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]

    ww1_mystery_percentage = (len(ww1_mystery_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_mystery_percentage = (len(ww2_mystery_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_mystery_percentage = (len(non_war_mystery_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of Mystery Movies in the Entire Dataset: {total_mystery_percentage:.2f}%")
    print(f"Percentage of Mystery Movies During WW1 (1914-1918): {ww1_mystery_percentage:.2f}%")
    print(f"Percentage of Mystery Movies During WW2 (1939-1945): {ww2_mystery_percentage:.2f}%")
    print(f"Percentage of Mystery Movies During Non-War Period (1920-1938): {non_war_mystery_percentage:.2f}%")


def documentary_movies_timeline(movies_df):
    #Used the same code as before but now for Documentary movies but applied log so results are better visualy

    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_movie_count_by_year = documentary_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    documentary_movie_count_by_year = documentary_movie_count_by_year[documentary_movie_count_by_year.index >= 1900]
    total_movies_by_year = total_movies_by_year[total_movies_by_year.index >= 1910]

    documentary_percentage_by_year = (documentary_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    # We apply log function
    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='#f0390f', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='#f8c03f', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='#1ecbe1', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (Starting from 1900)')

    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def documentary_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_documentary_movies = len(documentary_movies_df)

    total_documentary_percentage = (total_documentary_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_documentary_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    ww2_documentary_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    non_war_documentary_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]

    ww1_documentary_percentage = (len(ww1_documentary_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_documentary_percentage = (len(ww2_documentary_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_documentary_percentage = (len(non_war_documentary_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of Documentary Movies in the Entire Dataset: {total_documentary_percentage:.2f}%")
    print(f"Percentage of Documentary Movies During WW1 (1914-1918): {ww1_documentary_percentage:.2f}%")
    print(f"Percentage of Documentary Movies During WW2 (1939-1945): {ww2_documentary_percentage:.2f}%")
    print(f"Percentage of Documentary Movies During Non-War Period (1920-1938): {non_war_documentary_percentage:.2f}%")


def action_movies_timeline(movies_df):
    #Used the same code as before but now for Action movies
    action_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Action' in x if isinstance(x, list) else False)]

    action_movie_count_by_year = action_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    action_percentage_by_year = (action_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies')
    ax1.plot(action_movie_count_by_year.index, action_movie_count_by_year.values, color='#f8c03f', label='Action Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Action Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(action_percentage_by_year.index, action_percentage_by_year.values, color='#1ecbe1', label='% Action Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Action Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Action Movies, and Percentage of Action Movies Released by Year')
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def action_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    action_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Action' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_action_movies = len(action_movies_df)

    total_action_percentage = (total_action_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_action_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'Action' in x if isinstance(x, list) else False)]
    ww2_action_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'Action' in x if isinstance(x, list) else False)]
    non_war_action_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'Action' in x if isinstance(x, list) else False)]

    ww1_action_percentage = (len(ww1_action_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_action_percentage = (len(ww2_action_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_action_percentage = (len(non_war_action_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of Action Movies in the Entire Dataset: {total_action_percentage:.2f}%")
    print(f"Percentage of Action Movies During WW1 (1914-1918): {ww1_action_percentage:.2f}%")
    print(f"Percentage of Action Movies During WW2 (1939-1945): {ww2_action_percentage:.2f}%")
    print(f"Percentage of Action Movies During Non-War Period (1920-1938): {non_war_action_percentage:.2f}%")


def adventure_movies_timeline(movies_df):
    #Used the same code as before but now for Adventure movies
    adventure_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Adventure' in x if isinstance(x, list) else False)]
    adventure_movie_count_by_year = adventure_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    adventure_percentage_by_year = (adventure_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies')
    ax1.plot(adventure_movie_count_by_year.index, adventure_movie_count_by_year.values, color='#f8c03f', label='Adventure Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Adventure Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(adventure_percentage_by_year.index, adventure_percentage_by_year.values, color='#1ecbe1', label='% Adventure Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Adventure Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Adventure Movies, and Percentage of Adventure Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')


    plt.tight_layout()
    plt.show()


def adventure_movies_info(movies_df):
    #Now we get the number for the percentage printed out
    adventure_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Adventure' in x if isinstance(x, list) else False)]

    total_movies = len(movies_df)

    total_adventure_movies = len(adventure_movies_df)

    total_adventure_percentage = (total_adventure_movies / total_movies) * 100

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_adventure_movies_df = ww1_movies_df[ww1_movies_df['genres'].apply(lambda x: 'Adventure' in x if isinstance(x, list) else False)]
    ww2_adventure_movies_df = ww2_movies_df[ww2_movies_df['genres'].apply(lambda x: 'Adventure' in x if isinstance(x, list) else False)]
    non_war_adventure_movies_df = non_war_movies_df[non_war_movies_df['genres'].apply(lambda x: 'Adventure' in x if isinstance(x, list) else False)]

    ww1_adventure_percentage = (len(ww1_adventure_movies_df) / len(ww1_movies_df)) * 100 if len(ww1_movies_df) > 0 else 0
    ww2_adventure_percentage = (len(ww2_adventure_movies_df) / len(ww2_movies_df)) * 100 if len(ww2_movies_df) > 0 else 0
    non_war_adventure_percentage = (len(non_war_adventure_movies_df) / len(non_war_movies_df)) * 100 if len(non_war_movies_df) > 0 else 0

    print(f"Percentage of Adventure Movies in the Entire Dataset: {total_adventure_percentage:.2f}%")
    print(f"Percentage of Adventure Movies During WW1 (1914-1918): {ww1_adventure_percentage:.2f}%")
    print(f"Percentage of Adventure Movies During WW2 (1939-1945): {ww2_adventure_percentage:.2f}%")
    print(f"Percentage of Adventure Movies During Non-War Period (1920-1938): {non_war_adventure_percentage:.2f}%")


def us_movies_war(movies_df):
    # For this analyisis the extra step is obtaining only movies from the US
    us_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United States of America' in x if isinstance(x, list) else False)]

    war_movies_us_df = us_movies_df[us_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_us_df.groupby('release_year').size()
    total_movies_by_year = us_movies_df.groupby('release_year').size()
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total US Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='#f8c03f', label='US War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='#1ecbe1', label='% US War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total US Movies, US War Movies, and Percentage of US War Movies Released by Year')

    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def uk_movies_war(movies_df):
    # Similar to the previous plot but replacing the US for the UK
    uk_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United Kingdom' in x if isinstance(x, list) else False)]

    war_movies_uk_df = uk_movies_df[uk_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_uk_df.groupby('release_year').size()
    total_movies_by_year = uk_movies_df.groupby('release_year').size()
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total UK Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='#f8c03f', label='UK War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='#1ecbe1', label='% UK War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total UK Movies, UK War Movies, and Percentage of UK War Movies Released by Year')

    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def germany_movies_war(movies_df):
    # Almost the same process than with the US and the UK but because Germany had different names during the war we asked chatGPT to give us the different names for Germany
    germany_related = ['Germany', 'German Democratic Republic', 'West Germany', 'Nazi Germany']

    germany_movies_df = movies_df[movies_df['countries'].apply(lambda x: any(country in germany_related for country in x) if isinstance(x, list) else False)]
    war_movies_germany_df = germany_movies_df[germany_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_germany_df.groupby('release_year').size()
    total_movies_by_year = germany_movies_df.groupby('release_year').size()
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Germany-related Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='#f8c03f', label='Germany-related War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='#1ecbe1', label='% Germany-related War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Germany-related Movies, Germany-related War Movies, and Percentage of Germany-related War Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def indian_movies_war(movies_df):
    india_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'India' in x if isinstance(x, list) else False)]

    war_movies_india_df = india_movies_df[india_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]

    war_movie_count_by_year = war_movies_india_df.groupby('release_year').size()

    total_movies_by_year = india_movies_df.groupby('release_year').size()

    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total India Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='#f8c03f', label='India War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='#1ecbe1', label='% India War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1914, 1918, color='#bdbdbd', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='#bdbdbd', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total India Movies, India War Movies, and Percentage of India War Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def science_fiction_movie(movies_df):
    # This code is very similar to previous ones but with the difference of changing the period for our plot and highlighting the space race instead
    movies_df['genres'] = movies_df['genres'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    sci_fi_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Science Fiction' in x if isinstance(x, list) else False)]

    sci_fi_movie_count_by_year = sci_fi_movies_df.groupby('release_year').size()

    total_movies_by_year = movies_df.groupby('release_year').size()

    sci_fi_percentage_by_year = (sci_fi_movie_count_by_year / total_movies_by_year) * 100

    start_year, end_year = 1930, 1980
    sci_fi_movie_count_by_year = sci_fi_movie_count_by_year[(sci_fi_movie_count_by_year.index >= start_year) & (sci_fi_movie_count_by_year.index <= end_year)]
    total_movies_by_year = total_movies_by_year[(total_movies_by_year.index >= start_year) & (total_movies_by_year.index <= end_year)]
    sci_fi_percentage_by_year = sci_fi_percentage_by_year[(sci_fi_percentage_by_year.index >= start_year) & (sci_fi_percentage_by_year.index <= end_year)]

    fig, ax1 = plt.subplots(figsize=(12, 4))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total Movies')
    ax1.plot(sci_fi_movie_count_by_year.index, sci_fi_movie_count_by_year.values, color='#f8c03f', label='Science Fiction Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Sci-Fi Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='#1ecbe1', label='% Sci-Fi Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Sci-Fi Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1957, 1975, color='#bdbdbd', alpha=0.3, label="Space Race Period (1957-1975)")

    plt.title('Total Movies, Science Fiction Movies, and Percentage of Sci-Fi Movies Released by Year (1940-1990)')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def us_scinece_fiction(movies_df):
    # Now we get the US movies only
    movies_df['genres'] = movies_df['genres'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    us_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United States of America' in x if isinstance(x, list) else False)]
    sci_fi_movies_us_df = us_movies_df[us_movies_df['genres'].apply(lambda x: 'Science Fiction' in x if isinstance(x, list) else False)]
    sci_fi_movie_count_by_year = sci_fi_movies_us_df.groupby('release_year').size()
    total_movies_by_year = us_movies_df.groupby('release_year').size()
    sci_fi_percentage_by_year = (sci_fi_movie_count_by_year / total_movies_by_year) * 100

    start_year, end_year = 1930, 1980
    sci_fi_movie_count_by_year = sci_fi_movie_count_by_year[(sci_fi_movie_count_by_year.index >= start_year) & (sci_fi_movie_count_by_year.index <= end_year)]
    total_movies_by_year = total_movies_by_year[(total_movies_by_year.index >= start_year) & (total_movies_by_year.index <= end_year)]
    sci_fi_percentage_by_year = sci_fi_percentage_by_year[(sci_fi_percentage_by_year.index >= start_year) & (sci_fi_percentage_by_year.index <= end_year)]

    fig, ax1 = plt.subplots(figsize=(12, 4))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='#f0390f', label='Total US Movies')
    ax1.plot(sci_fi_movie_count_by_year.index, sci_fi_movie_count_by_year.values, color='#f8c03f', label='US Science Fiction Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Sci-Fi Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='#1ecbe1', label='% Sci-Fi Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Sci-Fi Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(1957, 1975, color='#bdbdbd', alpha=0.3, label="Space Race Period (1957-1975)")

    plt.title('Total US Movies, Science Fiction Movies, and Percentage of Sci-Fi Movies Released by Year (1940-1990)')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def soviet_union_movies_1930_1980(movies_df):
    # Similar to what we did with Germany, we asked chatGPT for the names of the SSR or countries that belonged to it
    soviet_countries = [
        'Soviet Union', 'Russia', 'Ukraine', 'Uzbekistan', 'Georgia', 'Armenia',
        'Azerbaijan', 'Kazakhstan', 'Belarus', 'Moldova', 'Lithuania', 'Latvia',
        'Estonia', 'Turkmenistan', 'Kyrgyzstan', 'Tajikistan', 'Turkish SSR',
        'Uzbek SSR', 'German Democratic Republic', 'Czechoslovakia', 'Poland'
    ]


    soviet_movies_df = movies_df[movies_df['countries'].apply(lambda x: any(country in soviet_countries for country in x) if isinstance(x, list) else False)]
    movie_count_by_year = soviet_movies_df.groupby('release_year').size()

    start_year, end_year = 1930, 1980
    movie_count_by_year = movie_count_by_year[(movie_count_by_year.index >= start_year) & (movie_count_by_year.index <= end_year)]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(movie_count_by_year.index, movie_count_by_year.values, color='blue', label='Total Movies')

    ax.set_title('Total Movies Released by Year (1930-1980) from Soviet Union and Affiliates')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Number of Movies')

    ax.grid(True)

    ax.legend(loc='upper left')

    plt.tight_layout()
    plt.show()


def documentary_movies_1980_2015(movies_df):
    #Now we gather documentary movies
    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_movie_count_by_year = documentary_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    documentary_movie_count_by_year = documentary_movie_count_by_year[(documentary_movie_count_by_year.index >= 1980) & (documentary_movie_count_by_year.index <= 2015)]
    total_movies_by_year = total_movies_by_year[(total_movies_by_year.index >= 1980) & (total_movies_by_year.index <= 2015)]
    documentary_percentage_by_year = (documentary_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='#f0390f', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='#f8c03f', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='#1ecbe1', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(2001, 2001, color='red', alpha=0.3, label="9/11 Period (2001)", linewidth=8)  # Thicker line for 9/11

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (1980-2015)')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def documentary_movies_1980_2015_us(movies_df):
    # Similar process but again obtaining movies only from the US
    usa_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United States of America' in x if isinstance(x, list) else False)]
    documentary_movies_usa_df = usa_movies_df[usa_movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_movie_count_by_year = documentary_movies_usa_df.groupby('release_year').size()
    total_movies_by_year = usa_movies_df.groupby('release_year').size()
    documentary_movie_count_by_year = documentary_movie_count_by_year[(documentary_movie_count_by_year.index >= 1980) & (documentary_movie_count_by_year.index <= 2015)]
    total_movies_by_year = total_movies_by_year[(total_movies_by_year.index >= 1980) & (total_movies_by_year.index <= 2015)]
    documentary_percentage_by_year = (documentary_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='#f0390f', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='#f8c03f', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='#f0390f')
    ax1.tick_params(axis='y', labelcolor='#f0390f')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='#1ecbe1', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='#1ecbe1')
    ax2.tick_params(axis='y', labelcolor='#1ecbe1')

    ax1.axvspan(2001, 2001, color='red', alpha=0.3, label="9/11 Period (2001)", linewidth=8)  # Thicker line for 9/11

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (1980-2015) from United States')

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


def ww2_correlation(movies_df):
    # Obtaining correlation:

    # First we get all the war movies and group them by year
    war_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    # Then we obtained the percentage
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    # Then we create an indicator to see if movie occurs during WW2 1 for movies that occured and if not the value is 0
    start_year, end_year = 1939, 1945
    movies_df['WWII Indicator'] = movies_df['release_year'].apply(lambda x: 1 if start_year <= x <= end_year else 0)
    wwii_indicator_by_year = movies_df.groupby('release_year')['WWII Indicator'].max()

    #Finaly we calculate the correlation between the percentage of war movies and the years of war
    correlation = war_percentage_by_year.corr(wwii_indicator_by_year)

    print("Correlation between WWII period and percentage of war movies produced:", correlation)


def ww1_correlation_us(movies_df):
    # First we get all the war movies from the US and group them by year
    us_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United States of America' in x if isinstance(x, list) else False)]
    war_movies_us_df = us_movies_df[us_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year_us = war_movies_us_df.groupby('release_year').size()
    total_movies_by_year_us = us_movies_df.groupby('release_year').size()

    # Then we obtained the percentage
    war_percentage_by_year_us = (war_movie_count_by_year_us / total_movies_by_year_us) * 100

    # Then we create an indicator to see if movie occurs during WW2 1 for movies that occured and if not the value is 0
    start_year, end_year = 1939, 1945
    us_movies_df.loc[:, 'WWII Indicator'] = us_movies_df['release_year'].apply(lambda x: 1 if start_year <= x <= end_year else 0)
    wwii_indicator_by_year_us = us_movies_df.groupby('release_year')['WWII Indicator'].max()

    #Finaly we calculate the correlation between the percentage of war movies and the years of war from the US
    correlation_us = war_percentage_by_year_us.corr(wwii_indicator_by_year_us)

    print("Correlation between WWII period and percentage of War movies produced in the United States:", correlation_us)


def ww2_correlation_uk(movies_df):
        # First we get all the war movies from the UK and group them by year
    uk_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'United Kingdom' in x if isinstance(x, list) else False)]
    war_movies_uk_df = uk_movies_df[uk_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year_uk = war_movies_uk_df.groupby('release_year').size()
    total_movies_by_year_uk = uk_movies_df.groupby('release_year').size()

    # Then we obtained the percentage
    war_percentage_by_year_uk = (war_movie_count_by_year_uk / total_movies_by_year_uk) * 100

    # Then we create an indicator to see if movie occurs during WW2 1 for movies that occured and if not the value is 0
    start_year, end_year = 1939, 1945
    uk_movies_df.loc[:, 'WWII Indicator'] = uk_movies_df['release_year'].apply(lambda x: 1 if start_year <= x <= end_year else 0)
    wwii_indicator_by_year_us = uk_movies_df.groupby('release_year')['WWII Indicator'].max()

    #Finaly we calculate the correlation between the percentage of war movies and the years of war from the UK
    correlation_us = war_percentage_by_year_uk.corr(wwii_indicator_by_year_us)

    print("Correlation between WWII period and percentage of War movies produced in the United Kigdom:", correlation_us)


def ww2_correlation_mystery(movies_df):
    # First we get all the mystery movies and group them by year
    mystery_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Mystery' in x if isinstance(x, list) else False)]
    mystery_movie_count_by_year = mystery_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    # Then we obtained the percentage
    mystery_percentage_by_year = (mystery_movie_count_by_year / total_movies_by_year) * 100

    # Then we create an indicator to see if movie occurs during WW2 1 for movies that occured and if not the value is 0
    start_year, end_year = 1932, 1948
    movies_df['WWII Indicator'] = movies_df['release_year'].apply(lambda x: 1 if start_year <= x <= end_year else 0)
    wwii_indicator_by_year = movies_df.groupby('release_year')['WWII Indicator'].max()

    correlation = mystery_percentage_by_year.corr(wwii_indicator_by_year)

    print("Correlation between WWII period and percentage of Mystery movies produced:", correlation)


def ww2_correlation_documentary(movies_df):
    # First we get all the Documentary movies and group them by year
    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_movies_1910_1960_df = documentary_movies_df[(documentary_movies_df['release_year'] >= 1910) & (documentary_movies_df['release_year'] <= 1960)]
    documentary_movie_count_by_year = documentary_movies_1910_1960_df.groupby('release_year').size()
    total_movies_by_year_1910_1960 = movies_df[(movies_df['release_year'] >= 1910) & (movies_df['release_year'] <= 1960)].groupby('release_year').size()

    # Then we obtained the percentage
    documentary_percentage_by_year = (documentary_movie_count_by_year / total_movies_by_year_1910_1960) * 100

    # Then we create an indicator to see if movie occurs during WW2 1 for movies that occured and if not the value is 0
    start_year, end_year = 1939, 1945
    movies_df['WWII Indicator'] = movies_df['release_year'].apply(lambda x: 1 if start_year <= x <= end_year else 0)
    wwii_indicator_by_year = movies_df[(movies_df['release_year'] >= 1910) & (movies_df['release_year'] <= 1960)].groupby('release_year')['WWII Indicator'].max()

    correlation = documentary_percentage_by_year.corr(wwii_indicator_by_year)

    print("Correlation between WWII period and percentage of Documentary movies produced (1910-1960):", correlation)


def sci_fi_1943_1959(movies_df):
    # First we get the science fiction movies, count them and obtain the percentage
    sci_fi_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Science Fiction' in x if isinstance(x, list) else False)]
    sci_fi_count_by_year = sci_fi_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    sci_fi_percentage_by_year = ((sci_fi_count_by_year / total_movies_by_year) * 100).dropna()


    #Then we adjust the period to focus our function
    pre_space_race_years = range(1943, 1959)
    sci_fi_percentage_pre_space_race = sci_fi_percentage_by_year[sci_fi_percentage_by_year.index.isin(pre_space_race_years)]

    # Next we get our X and Y values
    years = np.array(sci_fi_percentage_pre_space_race.index).reshape(-1, 1)
    percentages = sci_fi_percentage_pre_space_race.values

    # We apply regresion using function from sklearn
    model = LinearRegression()
    model.fit(years, percentages)
    trendline = model.predict(years)

    plt.figure(figsize=(10, 6))
    plt.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='gray', label='Percentage of Sci-Fi Movies (All Years)')
    plt.plot(sci_fi_percentage_pre_space_race.index, sci_fi_percentage_pre_space_race.values, color='blue', label='Sci-Fi Movies % from 1943 to 1959')
    plt.plot(sci_fi_percentage_pre_space_race.index, trendline, color='red', linestyle='--', label='Trendline (1943-1959)')

    plt.axvspan(1957, 1975, color='#bdbdbd', alpha=0.3, label="Space Race Period (1957-1975)")

    plt.ylim(0, 20)

    plt.xlabel('Year')
    plt.ylabel('Percentage of Sci-Fi Movies')
    plt.title('Trend in Sci-Fi Movies from 1943 to 1959')
    plt.legend()
    plt.grid(True)
    plt.show()

    #Finaly we display the slope value
    print("Slope from 1943 to 1959:", model.coef_[0])


def sci_fi_1937_1975(movies_df):
    # First we get the science fiction movies, count them and obtain the percentage
    sci_fi_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Science Fiction' in x if isinstance(x, list) else False)]
    sci_fi_count_by_year = sci_fi_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    sci_fi_percentage_by_year = (sci_fi_count_by_year / total_movies_by_year * 100).dropna()

    #Then we adjust the period to focus our function
    pre_space_race_years = range(1947, 1982)
    sci_fi_percentage_pre_space_race = sci_fi_percentage_by_year[sci_fi_percentage_by_year.index.isin(pre_space_race_years)]

    sci_fi_percentage_pre_space_race = sci_fi_percentage_pre_space_race.reindex(pre_space_race_years, fill_value=0)

    # Later we adjust our data for our function
    years = np.array(sci_fi_percentage_pre_space_race.index)
    percentages = sci_fi_percentage_pre_space_race.values

    # We apply a 3rd degree polynomial function
    degree = 3
    poly_model = Polynomial.fit(years, percentages, degree)

    trendline = poly_model(years)

    plt.figure(figsize=(10, 6))
    plt.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='gray', label='Percentage of Sci-Fi Movies (All Years)')
    plt.plot(sci_fi_percentage_pre_space_race.index, sci_fi_percentage_pre_space_race.values, color='blue', label='Sci-Fi Movies % from 1947 to 1982')
    plt.plot(sci_fi_percentage_pre_space_race.index, trendline, color='red', linestyle='--', label=f'Polynomial Trendline (Degree {degree})')

    plt.axvspan(1957, 1975, color='#bdbdbd', alpha=0.3, label="Space Race Period (1947-1982)")

    plt.ylim(0, 20)

    plt.xlabel('Year')
    plt.ylabel('Percentage of Sci-Fi Movies')
    plt.title('Trend in Sci-Fi Movies from 1937 to 1975')
    plt.legend()
    plt.grid(True)
    plt.show()


    # Finaly we display the function
    coefficients = poly_model.convert().coef
    poly_function_str = "f(x) = " + " + ".join(f"{coef:.3f}*x^{i}" if i > 0 else f"{coef:.3f}" for i, coef in enumerate(coefficients))
    print("Polynomial Function:", poly_function_str)


def documentary_1991_2006_linear(movies_df):
    # First we get the documentary movies, count them and obtain the percentage
    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_count_by_year = documentary_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    documentary_percentage_by_year = ((documentary_count_by_year / total_movies_by_year) * 100).dropna()

    #Then we adjust the period to focus our function
    pre_post_911_years = range(1990, 2009)
    documentary_percentage_pre_post_911 = documentary_percentage_by_year[documentary_percentage_by_year.index.isin(pre_post_911_years)]

    # Next we get our X and Y values
    years = np.array(documentary_percentage_pre_post_911.index).reshape(-1, 1)
    percentages = documentary_percentage_pre_post_911.values

    # We apply regresion using function from sklearn
    model = LinearRegression()
    model.fit(years, percentages)
    trendline = model.predict(years)

    plt.figure(figsize=(10, 6))
    plt.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='gray', label='Percentage of Documentary Movies (All Years)')
    plt.plot(documentary_percentage_pre_post_911.index, documentary_percentage_pre_post_911.values, color='blue', label='Documentary Movies % from 1990 to 2009')
    plt.plot(documentary_percentage_pre_post_911.index, trendline, color='red', linestyle='--', label='Trendline (1990-2009)')

    plt.axvline(x=2001, color='#bdbdbd', alpha=0.5, linestyle='-', linewidth=6, label="9/11 (2001)")

    plt.ylim(0, 20)

    plt.xlabel('Year')
    plt.ylabel('Percentage of Documentary Movies')
    plt.title('Trend in Documentary Movies from 1991 to 2006')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Display the slope value
    print("Slope from 1990 to 2009:", model.coef_[0])


def documentary_1991_2006_polynomial(movies_df):
    # First we get the documentary movies, count them and obtain the percentage
    documentary_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Documentary' in x if isinstance(x, list) else False)]
    documentary_count_by_year = documentary_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    documentary_percentage_by_year = (documentary_count_by_year / total_movies_by_year * 100).dropna()

    #Then we adjust the period to focus our function
    pre_post_911_years = range(1990, 2009)
    documentary_percentage_pre_post_911 = documentary_percentage_by_year[documentary_percentage_by_year.index.isin(pre_post_911_years)]

    documentary_percentage_pre_post_911 = documentary_percentage_pre_post_911.reindex(pre_post_911_years, fill_value=0)

    # Later we adjust our data for our function
    years = np.array(documentary_percentage_pre_post_911.index)
    percentages = documentary_percentage_pre_post_911.values

    # We apply a 2nd degree polynomial function (we used second because 3rd displayed the same plot)
    degree = 2
    poly_model = Polynomial.fit(years, percentages, degree)

    trendline = poly_model(years)

    plt.figure(figsize=(10, 6))
    plt.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='gray', label='Percentage of Documentary Movies (All Years)')
    plt.plot(documentary_percentage_pre_post_911.index, documentary_percentage_pre_post_911.values, color='blue', label='Documentary Movies % from 1991 to 2006')
    plt.plot(documentary_percentage_pre_post_911.index, trendline, color='red', linestyle='--', label=f'Polynomial Trendline (Degree {degree})')

    plt.axvline(x=2001, color='#bdbdbd', alpha=0.5, linestyle='-', linewidth=6, label="9/11 (2001)")

    plt.ylim(0, 20)

    plt.xlabel('Year')
    plt.ylabel('Percentage of Documentary Movies')
    plt.title('Trend in Documentary Movies from 1991 to 2006')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Finaly we display the function
    coefficients = poly_model.convert().coef
    poly_function_str = "f(x) = " + " + ".join(f"{coef:.3f}*x^{i}" if i > 0 else f"{coef:.3f}" for i, coef in enumerate(coefficients))
    print("Polynomial Function:", poly_function_str)

