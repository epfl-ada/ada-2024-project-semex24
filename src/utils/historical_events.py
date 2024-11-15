import pandas as pd
import matplotlib.pyplot as plt

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
    genre_comparison_df.plot(kind='bar', figsize=(14, 7))
    plt.title("Comparison of genres During WW1, Non-War Period, and WW2")
    plt.xlabel("Genres")
    plt.ylabel("Frequency of Movies")
    plt.legend(["WW1", "Non-War (1920-1938)", "WW2"])
    plt.show()



def percentage_genres_war_periods(movies_df):
    # Now we repeated the steps from above but, obtained the percentages of each genre and plotted them

    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]

    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    non_war_genre_counts = non_war_movies_df['genres'].explode().value_counts()

    # We calculated the percentages by dividung all the counts by the sum of each genre
    ww1_genre_percentages = (ww1_genre_counts / ww1_genre_counts.sum()) * 100
    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    non_war_genre_percentages = (non_war_genre_counts / non_war_genre_counts.sum()) * 100

    genre_comparison_df = pd.DataFrame({
        'WW1': ww1_genre_percentages,
        'Non-War': non_war_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    genre_comparison_df.plot(kind='bar', figsize=(14, 7))
    plt.title("Percentage of genres During WW1, Non-War Period, and WW2")
    plt.xlabel("Genres")
    plt.ylabel("Percentage of Movies")
    plt.legend(["WW1", "Non-War (1920-1938)", "WW2"])
    plt.show()


def percentage_genres_war_periods_all_movies(movies_df):
    #We repeated the process from above with the difference of getting all the movies instead of only movies from 1920-138

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

    genre_comparison_percent_df.plot(kind='bar', figsize=(14, 7))
    plt.title("Percentage of genres During WW1, All Movies, and WW2")
    plt.xlabel("Genres")
    plt.ylabel("Percentage of Movies")
    plt.legend(["WW1", "All Movies", "WW2"])
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

    plt.title("Percentage of genres Over Time (Respect to All Movies)")
    plt.xlabel("Year")
    plt.ylabel("Percentage of Movies")
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.tight_layout()

    plt.show()


def number_movies(movies_df):
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    plt.figure(figsize=(10, 5))
    plt.plot(movie_count_by_year.index, movie_count_by_year.values, marker='o')
    plt.xlabel('Year of release')
    plt.ylabel('Number of movies')
    plt.title('Number of movies released by year')
    plt.grid(True)
    plt.show()


def number_movies_1900_1925(movies_df):
    # We created a dataframe only for movies between 1900-1925 and repeated the steps from above
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    filtered_movie_count = movie_count_by_year[(movie_count_by_year.index >= 1900) & (movie_count_by_year.index <= 1950)]

    plt.figure(figsize=(10, 5))
    plt.plot(filtered_movie_count.index, filtered_movie_count.values, marker='o')
    plt.xlabel('Year of release')
    plt.ylabel('Number of movies')
    plt.title('Number of movies released by year (1900-1925)')
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
    ww1_movies_df = movies_df[(movies_df['release_year'] >= 1914) & (movies_df['release_year'] <= 1918)]
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    all_movies_df = movies_df
    # Used the same code as before but removed the part for WW1
    ww2_movies_df = movies_df[(movies_df['release_year'] >= 1939) & (movies_df['release_year'] <= 1945)]
    non_war_movies_df = movies_df[(movies_df['release_year'] >= 1920) & (movies_df['release_year'] <= 1938)]
    all_movies_df = movies_df  # All movies in the dataset

    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()
    non_war_genre_counts = non_war_movies_df['genres'].explode().value_counts()

    genre_comparison_df = pd.DataFrame({
        'Non-War': non_war_genre_counts,
        'WW2': ww2_genre_counts
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_df.plot(kind='bar')
    plt.title("Comparison of genres during WW2 and Non-War Period")
    plt.xlabel("Genres")
    plt.ylabel("Frequency of Movies")
    plt.legend(["Non-War (1920-1938)", "WW2"])
    plt.tight_layout()
    plt.show()

    ww1_genre_counts = ww1_movies_df['genres'].explode().value_counts()
    ww2_genre_counts = ww2_movies_df['genres'].explode().value_counts()

    ww1_genre_percentages = (ww1_genre_counts / ww1_genre_counts.sum()) * 100
    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    non_war_genre_percentages = (non_war_genre_counts / non_war_genre_counts.sum()) * 100

    genre_comparison_percent_df = pd.DataFrame({
        'Non-War': non_war_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_percent_df.plot(kind='bar')
    plt.title("Percentage of genres during WW2 and Non-War Period")
    plt.xlabel("Genres")
    plt.ylabel("Percentage of Movies")
    plt.legend(["Non-War (1920-1938)", "WW2"])
    plt.tight_layout()
    plt.show()

    all_genre_counts = all_movies_df['genres'].explode().value_counts()

    ww2_genre_percentages = (ww2_genre_counts / ww2_genre_counts.sum()) * 100
    all_genre_percentages = (all_genre_counts / all_genre_counts.sum()) * 100

    genre_comparison_percent_all_df = pd.DataFrame({
        'All Movies': all_genre_percentages,
        'WW2': ww2_genre_percentages
    }).fillna(0)

    plt.figure(figsize=(14, 7))
    genre_comparison_percent_all_df.plot(kind='bar')
    plt.title("Percentage of genres of All Movies, and WW2 movies")
    plt.xlabel("Genres")
    plt.ylabel("Percentage of Movies")
    plt.legend(["All Movies", "WW2"])
    plt.tight_layout()
    plt.show()


def war_movies_timeline(movies_df):
    # First we get only the war movies and group them by year to get the total number of movies
    war_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]
    war_movie_count_by_year = war_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()

    # Then we calculate the percentage
    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='darkred', label='War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='green', label='% War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, War Movies, and Percentage of War Movies Released by Year')
    ax1.grid(True)
    ax1.legend(loc='upper left')

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
    #Used the same code as before but now for Crime movies
    crime_movies_df = movies_df[movies_df['genres'].apply(lambda x: 'Crime' in x if isinstance(x, list) else False)]

    crime_movie_count_by_year = crime_movies_df.groupby('release_year').size()
    total_movies_by_year = movies_df.groupby('release_year').size()
    crime_percentage_by_year = (crime_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(crime_movie_count_by_year.index, crime_movie_count_by_year.values, color='darkred', label='Crime Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Crime Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(crime_percentage_by_year.index, crime_percentage_by_year.values, color='green', label='% Crime Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Crime Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Crime Movies, and Percentage of Crime Movies Released by Year')
    ax1.grid(True)
    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(mystery_movie_count_by_year.index, mystery_movie_count_by_year.values, color='purple', label='Mystery Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Mystery Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(mystery_percentage_by_year.index, mystery_percentage_by_year.values, color='green', label='% Mystery Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Mystery Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Mystery Movies, and Percentage of Mystery Movies Released by Year')
    ax1.grid(True)
    ax1.legend(loc='upper left')

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
    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='blue', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='brown', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='green', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (Starting from 1900)')

    ax1.grid(True)
    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(action_movie_count_by_year.index, action_movie_count_by_year.values, color='darkred', label='Action Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Action Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(action_percentage_by_year.index, action_percentage_by_year.values, color='green', label='% Action Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Action Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Action Movies, and Percentage of Action Movies Released by Year')
    ax1.grid(True)
    ax1.legend(loc='upper left')

    plt.tight_layout()
    plt.show()


def action_movies_timeline(movies_df):
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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(adventure_movie_count_by_year.index, adventure_movie_count_by_year.values, color='darkred', label='Adventure Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Adventure Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(adventure_percentage_by_year.index, adventure_percentage_by_year.values, color='green', label='% Adventure Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Adventure Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Movies, Adventure Movies, and Percentage of Adventure Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')


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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total US Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='darkred', label='US War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='green', label='% US War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total US Movies, US War Movies, and Percentage of US War Movies Released by Year')

    ax1.grid(True)
    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total UK Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='darkred', label='UK War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='green', label='% UK War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total UK Movies, UK War Movies, and Percentage of UK War Movies Released by Year')

    ax1.grid(True)
    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Germany-related Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='darkred', label='Germany-related War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='green', label='% Germany-related War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total Germany-related Movies, Germany-related War Movies, and Percentage of Germany-related War Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')

    plt.tight_layout()
    plt.show()


def indian_movies_war(movies_df):
    india_movies_df = movies_df[movies_df['countries'].apply(lambda x: 'India' in x if isinstance(x, list) else False)]

    war_movies_india_df = india_movies_df[india_movies_df['genres'].apply(lambda x: 'War' in x if isinstance(x, list) else False)]

    war_movie_count_by_year = war_movies_india_df.groupby('release_year').size()

    total_movies_by_year = india_movies_df.groupby('release_year').size()

    war_percentage_by_year = (war_movie_count_by_year / total_movies_by_year) * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total India Movies')
    ax1.plot(war_movie_count_by_year.index, war_movie_count_by_year.values, color='darkred', label='India War Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / War Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(war_percentage_by_year.index, war_percentage_by_year.values, color='green', label='% India War Movies', linestyle='--')
    ax2.set_ylabel('Percentage of War Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1914, 1918, color='lightblue', alpha=0.3, label="WW1 Period (1914-1918)")
    ax1.axvspan(1939, 1945, color='lightblue', alpha=0.3, label="WW2 Period (1939-1945)")

    plt.title('Total India Movies, India War Movies, and Percentage of India War Movies Released by Year')

    ax1.grid(True)

    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total Movies')
    ax1.plot(sci_fi_movie_count_by_year.index, sci_fi_movie_count_by_year.values, color='darkred', label='Science Fiction Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Sci-Fi Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='green', label='% Sci-Fi Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Sci-Fi Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1957, 1975, color='lightblue', alpha=0.3, label="Space Race Period (1957-1975)")

    plt.title('Total Movies, Science Fiction Movies, and Percentage of Sci-Fi Movies Released by Year (1940-1990)')

    ax1.grid(True)

    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, total_movies_by_year.values, color='blue', label='Total US Movies')
    ax1.plot(sci_fi_movie_count_by_year.index, sci_fi_movie_count_by_year.values, color='darkred', label='US Science Fiction Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Number of Movies / Sci-Fi Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(sci_fi_percentage_by_year.index, sci_fi_percentage_by_year.values, color='green', label='% Sci-Fi Movies', linestyle='--')
    ax2.set_ylabel('Percentage of Sci-Fi Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(1957, 1975, color='lightblue', alpha=0.3, label="Space Race Period (1957-1975)")

    plt.title('Total US Movies, Science Fiction Movies, and Percentage of Sci-Fi Movies Released by Year (1940-1990)')

    ax1.grid(True)

    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='blue', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='brown', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='green', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(2001, 2001, color='red', alpha=0.3, label="9/11 Period (2001)", linewidth=8)  # Thicker line for 9/11

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (1980-2015)')

    ax1.grid(True)

    ax1.legend(loc='upper left')

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

    ax1.plot(total_movies_by_year.index, np.log1p(total_movies_by_year.values), color='blue', label='Log of Total Movies')
    ax1.plot(documentary_movie_count_by_year.index, np.log1p(documentary_movie_count_by_year.values), color='brown', label='Log of Documentary Movies')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Log of Total Number of Movies / Log of Documentary Movies', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(documentary_percentage_by_year.index, documentary_percentage_by_year.values, color='green', label=f'Scaled % Documentary Movies', linestyle='--')
    ax2.set_ylabel('Scaled Percentage of Documentary Movies', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    ax1.axvspan(2001, 2001, color='red', alpha=0.3, label="9/11 Period (2001)", linewidth=8)  # Thicker line for 9/11

    plt.title('Total Movies, Documentary Movies (Log Scale), and Scaled Percentage of Documentary Movies Released by Year (1980-2015) from United States')

    ax1.grid(True)

    ax1.legend(loc='upper left')

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