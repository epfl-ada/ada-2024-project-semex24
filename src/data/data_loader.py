import pandas as pd
import ast

def data_loader_movies():
    file_path = 'data/movies_dataset.tsv'
    movies_df =  pd.read_csv(file_path, sep='\t')
    return movies_df


def parse_genres(x):
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except (ValueError, SyntaxError):
            return [genre.strip() for genre in x.split(',')]
    return x


def feature_engineering_movies(df):
    movies_df = df.copy()
    movies_df['release_date'] = pd.to_datetime(movies_df['release_date'], errors='coerce')
    movies_df['release_year'] = movies_df['release_date'].dt.year
    movie_count_by_year = movies_df['release_year'].value_counts().sort_index()
    movies_df['genres'] = movies_df['genres'].apply(parse_genres)

    # Converting to lists genre column, country and language column
    movies_df['countries'] = movies_df['countries'].str.split(', ')
    movies_df['languages'] = movies_df['languages'].str.split(', ')
    movies_df = movies_df.dropna(subset=['release_year'])

    return movies_df
