# sentiment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from scipy.stats import ttest_ind

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# 1. Function to calculate sentiment scores
def calculate_sentiment_scores(df, text_column):
    df['sentiment'] = df[text_column].apply(lambda x: analyzer.polarity_scores(x)['compound'])
    return df

# 2. Function to calculate average sentiment per year
def calculate_average_sentiment_by_year(df, year_column='year', sentiment_column='sentiment'):
    average_sentiment_by_year = df.groupby(year_column)[sentiment_column].mean().reset_index()
    return average_sentiment_by_year

# 3. Function to plot sentiment trend over time
def plot_sentiment_trend(average_sentiment_by_year, year_column='year', sentiment_column='sentiment'):
    plt.figure(figsize=(10, 6))
    plt.plot(average_sentiment_by_year[year_column], average_sentiment_by_year[sentiment_column], label="Average Sentiment")
    plt.xlabel('Year')
    plt.ylabel('Average Sentiment (Compound Score)')
    plt.title('Sentiment Trend in Movies Over Time')
    plt.legend()
    plt.tight_layout()
    plt.show()

# 4. Function to compare sentiment across historical periods
def compare_sentiment_periods(df, period_dict, sentiment_column='sentiment'):
    period_sentiments = {}
    for period, (start, end) in period_dict.items():
        period_df = df[(df['year'] >= start) & (df['year'] <= end)]
        avg_sentiment = period_df[sentiment_column].mean()
        period_sentiments[period] = avg_sentiment
        print(f"Average sentiment during {period} ({start}-{end}): {avg_sentiment}")
    return period_sentiments

# 5. Function to perform t-tests between historical periods
def t_test_between_periods(df, period_dict, sentiment_column='sentiment'):
    periods_data = {}
    for period, (start, end) in period_dict.items():
        periods_data[period] = df[(df['year'] >= start) & (df['year'] <= end)][sentiment_column]
    
    t_test_results = {}
    period_names = list(periods_data.keys())
    for i in range(len(period_names)):
        for j in range(i+1, len(period_names)):
            period1 = period_names[i]
            period2 = period_names[j]
            t_stat, p_val = ttest_ind(periods_data[period1], periods_data[period2], nan_policy='omit')
            t_test_results[(period1, period2)] = (t_stat, p_val)
            print(f"T-test between {period1} and {period2}: t-stat = {t_stat}, p-val = {p_val}")
    
    return t_test_results

# 6. Function to visualize sentiment with historical event markers
def plot_sentiment_with_events(average_sentiment_by_year, events, year_column='year', sentiment_column='sentiment'):
    plt.figure(figsize=(10, 6))
    plt.plot(average_sentiment_by_year[year_column], average_sentiment_by_year[sentiment_column], label="Average Sentiment")

    # Mark events
    for event, year in events.items():
        plt.axvline(x=year, color='red', linestyle='--', alpha=0.7)
        plt.text(year, plt.ylim()[1] * 0.9, event, rotation=90, verticalalignment='top', color='red', fontsize=8)
    
    plt.xlabel('Year')
    plt.ylabel('Average Sentiment (Compound Score)')
    plt.title('Sentiment Trend in Movies Over Time with Historical Events')
    plt.legend()
    plt.tight_layout()
    plt.show()
