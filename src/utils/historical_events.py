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