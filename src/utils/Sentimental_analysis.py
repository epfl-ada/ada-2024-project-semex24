import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def sentiment_trend_over_time(merged_df, analyzer):
    # Apply sentiment analysis on the 'plot_summary' column
    merged_df['sentiment'] = merged_df['plot_summary'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

    # Calculate the average sentiment per year
    average_sentiment_by_year = merged_df.groupby('year')['sentiment'].mean().reset_index()

    # Plot the sentiment trend over time
    plt.plot(average_sentiment_by_year['year'], average_sentiment_by_year['sentiment'])
    plt.xlabel('Year')
    plt.ylabel('Average Sentiment (Compound Score)')
    plt.title('Sentiment Trend in Movies Over Time')
    plt.show()


def statistics(merged_df):
    # Basic statistics for the sentiment score
    print(merged_df['sentiment'].describe())

    # Count the number of positive, neutral, and negative summaries
    positive_count = len(merged_df[merged_df['sentiment'] > 0])
    neutral_count = len(merged_df[merged_df['sentiment'] == 0])
    negative_count = len(merged_df[merged_df['sentiment'] < 0])

    print("Positive summaries:", positive_count)
    print("Neutral summaries:", neutral_count)
    print("Negative summaries:", negative_count)


def sentiment_trend_with_historical_events(merged_df):
    average_sentiment_by_year = merged_df.groupby('year')['sentiment'].mean().reset_index()
    # Create the average sentiment trend plot over time
    plt.plot(average_sentiment_by_year['year'], average_sentiment_by_year['sentiment'], label="Average Sentiment")

    # Mark historical events
    historical_events = {
        "World War I": 1914,
        "Great Depression": 1929,
        "World War II": 1939,
        "Cold War (Start)": 1947,
        "Vietnam War (Start)": 1955,
        "Fall of the Berlin Wall": 1989,
        "September 11 Attacks": 2001,
        "Great Recession": 2008,
    }

    # Add vertical lines for the event years
    for event, year in historical_events.items():
        plt.axvline(x=year, color='red', linestyle='--', alpha=0.7)
        plt.text(year, plt.ylim()[1]*0.9, event, rotation=90, verticalalignment='top', color='red', fontsize=8)

    # Configure the plot
    plt.xlabel('Year')
    plt.ylabel('Average Sentiment (Compound Score)')
    plt.title('Sentiment Trend in Movies Over Time with Historical Events')
    plt.legend()
    plt.show()


def ttest_ind_sentiment(merged_df):
    # Define historical events with their respective periods
    historical_events = {
        "World War I": {"before": (1900, 1913), "during": (1914, 1918), "after": (1919, 1925)},
        "Great Depression": {"before": (1926, 1928), "during": (1929, 1933), "after": (1934, 1939)},
        "World War II": {"before": (1930, 1938), "during": (1939, 1945), "after": (1946, 1955)},
        "Space Race": {"before": (1950, 1956), "during": (1957, 1969), "after": (1970, 1975)},
        "9/11": {"before": (1995, 2000), "during": (2001, 2001), "after": (2002, 2006)},
        "Great Recession": {"before": (2000, 2006), "during": (2007, 2009), "after": (2010, 2015)}
    }

    # Loop through each historical event
    for event, periods in historical_events.items():
        # Filter data for each period
        period_before = merged_df[(merged_df['release_date'].dt.year >= periods["before"][0]) & 
                                (merged_df['release_date'].dt.year <= periods["before"][1])]
        period_during = merged_df[(merged_df['release_date'].dt.year >= periods["during"][0]) & 
                                (merged_df['release_date'].dt.year <= periods["during"][1])]
        period_after = merged_df[(merged_df['release_date'].dt.year >= periods["after"][0]) & 
                                (merged_df['release_date'].dt.year <= periods["after"][1])]
        
        # Calculate average sentiment for each period
        sentiment_before = period_before['sentiment'].mean()
        sentiment_during = period_during['sentiment'].mean()
        sentiment_after = period_after['sentiment'].mean()
        
        # Display the average sentiments
        print(f"\n{event} Sentiment Averages:")
        print(f"Before {event}: {sentiment_before}")
        print(f"During {event}: {sentiment_during}")
        print(f"After {event}: {sentiment_after}")
        
        # Perform t-tests to check for significant differences
        t_stat_before_during, p_val_before_during = ttest_ind(period_before['sentiment'], period_during['sentiment'], nan_policy='omit')
        t_stat_during_after, p_val_during_after = ttest_ind(period_during['sentiment'], period_after['sentiment'], nan_policy='omit')
        t_stat_before_after, p_val_before_after = ttest_ind(period_before['sentiment'], period_after['sentiment'], nan_policy='omit')
        
        # Display t-test results
        print(f"\nt-test results for {event}:")
        print(f"Before vs During: t-statistic = {t_stat_before_during}, p-value = {p_val_before_during}")
        print(f"During vs After: t-statistic = {t_stat_during_after}, p-value = {p_val_during_after}")
        print(f"Before vs After: t-statistic = {t_stat_before_after}, p-value = {p_val_before_after}")
        
        # Interpretations
        if p_val_before_during < 0.05:
            print("Statistically significant sentiment change from before to during the event.")
        else:
            print("No statistically significant sentiment change from before to during the event.")

        if p_val_during_after < 0.05:
            print("Statistically significant sentiment change from during to after the event.")
        else:
            print("No statistically significant sentiment change from during to after the event.")

        if p_val_before_after < 0.05:
            print("Statistically significant sentiment change from before to after the event.")
        else:
            print("No statistically significant sentiment change from before to after the event.")



def comparison_ww2(merged_df):
    # Filter for the WWII period (1939-1945)
    ww2_df = merged_df[(merged_df['year'] >= 1939) & (merged_df['year'] <= 1945)]
    average_sentiment_ww2 = ww2_df['sentiment'].mean()
    print(f"Average sentiment during World War II (1939-1945): {average_sentiment_ww2}")

    # Period before the war (1930-1938)
    pre_ww2_df = merged_df[(merged_df['year'] >= 1930) & (merged_df['year'] < 1939)]
    average_sentiment_pre_ww2 = pre_ww2_df['sentiment'].mean()
    print(f"Average sentiment before World War II (1930-1938): {average_sentiment_pre_ww2}")

    # Period after the war (1946-1955)
    post_ww2_df = merged_df[(merged_df['year'] > 1945) & (merged_df['year'] <= 1955)]
    average_sentiment_post_ww2 = post_ww2_df['sentiment'].mean()
    print(f"Average sentiment after World War II (1946-1955): {average_sentiment_post_ww2}")

    # Define periods and corresponding average sentiments
    years = ['1930-1938 (Pre-War)', '1939-1945 (World War II)', '1946-1955 (Post-War)']
    average_sentiments = [average_sentiment_pre_ww2, average_sentiment_ww2, average_sentiment_post_ww2]

    # Plot the sentiment comparison
    plt.figure(figsize=(10, 6))
    plt.bar(years, average_sentiments, color=['blue', 'red', 'green'])
    plt.xlabel('Period')
    plt.ylabel('Average Sentiment (Compound Score)')
    plt.title('Comparison of Average Sentiment in Cinema During and Around World War II')
    plt.show()


def stats_sentiment_ww2(merged_df):
    # Filter the periods before, during, and after World War II
    period_before_war = merged_df[(merged_df['release_date'].dt.year >= 1930) & (merged_df['release_date'].dt.year <= 1938)]
    period_during_war = merged_df[(merged_df['release_date'].dt.year >= 1939) & (merged_df['release_date'].dt.year <= 1945)]
    period_after_war = merged_df[(merged_df['release_date'].dt.year >= 1946) & (merged_df['release_date'].dt.year <= 1955)]

    # Calculate the average sentiment for each period
    sentiment_before_war = period_before_war['sentiment'].mean()
    sentiment_during_war = period_during_war['sentiment'].mean()
    sentiment_after_war = period_after_war['sentiment'].mean()

    # Display the average sentiment results
    print("Average sentiment before World War II (1930-1938):", sentiment_before_war)
    print("Average sentiment during World War II (1939-1945):", sentiment_during_war)
    print("Average sentiment after World War II (1946-1955):", sentiment_after_war)

    # Perform t-tests between periods to check for significant differences
    t_stat_before_during, p_val_before_during = ttest_ind(period_before_war['sentiment'], period_during_war['sentiment'], nan_policy='omit')
    t_stat_during_after, p_val_during_after = ttest_ind(period_during_war['sentiment'], period_after_war['sentiment'], nan_policy='omit')
    t_stat_before_after, p_val_before_after = ttest_ind(period_before_war['sentiment'], period_after_war['sentiment'], nan_policy='omit')

    # Display the t-test results
    print("\nt-test between before and during the war:")
    print("t-statistic:", t_stat_before_during, "p-value:", p_val_before_during)

    print("\nt-test between during and after the war:")
    print("t-statistic:", t_stat_during_after, "p-value:", p_val_during_after)

    print("\nt-test between before and after the war:")
    print("t-statistic:", t_stat_before_after, "p-value:", p_val_before_after)

    # Interpretation
    if p_val_before_during < 0.05:
        print("\nThe difference in sentiment between the period before and during the war is statistically significant.")
    else:
        print("\nThere is no statistically significant difference in sentiment between the period before and during the war.")

    if p_val_during_after < 0.05:
        print("The difference in sentiment between the period during and after the war is statistically significant.")
    else:
        print("There is no statistically significant difference in sentiment between the period during and after the war.")

    if p_val_before_after < 0.05:
        print("The difference in sentiment between the period before and after the war is statistically significant.")
    else:
        print("There is no statistically significant difference in sentiment between the period before and after the war.")