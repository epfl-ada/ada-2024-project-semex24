import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re 
import statsmodels.formula.api as smf
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from statsmodels.formula.api import ols
import warnings
warnings.filterwarnings('ignore')
from scipy.stats import linregress
from scipy.stats import pearsonr

def is_month_year_only(date_str):
    month_year_pattern = r'\d{4}-\d{2}'
    return bool(re.match(month_year_pattern, str(date_str)))
    
def is_full_date(date_str):
    full_date_pattern = r'\d{4}-\d{2}-\d{2}'
    return bool(re.match(full_date_pattern, str(date_str)))

def getdf_filtered(movies_df):

    # dropna release_year
    df_filtered = movies_df.dropna(subset=['release_year'])
    df_filtered = df_filtered[df_filtered['release_year'] >= 1800]

    # percentile popularity
    percentile_95 = df_filtered['popularity'].quantile(0.95)
    df_filtered[df_filtered['popularity'] > percentile_95] = np.nan

    #percentile budget
    percentile_2 = df_filtered['budget'].quantile(0.02)
    df_filtered.loc[df_filtered['budget'] < percentile_2, 'budget'] = np.nan

    #percentile revenue
    percentile_01 = df_filtered['revenue'].quantile(0.001)
    df_filtered[df_filtered['revenue'] < percentile_01] = np.nan

    #percentile runtime
    percentile_01 = df_filtered['runtime'].quantile(0.01)
    df_filtered[df_filtered['runtime'] < percentile_01] = np.nan
    percentile_99 = df_filtered['runtime'].quantile(0.999)
    df_filtered[df_filtered['runtime'] > percentile_99] = np.nan

    
    return df_filtered

def date_pattern(df_movies):
    df_seasons = df_movies[df_movies['release_date'].apply(is_month_year_only)]
    print(f"Number of movies that have at least month and a year: {df_seasons.shape[0]}")
    print(f"Number of movies that have any date (but not NaN): {df_movies.shape[0]}")
    print(f"Number of movies that have day, month and a year: {df_seasons[df_seasons['release_date'].apply(is_full_date)].shape[0]}")
    return df_seasons

def find_season(date_str):
    if is_full_date(date_str) or is_month_year_only(date_str):
        month = date_str.month  #get just the month
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Autumn'
    return None

def seasonal_analysis(df_seasons):
    df_seasons.loc[:, 'season'] = df_seasons['release_date'].apply(find_season)
    df_summer = df_seasons[df_seasons['season']=='Summer']
    df_autumn = df_seasons[df_seasons['season']=='Autumn']
    df_winter = df_seasons[df_seasons['season']=='Winter']
    df_spring = df_seasons[df_seasons['season']=='Spring']

    # What is the number of movies in each dataset?
    print(f"Movies released in summer: {df_summer.shape[0]}")
    print(f"Movies released in autumn: {df_autumn.shape[0]}")
    print(f"Movies released in winter: {df_winter.shape[0]}")
    print(f"Movies released in spring: {df_spring.shape[0]}")

def plot_seasons(df_seasons):
    plt.figure(figsize=(10, 6))                                                                         #Summer       Autumn   Winter    Spring
    sns.countplot(x='season', data=df_seasons, order=['Summer', 'Autumn','Winter', 'Spring'], palette=['#f0390f', '#f8c03f', '#1ecbe1', '#0fa4a8'])
    plt.title('Number of released movies through seasons')
    plt.xlabel('Season')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

def plot_seasons_revenues(df_seasons):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="revenue", data=df_seasons, palette=['#f0390f', '#1ecbe1', '#0fa4a8', '#f8c03f'])
    plt.title('Revenues of movies through seasons')
    plt.xlabel('Season')
    plt.ylabel('revenue')
    plt.show()    

def plot_seasonal_revenue(df_seasons):
    seasonal_revenue = df_seasons.groupby(['release_year', 'season'])['revenue'].mean().unstack()
    seasonal_revenue.plot(figsize=(10, 6), marker='o', color=['#f8c03f', '#0fa4a8', '#f0390f', '#1ecbe1'])
    plt.title('Average revenue per Season Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average revenue')
    plt.show()

