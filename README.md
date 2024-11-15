# **Cinema Through Time: How Seasons and History Shape the Movies We Watch**

## **Abstract**
Our project explores how significant historical events and seasonal trends influence the films we watch, reflecting society’s evolving narratives. By examining the impact of events like World Wars, economic recessions, and modern-day challenges, we aim to uncover patterns in how cinema adapts to cultural shifts. This study analyzes genre popularity across seasons, such as horror in October and family films in December, to determine whether specific genres align with particular times of the year. Our goal is to reveal how historical context and seasonal preferences shape the evolution of cinema and connect audiences to stories that resonate with societal highs and lows.

## **Table of Contents**
1. [Research Questions](#research-questions)  
2. [Additional Dataset](#Additional-Datasets)  
3. [Methods](#methods)  
4. [Proposed Timeline](#proposed-timeline)  
5. [Organization Within the Team](#organization-within-the-team)  
6. [Questions for TAs](#questions-for-tas) 


## **Research Questions**

1. **How do major historical events influence the themes and genres of movies?**
   - Objective: Identify shifts in genre and thematic focus during significant historical periods, such as wars or economic recessions.

2. **Are there specific seasons where certain movie genres are more popular?**
   - Objective: Examine seasonal trends to see if particular genres align with times of the year, such as horror in autumn or family films in winter.

3. **How do historical events and seasonal timing impact movie budgets?**
   - Objective: Analyze if and how budgets vary across seasons and historical events, identifying trends in production investment.

4. **What is the relationship between release season, historical context, and movie revenue?**
   - Objective: Investigate how the timing of a movie’s release affects its financial success, considering both seasonal peaks and historical influences.

5. **What are the predominant sentiments in plot summaries during historical events?**
   - Objective: Explore the emotional tone in movie plots, examining how sentiment trends align with or respond to major historical events.

6. **How has language diversity in movies changed in response to historical events and audience shifts over time?**
   - Objective: Explore the variation in language representation within movies over different historical periods, reflecting cultural and societal changes.

## **Additional Dataset**

Alongside CMU, we will use the TMDB Movies Dataset 2024 from Kaggle, which provides a comprehensive collection of 1 million movies with metadata such as titles, release dates, genres, revenue, and popularity scores. This dataset will complement CMU Personas by filling in missing values, particularly in revenue and popularity fields, enhancing the overall data quality. The integration of TMDB data allows us to standardize genres and dates across datasets, ensuring consistency. Additionally, the enriched features from TMDB will enable us to perform a more in-depth analysis of seasonal trends and historical impacts, offering a fuller picture of audience preferences over time.

## **Methods**

1. **Data Collection & Cleaning**: We will use the *CMU* dataset combined with the *TMDB Movies Dataset 2024* dataset to enhance our analysis. This step involves standardizing titles, genres, and dates and addressing missing values, particularly in revenue. This integration builds a reliable database that captures both historical context and movie-specific details.

2. **Exploratory Data Analysis (EDA)**: Conduct initial EDA to visualize genre distribution, and popularity across historical periods and seasons. Using bar charts and time series, we’ll assess patterns and variations in popularity and revenue, setting the foundation for deeper analysis.

3. **Seasonal Trend Analysis**: We’ll apply statistical tests (e.g., chi-square, ANOVA) to examine genre popularity by season, testing hypotheses on genre-season associations such as horror’s peak in October and family movies’ rise in December.

4. **Historical Impact Analysis**: We’ll conduct regression analysis to assess the impact of major historical events on genre shifts and thematic changes. We’ll investigate genre transformations in response to events like wars, economic crises, and socio-political shifts.

5. **Revenue Analysis Over Time**: Using time series analysis, we’ll track revenue patterns by season and historical context, identifying financially significant periods. This will reveal seasonal and event-based revenue peaks.

6. **Clustering for Genre and Country Insights**: We’ll apply clustering algorithms, like K-means, to identify patterns in genre preferences based on release season and country, aiming to uncover optimal release strategies based on cultural and regional differences.

7. **Sentiment Analysis**: Using NLP, we’ll analyze plot summaries to capture sentiment and thematic tones. This will add depth to our analysis of genre and theme changes across historical events.

8. **Data Visualization**: We’ll create interactive visualizations to illustrate genre-season relationships, revenue trends, and historical impact on cinema, using heatmaps and bubble charts to communicate our findings clearly.


## **Proposed Timeline**

1. **Step 1 (28.10.2024 - 01.11.2024)**: Integrate CMU and TMDB datasets, standardize formats, and address missing values.
2. **Step 2 (04.11.2024 - 08.11.2024)**: Conduct EDA, create visualizations, and identify trends.
3. **Step 3 (11.11.2024 - 14.11.2024)**: Analyze seasonal genre trends using statistical methods.
4. **Step 4 (11.11.2024 - 14.11.2024)**: Perform regression analysis on historical events' impact.
5. **Step 5 (02.12.2023 - 06.12.2024)**: Apply time series analysis to revenue patterns.
6. **Step 6 (09.12.2023 - 13.12.2024)**: Conduct clustering for genre and regional preferences.
7. **Step 7 (09.12.2023 - 13.12.2024)**: Perform sentiment analysis on plot summaries.
8. **Step 8 (16.12.2023 - 20.12.2024)**: Finalize visualizations, compile findings, and complete the report.

![Proposed Timeline](src/media/timeline_chart.png)

## **Organization Within the Team**

- **Dataset Preparation**: Milica & Marija - Integrate datasets, address missing values.
- **Data Exploration**: Marija & Eugenio - Conduct EDA and create visualizations.
- **Seasonal Trends Analysis**: Milica & Marija - Analyze genre popularity by season.
- **Historical Impact Analysis**: Daniela & Marija - Explore genre shifts due to historical events.
- **Revenue Analysis**: Andrea & Eugenio - Perform time series analysis on revenue.
- **Clustering Analysis**: Milica & Eugenio - Analyze genre and country preferences.
- **Sentiment Analysis**: Daniela & Andrea - Analyze plot sentiment.
- **Final Report and Visualization**: Marija, Andrea & Daniela - Develop visualizations and finalize the report.

## **Questions for TAs**  
- Do you have recommendations on tools for visualizing seasonal and historical trends effectively?  
- Should we prioritize a specific method for clustering genres and countries, or experiment with multiple algorithms? 

---

