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


def load_data_sentiment_analysis():
    #Loaad again the data
    plot_summary_df = pd.read_csv("data/plot_summaries.txt", delimiter='\t', names=["wikipedia_id", "plot_summary"])
    movies_df = pd.read_csv("data/movies_dataset.tsv", delimiter='\t')
    merged_df = pd.merge(plot_summary_df, movies_df, on="wikipedia_id", how="inner")
    return merged_df

def preprocess_data_sentiment_analysis(df):
    merged_df = df.copy()
    merged_df['release_date'] = pd.to_datetime(merged_df['release_date'], errors='coerce')
    merged_df = merged_df.dropna(subset=['release_date'])
    merged_df['year'] = merged_df['release_date'].dt.year

    return merged_df