def plot_seasons_budgets(df_seasons):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="budget", data=df_seasons, palette=['#f0390f', '#1ecbe1', '#0fa4a8', '#f8c03f'])
    plt.title('budgets of movies through seasons')
    plt.xlabel('Season')
    plt.ylabel('budget')
    plt.show()   

def plot_seasons_runtime(df_seasons):
    plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="runtime", data=df_seasons, palette=['#f0390f', '#1ecbe1', '#0fa4a8', '#f8c03f'])
    plt.title('Runtime of movies through seasons')
    plt.xlabel('Season')
    plt.ylabel('Runtime')
    plt.show()    

def plot_seasons_popularity(df_seasons): 
    plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="popularity", data=df_seasons, palette=['#f0390f', '#1ecbe1', '#0fa4a8', '#f8c03f'])
    plt.title('Popularity score of movies through seasons')
    plt.xlabel('Season')
    plt.ylabel('popularity score')
    plt.show()    


def plot_genre_distribution(df_seasons):
    df_seasons_exploded = df_seasons.explode('genres')
    plt.figure(figsize=(12, 8))
    sns.countplot(x='season', hue='genres', data=df_seasons_exploded, order=['Summer', 'Autumn', 'Winter', 'Spring'], palette='Spectral')
    plt.title('Genre Distribution Across Seasons')
    plt.xlabel('Season')
    plt.ylabel('Number of Movies')
    plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

