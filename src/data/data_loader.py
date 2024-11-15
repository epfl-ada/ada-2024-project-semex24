import pandas as pd

def data_loader_movies(file_path):
    movies_df =  pd.read_csv(file_path, sep='\t')
    return movies_df