def plot_genre_season_heatmap(df_seasons):
    df_seasons_exploded = df_seasons.explode('genres')
    genre_season_pivot = df_seasons_exploded.pivot_table(index='genres', columns='season', aggfunc='size', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(genre_season_pivot, annot=True, cmap='Spectral', fmt="d")
    plt.title('Frequency of genres by Season')
    plt.xlabel('Season')
    plt.ylabel('Genre')
    plt.show()    

def plot_top_genres_per_season(df_seasons):
    df_seasons_exploded = df_seasons.explode('genres')
    genre_counts = df_seasons_exploded.groupby(['season', 'genres']).size().reset_index(name='count')
    top_genres_per_season = genre_counts.sort_values(['season', 'count'], ascending=[True, False])
    top_genres_per_season = top_genres_per_season.groupby('season').head(10)

    plt.figure(figsize=(15, 6))
    sns.barplot(data=top_genres_per_season, x='season', y='count', hue='genres', order=['Summer', 'Autumn', 'Winter', 'Spring'], palette='Spectral')
    plt.title('Top 10 Genres by Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Movies')
    plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

def seasonal_regression_revenue(df_seasons):
    df_seasons['season'] = df_seasons['season'].astype('category')
    model_season_revenue = smf.ols(formula='revenue ~ C(season)', data=df_seasons)
    results_season_revenue = model_season_revenue.fit()
    print(results_season_revenue.summary())

def seasonal_regression_popularity(df_seasons):
    df_seasons['season'] = df_seasons['season'].astype('category')
    model_season_popularity = smf.ols(formula='popularity ~ C(season)', data=df_seasons)
    results_season_popularity = model_season_popularity.fit()
    print(results_season_popularity.summary())

def chi2_genre(df_seasons):
    df_exploded = df_seasons.explode('genres')
    df_genres = df_exploded['genres'].str.get_dummies() #converting to one hot encoded columns
    df_genres_grouped = df_genres.groupby(df_exploded.index).sum()
    df_seasons_added_genres = pd.concat([df_seasons, df_genres_grouped], axis=1)
    season_genre_counts = df_seasons_added_genres.groupby('season')[df_genres_grouped.columns].sum()
    chi2, p, dof, expected = chi2_contingency(season_genre_counts)
    print(f'Chi-Square Statistic: {chi2}, p-value: {p}')    

def genre_season_performance(df_seasons):
    genre_season_performance = df_seasons.explode('genres').groupby(['genres', 'season']).agg({
        'revenue': 'mean',
        'popularity': 'mean'
    }).reset_index()
    print(genre_season_performance.head())
    return genre_season_performance

def plot_genre_season_performance(genre_season_performance):
    revenue_pivot = genre_season_performance.pivot(index='genres', columns='season', values='revenue')
    popularity_pivot = genre_season_performance.pivot(index='genres', columns='season', values='popularity')

    plt.figure(figsize=(12, 6))
    sns.heatmap(revenue_pivot, annot=True, cmap="YlOrRd", fmt='.2f', cbar=True)
    plt.title('Average revenue by Genre and Season')
    plt.xlabel('Season')
    plt.ylabel('Genre')
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.heatmap(popularity_pivot, annot=True, cmap="YlOrRd", fmt='.2f', cbar=True)
    plt.title('Average popularity by Genre and Season')
    plt.xlabel('Season')
    plt.ylabel('Genre')
    plt.show()

def revenue_ttest(df_seasons):
    spring_revenue = df_seasons[(df_seasons['genres'].apply(lambda x: 'Fantasy' in x or 'Science Fiction' in x)) & (df_seasons['season'] == 'Spring')]['revenue']
    other_seasons_revenue = df_seasons[(df_seasons['genres'].apply(lambda x: 'Fantasy' in x or 'Science Fiction' in x)) & (df_seasons['season'] != 'Spring')]['revenue']
    t_stat, p_value = ttest_ind(spring_revenue.dropna(), other_seasons_revenue.dropna())
    print(f"T-statistic: {t_stat}, p-value: {p_value}")

def multiple_regression(df_seasons):
    # Exploding the genres column (so that each genre is a separate row)
    df_exploded = df_seasons.explode('genres')
    # Create a multiple linear regression model: revenue ~ season + genre + season:genre
    model = ols('revenue ~ C(season) + C(genres) + C(season):C(genres)', data=df_exploded).fit()
    # Print the summary to get the coefficients and p-values
    print(model.summary())

def holiday_analysys(df_filtered):
    df_month_year = df_filtered[df_filtered['release_date'].apply(is_month_year_only or is_full_date)]
    df_full_date = df_filtered[df_filtered['release_date'].apply(is_full_date)]

    # Extract month from release_date
    df_month_year['month'] = df_month_year['release_date'].dt.month
    df_month_year['year'] = df_month_year['release_date'].dt.year
    df_full_date['month'] = df_full_date['release_date'].dt.month
    df_full_date['year'] = df_full_date['release_date'].dt.year
    df_full_date['day'] = df_full_date['release_date'].dt.day

    # drop NaN values
    df_month_year = df_month_year.dropna(subset=['month', 'year'])
    df_full_date = df_full_date.dropna(subset=['month', 'year', 'day'])

    # Subset movies after 1950
    df_month_year = df_month_year[df_month_year['year'] >= 1950]
    df_full_date = df_full_date[df_full_date['year'] >= 1950]

    # Use English speaking movies only
    df_month_year = df_month_year[df_month_year['languages'].apply(lambda x: 'English Language' in x if isinstance(x, list) else False)]
    df_full_date = df_full_date[df_full_date['languages'].apply(lambda x: 'English Language' in x if isinstance(x, list) else False)]

    # Let's see the distribution of movies through months
    plt.figure(figsize=(10, 6))
    sns.countplot(x='month', data=df_month_year, palette=['#f0390f'])
    plt.title('Number of released movies through months')
    plt.xlabel('Month')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

    return df_month_year, df_full_date

def release_year_analysis(df_month_year):
    # show distribution of movies through years
    plt.figure(figsize=(10, 6))
    sns.countplot(x='year', data=df_month_year, palette=['#f0390f'])
    plt.title('Number of released movies through years')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.xticks( ticks=plt.gca().get_xticks()[::5], rotation=45)
    plt.show()

def family_movies(df_full_date):
    # filtering family movies
    family_movies = df_full_date[df_full_date['genres'].apply(lambda x: any(genre in x for genre in ['Family']) if isinstance(x, list) else False)]

    # Let's see the distribution of family movies through months
    plt.figure(figsize=(10, 6))
    sns.countplot(x='month', data=family_movies, palette=['#f0390f'])
    plt.title('Number of released family movies through months')
    plt.xlabel('Month')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

    return family_movies

def groupby_year_month(family_movies):
    # Grouping by year and month
    monthly_family_count = family_movies.groupby(['year', 'month']).size().reset_index(name='movie_count')
    december_count = monthly_family_count[monthly_family_count['month'] == 12]['movie_count']

    p_values = {}

    # Performing t-tests comparing December with each other month
    for month in range(1, 13):
        if month != 12:  
            
            other_month_count = monthly_family_count[monthly_family_count['month'] == month]['movie_count']
            t_stat, p_value = ttest_ind(december_count, other_month_count, equal_var=False)
            p_values[month] = p_value

    for month, p_value in p_values.items():
        print(f"Comparison of December with Month {month}: p-value = {p_value}")

    significant_months = [month for month, p_value in p_values.items() if p_value < 0.05]
    if significant_months:
        print(f"December has significantly more family movie releases than  the following months: {significant_months}")
    else:
        print("December does not have significantly more family movie releases than any other month.")

def family_trends_function(family_movies):
    family_trends = family_movies.groupby('month').agg({
        'revenue': 'mean',
        'genres': 'size'  
    }).reset_index()

    family_trends.dropna(inplace=True)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#f0390f'
    ax1.set_title('Revenue vs Count of Family Movies', fontsize=16)
    ax1.set_xlabel('Month', fontsize=14)
    ax1.set_ylabel('Average Revenue', color=color1)
    sns.lineplot(x='month', y='revenue', data=family_trends, ax=ax1, color=color1, label='Avg Revenue', marker='o')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)

    ax2 = ax1.twinx()
    color2 = '#1ecbe1'
    ax2.set_ylabel('Movie Count', color=color2)
    sns.lineplot(x='month', y='genres', data=family_trends, ax=ax2, color=color2, label='Movie Count', marker='o')
    ax2.tick_params(axis='y', labelcolor=color2)

    ax1.grid(True)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()
    return family_trends

def family_trends_regression(family_trends):
    slope, intercept, r_value, p_value, std_err = linregress(family_trends['month'], family_trends['revenue'])
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")

def family_trends_correlation(family_trends):
    slope, intercept, r_value, p_value, std_err = linregress(family_trends['month'], family_trends['genres'])
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")

def family_trends_regression_plot(family_trends):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='month', y='revenue', data=family_trends, ci=None)
    plt.title('Regression Plot of Revenue vs Month for Family Movies')
    plt.xlabel('Month')

def family_trends_correlation_plot(family_movies):
    december_period = family_movies[family_movies['month'] == 12]
    december_trends = december_period.groupby(['month', 'day']).agg({
        'revenue': 'mean',
        'genres': 'size'  # Count of movies per day
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#f0390f'
    ax1.set_title('Family Movies: December Analysis', fontsize=16)
    ax1.set_xlabel('Day of December', fontsize=14)
    ax1.set_ylabel('Average Revenue', color=color1)
    sns.lineplot(
        x='day', y='revenue', data=december_trends, ax=ax1, color=color1, label='Avg Revenue (December)', marker='o'
    )
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xticks(range(1, 32))
    ax1.set_xticklabels([f'Dec-{i}' for i in range(1, 32)], rotation=45)

    ax2 = ax1.twinx()
    color2 = '#1ecbe1'
    ax2.set_ylabel('Movie Count', color=color2)
    sns.lineplot(
        x='day', y='genres', data=december_trends, ax=ax2, color=color2, linestyle='--', label='Movie Count (December)', marker='x'
    )
    ax2.tick_params(axis='y', labelcolor=color2)
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
    return december_trends

def family_trends_correlation_plot_2(december_trends):
    # Find the days with the highest revenue and movie count
    top_revenue_days = december_trends.sort_values(by='revenue', ascending=False).head(4)
    top_movie_count_days = december_trends.sort_values(by='genres', ascending=False).head(4)

    print("Top 4 Days with Highest Average Revenue in December:")
    print(top_revenue_days)

    print("\nTop 4 Days with Highest Movie Count in December:")
    print(top_movie_count_days)

def  december_correlation_clean(december_trends):
    december_trends_clean = december_trends.replace([np.inf, -np.inf], np.nan).dropna(subset=['revenue', 'genres'])

    # Pearson correlation between revenue and movie count and p value
    correlation, p_value = pearsonr(december_trends_clean['revenue'], december_trends_clean['genres'])
    print(f"Pearson Correlation: {correlation}")
    print(f"P-value: {p_value}")


def halloween_analysis(df_full_date):
    horror_movies = df_full_date[df_full_date['genres'].apply(lambda x: any(genre in x for genre in ['Horror']) if isinstance(x, list) else False)]

    plt.figure(figsize=(10, 6))
    sns.countplot(x='month', data=horror_movies, palette=['#f0390f'])
    plt.title('Number of Released Horror Movies Around Halloween')
    plt.xlabel('Month')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

    return horror_movies


def halloween_ttest(horror_movies):
    monthly_horror_count = horror_movies.groupby(['year', 'month']).size().reset_index(name='movie_count')
    october_count = monthly_horror_count[monthly_horror_count['month'] == 10]['movie_count']

    p_values = {}

    # Performing t-tests comparing October with each other month
    for month in range(1, 13):
        if month != 10:  
            other_month_count = monthly_horror_count[monthly_horror_count['month'] == month]['movie_count']
            t_stat, p_value = ttest_ind(october_count, other_month_count, equal_var=False)
            p_values[month] = p_value

    for month, p_value in p_values.items():
        print(f"Comparison of October with Month {month}: p-value = {p_value}")

    # Interpret the results
    significant_months = [month for month, p_value in p_values.items() if p_value < 0.05]
    if significant_months:
        print(f"October has significantly more horror movie releases than the following months: {significant_months}")
    else:
        print("October does not have significantly more horror movie releases than any other month.")


def halloween_trends_function(horror_movies):
    horror_trends = horror_movies.groupby('month').agg({
        'revenue': 'mean',
        'genres': 'size' 
    }).reset_index()

    horror_trends.dropna(inplace=True)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#f0390f'
    ax1.set_title('Revenue vs Count of Horror Movies', fontsize=16)
    ax1.set_xlabel('Month', fontsize=14)
    ax1.set_ylabel('Average Revenue', color=color1)
    sns.lineplot(x='month', y='revenue', data=horror_trends, ax=ax1, color=color1, label='Avg Revenue', marker='o')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
    ax2 = ax1.twinx()
    color2 = '#1ecbe1'
    ax2.set_ylabel('Movie Count', color=color2)
    sns.lineplot(x='month', y='genres', data=horror_trends, ax=ax2, color=color2, label='Movie Count', marker='o')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    return horror_trends


def halloween_trends_correlation(horror_trends):
    correlation = horror_trends['revenue'].corr(horror_trends['genres'])
    print(f"Pearson Correlation between Revenue and Movie Count: {correlation}")
    p_value = pearsonr(horror_trends['revenue'], horror_trends['genres'])[1]
    print(f"P-value: {p_value}")


def halloween_trends(df_full_date):
    horror_movies_october = df_full_date[
        df_full_date['genres'].apply(lambda x: 'Horror' in x if isinstance(x, list) else False) & 
        (df_full_date['month'] == 10)
    ]
    horror_trends = horror_movies_october.groupby(['month', 'day']).agg({
        'revenue': 'mean',
        'genres': 'size'  
    }).reset_index()

    # Plotting 
    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#f0390f'
    ax1.set_title('Revenue vs Count of Horror Movies in October', fontsize=16)
    ax1.set_xlabel('Date (Month-Day)', fontsize=14)
    ax1.set_ylabel('Average Revenue', color=color1)
    sns.lineplot(x='day', y='revenue', data=horror_trends, ax=ax1, color=color1, label='Avg Revenue', marker='o')
    ax1.tick_params(axis='y', labelcolor=color1)
    horror_trends['date'] = horror_trends.apply(lambda row: f"{row['month']}-{row['day']}", axis=1)
    ax1.set_xticks(horror_trends['day'])
    ax1.set_xticklabels([f'Oct-{i}' for i in range(1, 32)], rotation=45)
    ax2 = ax1.twinx()
    color2 = '#1ecbe1'
    ax2.set_ylabel('Movie Count', color=color2)
    sns.lineplot(x='day', y='genres', data=horror_trends, ax=ax2, color=color2, label='Movie Count', marker='o')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

    return horror_movies_october


def halloween_highest_revenue(horror_trends):
    # Identify peak days for revenue and movie count
    top_revenue_days = horror_trends.sort_values(by='revenue', ascending=False).head(4)
    top_movie_count_days = horror_trends.sort_values(by='genres', ascending=False).head(4)

    print("Top 4 Days with Highest Average Revenue in October:")
    top_revenue_days.head()
    return top_movie_count_days, top_revenue_days

def halloween_ttest_2(horror_movies_october, top_movie_count_days, top_revenue_days):
    print("\nTop 4 Days with Highest Movie Count in October:")
    top_movie_count_days.head()

    top_revenue_days_data = horror_movies_october[horror_movies_october['day'].isin(top_revenue_days['day'])]
    top_revenue_days_trends = top_revenue_days_data.groupby('day').agg({
        'revenue': 'mean'
    }).reset_index()

    top_revenue_days_count = top_revenue_days_data.groupby('day').size().reset_index(name='movie_count')

    # Perform t-test for each top revenue day against all other days
    p_values = {}
    for day in top_revenue_days['day']:
        day_revenue = top_revenue_days_trends[top_revenue_days_trends['day'] == day]['revenue'].values[0]
        other_days_revenue = top_revenue_days_trends[top_revenue_days_trends['day'] != day]['revenue']
        t_stat, p_value = ttest_ind([day_revenue] * len(other_days_revenue), other_days_revenue, equal_var=False)
        p_values[day] = p_value

    for day, p_value in p_values.items():
        print(f"Comparison of Day {day} with Other Days: p-value = {p_value}")

    significant_days = [day for day, p_value in p_values.items() if p_value < 0.05]
    if significant_days:
        print(f"Revenue on the following days is significantly higher than on other days: {significant_days}")
    else:
        print("Revenue on the top days is not significantly higher than on other days.")    


def horror_nonhorror(horror_movies, df_full_date):
    # Filtering for Horror and Non-Horror movies released in October
    october_horror_movies = horror_movies[(horror_movies['month'] == 10)]
    non_horror_movies = df_full_date[(df_full_date['month'] == 10) & 
                                    (df_full_date['genres'].apply(lambda x: 'Horror' not in x if isinstance(x, list) else True))]

    horror_trends = october_horror_movies.groupby(['year', 'day']).size().reset_index(name='horror_count')
    non_horror_trends = non_horror_movies.groupby(['year', 'day']).size().reset_index(name='non_horror_count')

    plt.figure(figsize=(14, 8))
    sns.lineplot(x='day', y='horror_count', data=horror_trends, label='Horror Movies', color='#f0390f', marker='o', linewidth=2)
    sns.lineplot(x='day', y='non_horror_count', data=non_horror_trends, label='Non-Horror Movies', color='#1ecbe1', marker='o', linewidth=2)
    plt.axvline(x=31, color='black', linestyle='--', label='Halloween (Oct 31)', lw=2)
    plt.title('Horror vs Non-Horror Movie Releases in October', fontsize=16)
    plt.xlabel('Day of October', fontsize=14)
    plt.ylabel('Movie Count', fontsize=14)
    plt.xticks(ticks=range(1, 32), labels=[str(i) for i in range(1, 32)], rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return horror_trends, non_horror_trends


def horror_trends_regression(horror_trends):
    slope, intercept, r_value, p_value, std_err = linregress(horror_trends['day'], horror_trends['horror_count'])
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value**2}")
    print(f"P-value: {p_value}")


def valentine_analysis(df_full_date):
    valentine_movies = df_full_date[df_full_date['genres'].apply(lambda x: any(genre in x for genre in [ 'Romance']) if isinstance(x, list) else False)]

    # Let's see the distribution of romantic movies through months
    plt.figure(figsize=(10, 6))
    sns.countplot(x='month', data=valentine_movies, palette=['#f0390f'])
    plt.title('Number of released Romance movies through months')
    plt.xlabel('Month')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()
    return valentine_movies

def valentine_ttest(valentine_movies):
    monthly_valentine_count = valentine_movies.groupby(['year', 'month']).size().reset_index(name='movie_count')
    february_count = monthly_valentine_count[monthly_valentine_count['month'] == 2]['movie_count']

    p_values = {}

    for month in range(1, 13):
        if month != 2:  
            
            other_month_count = monthly_valentine_count[monthly_valentine_count['month'] == month]['movie_count']
            t_stat, p_value =ttest_ind(february_count, other_month_count, equal_var=False)
            p_values[month] = p_value

    for month, p_value in p_values.items():
        print(f"Comparison of February with Month {month}: p-value = {p_value}")

    significant_months = [month for month, p_value in p_values.items() if p_value < 0.05]
    if significant_months:
        print(f"February has significantly more Romance movie releases than the following months: {significant_months}")
    else:
        print("February does not have significantly more Romance movie releases than any other month.")


def valentine_trends(df_full_date):
    valentines_movies = df_full_date[
        df_full_date['genres'].apply(lambda x: 'Romance' in x if isinstance(x, list) else False) & 
        (df_full_date['month'] == 2)
    ]

    valentines_period = valentines_movies[
        ((valentines_movies['day'] >= 1) & (valentines_movies['day'] <= 30))  # Feb 10 to Feb 18
    ]

    valentines_trends = valentines_period.groupby(['month', 'day']).agg({
        'revenue': 'mean',
        'genres': 'size'  
    }).reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    color1 = '#f0390f'
    ax1.set_title('Revenue vs Count of Romance Movies (Valentine\'s Week)', fontsize=16)
    ax1.set_xlabel('Date (Month-Day)', fontsize=14)
    ax1.set_ylabel('Average Revenue', color=color1)
    sns.lineplot(x='day', y='revenue', data=valentines_trends, ax=ax1, color=color1, label='Avg Revenue', marker='o')
    ax1.tick_params(axis='y', labelcolor=color1)
    valentines_trends['date'] = valentines_trends.apply(lambda row: f"{row['month']}-{row['day']}", axis=1)
    ax1.set_xticks(valentines_trends['day'])
    ax1.set_xticklabels([f'Feb-{i}' for i in range(1, 29)], rotation=45)
    ax2 = ax1.twinx()
    color2 = '#1ecbe1'
    ax2.set_ylabel('Movie Count', color=color2)
    sns.lineplot(x='day', y='genres', data=valentines_trends, ax=ax2, color=color2, label='Movie Count', marker='o')
    ax2.tick_params(axis='y', labelcolor=color2)
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.tight_layout()
    plt.show()
    return valentines_trends, valentines_period

def top_days(valentines_trends):
    # Identifing peak days for revenue and movie count
    top_revenue_days = valentines_trends.sort_values(by='revenue', ascending=False).head(4)
    top_movie_count_days = valentines_trends.sort_values(by='genres', ascending=False).head(4)

    # Display the top days
    print("Top 4 Days with Highest Average Revenue in Valentine's Week:")
    top_revenue_days.head(4)
    return top_revenue_days


def top_count_days(top_movie_count_days):
    print("\nTop 4 Days with Highest Movie Count in Valentine's Week:")
    top_movie_count_days.head()


def valentine(valentines_period):
    valentines_trends = valentines_period.groupby(['month', 'day']).agg({
        'revenue': 'mean',
        'genres': 'size'
    }).reset_index()

    heatmap_data = valentines_trends.pivot_table(index='day', columns='month', values='revenue', aggfunc='mean')

    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='YlOrRd', fmt='.2f', linewidths=0.5, cbar_kws={'label': 'Average Revenue'})
    plt.title('Heatmap of Average Revenue for Romance Movies (Valentine\'s Week)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Day of February', fontsize=14)
    plt.tight_layout()
    plt.show()

def valentine_ttest_2(valentines_period, top_revenue_days):
    top_revenue_days_data = valentines_period[valentines_period['day'].isin(top_revenue_days['day'])]

    top_revenue_days_trends = top_revenue_days_data.groupby('day').agg({
        'revenue': 'mean'
    }).reset_index()

    top_revenue_days_count = top_revenue_days_data.groupby('day').size().reset_index(name='movie_count')

    # t-test
    p_values = {}
    for day in top_revenue_days['day']:
        day_revenue = top_revenue_days_trends[top_revenue_days_trends['day'] == day]['revenue'].values[0]
        other_days_revenue = top_revenue_days_trends[top_revenue_days_trends['day'] != day]['revenue']
        t_stat, p_value = ttest_ind([day_revenue] * len(other_days_revenue), other_days_revenue, equal_var=False)
        p_values[day] = p_value

    for day, p_value in p_values.items():
        print(f"Comparison of Day {day} with Other Days: p-value = {p_value}")

    significant_days = [day for day, p_value in p_values.items() if p_value < 0.05]
    if significant_days:
        print(f"Revenue on the following days is significantly higher than on other days: {significant_days}")
    else:
        print("Revenue on the top days is not significantly higher than on other days.")


    
