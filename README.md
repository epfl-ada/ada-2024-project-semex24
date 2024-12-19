# **Cinema Through Time: How Seasons and History Shape the Movies We Watch**

## **Abstract**
Our project explores how significant historical events and seasonal trends influence the films we watch, reflecting society’s evolving narratives. By examining the impact of events like World Wars, economic recessions, and modern-day challenges, we aim to uncover patterns in how cinema adapts to cultural shifts. This study analyzes genre popularity across seasons, such as horror in October and family films in December, to determine whether specific genres align with particular times of the year. Our goal is to reveal how historical context and seasonal preferences shape the evolution of cinema and connect audiences to stories that resonate with societal highs and lows.

## **Table of Contents**
1. [Project structure](#project-structure)
2. [Research Questions](#research-questions)
3. [Additional Dataset](#Additional-dataset)  
4. [Methods](#methods)  
5. [Proposed Timeline](#proposed-timeline)  
6. [Organization Within the Team](#organization-within-the-team)  
7. [Questions for TAs](#questions-for-tas) 

## **Project structure**

The directory structure of the project is as follows:

```
ADA-2024-PROJECT-SEMEX24/
│
├── data/                         <- Project data files
│   ├── character.metadata.tsv     <- Character metadata
│   ├── movie.metadata.tsv         <- Movie metadata
│   ├── movies_dataset.tsv         <- Dataset for movies preprocessed
│   └── plot_summaries.txt         <- Plot summaries for analysis
│
├── src/                           <- Source code
│   ├── data/                      <- Data loading and processing
│   │   └── data_loader.py         <- Script to load and process data
│   ├── media/                     <- Media files for the project
│   │   └── timeline_chart.png     <- Timeline chart image
│   ├── scripts/                   <- Jupyter Notebooks for various analysis
│   │   ├── data_cleaning.ipynb    <- Notebook for cleaning data
│   │   ├── combined_analysis.ipynb    <- Combined analysis notebook with seasonal and historical analysis
│   │   └── sentimental_analysis.ipynb <- Sentiment analysis notebook
│   └── utils/                     <- Utility scripts for functions
│       ├── EDA.py                 <- Functions for Exploratory Data Analysis
│       ├── historical.py          <- Functions for historical analysis
│       ├── sentimental_analysis.py<- Functions fo sentiment analysis
│       └── sesonal.py             <- Functions for seasonal analysis
│
├── .gitignore                     <- List of files ignored by git
├── environment.yml                <- File for setting up the Python environment
├── README.md                      <- Project README file
└── results.ipynb                  <- A well-structured notebook for final results
```

## **Research Questions**

**MAIN QUESTION:** 
**How do societal eras, including historical periods and seasonal trends, shape the evolution of cinema?**
   Objective: Investigate how societal changes, significant historical events, and seasonal patterns influence the development of film genres, themes, and storytelling across different time periods.

**OTHER QUESTIONS:**

1. **How do major historical events shape the genres and themes of movies?**
   - **Objective**: Examine how significant historical events (e.g., wars, economic crises, political changes) influence shifts in dominant genres and narrative themes.

2. **What seasonal trends exist in the popularity of specific movie genres?**
   - **Objective**: Identify patterns in genre popularity aligned with specific times of the year (e.g., horror in fall, family films in winter) and assess whether these seasonal trends have evolved over time in response to cultural or societal shifts.

3. **How does the sentiment in plot summaries reflect major historical events?**
   - **Objective**: Analyze the emotional tone in plot summaries across different historical periods, exploring how the sentiments expressed in cinema align with or react to the emotional climate of the time.

4. **How do historical periods and seasonal timing influence movie budgets?**
   - **Objective**: Investigate whether certain historical periods or specific release seasons (like summer) are associated with higher production budgets.

5. **What impact do release season and historical context have on a movie's box office revenue?**
   - **Objective**: Explore how the timing of a movie’s release, combined with the historical context, affects its financial performance, identifying optimal release strategies and the role of external influences on revenue outcomes.


## **Additional Dataset**

Alongside CMU, we will use the TMDB Movies Dataset 2024 from Kaggle, which provides a comprehensive collection of 1 million movies with metadata such as titles, release dates, genres, revenue, and popularity scores. This dataset will complement CMU Personas by filling in missing values, particularly in revenue and popularity fields, enhancing the overall data quality. The integration of TMDB data allows us to standardize genres and dates across datasets, ensuring consistency. Additionally, the enriched features from TMDB will enable us to perform a more in-depth analysis of seasonal trends and historical impacts, offering a fuller picture of audience preferences over time.

   Source: https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies?resource=download 

## **Methods**

1. **Data Collection & Cleaning**: We use the *CMU* dataset combined with the *TMDB Movies Dataset 2024* dataset to enhance our analysis. This step involves standardizing titles, genres, and dates and addressing missing values, particularly in revenue. This integration builds a reliable database that captures both historical context and movie-specific details.

2. **Exploratory Data Analysis (EDA)**: Conduct initial EDA to visualize genre distribution, and popularity across historical periods and seasons. Using bar charts and histograms, we assess patterns and variations in popularity, release year and revenue, setting the foundation for deeper analysis.

3. **Historical Impact Analysis**: We conduct regression analysis to assess the impact of major historical events on genre shifts and thematic changes. We investigate genre transformations in response to events like wars, economic crises, and socio-political shifts.

4. **Sentiment Analysis**: Using NLP, we analyze plot summaries to capture sentiment and thematic tones through time. This will add depth to our analysis of genre and theme changes across historical events.

5. **Seasonal Trend Analysis**: We apply statistical tests, like correlation and regression, to examine genre popularity by season, testing hypotheses on genre-season associations such as horror’s peak in October and family movies’ rise in December.

6. **Revenue Analysis Over Seasons**: Using time series analysis, we track revenue patterns by season, identifying financially significant periods. This reveals seasonal and event-based revenue peaks.

7. **Data Visualization**: We create interactive visualizations to illustrate genre-season relationships, revenue trends, and historical impact on cinema, using heatmaps, bar charts and plotlines to communicate our findings clearly.


## **Proposed Timeline**

1. **Step 1 (20.10.2024 - 26.10.2024)**:  
   - Dataset Preparation: Integrate CMU and TMDB datasets, standardize formats, and address missing values.

2. **Step 2 (24.10.2024 - 31.10.2024)**:  
   - Data Exploration: Conduct exploratory data analysis (EDA), create initial visualizations, and identify trends.

3. **Step 4 (24.10.2024 - 13.11.2024)**:  
   - Historical Impact Analysis: Explore genre shifts due to historical events and perform regression analysis to assess impact.

4. **Step 3 (24.10.2024 - 01.11.2024)**:  
   - Seasonal Trends Analysis: Analyze genre popularity by season using statistical methods.

5. **Step 5 (24.10.2024 - 13.11.2024)**:  
   - Revenue Analysis: Apply regression and correlation analysis to examine revenue patterns over time and across seasons.

6.  **Step 6 (2.11.2024 - 01.12.2024)**:  
   - Sentiment Analysis: Perform sentiment analysis on plot summaries to assess emotional tone during historical events.

7. **Step 7 (2.11.2024 - 01.12.2024)**:  
   - Repository Organization: Clean and structure the GitHub repository, ensuring the results.ipynb file is complete, well-organized, and fully documented.

8. **Step 8 (15.11.2024 - 15.12.2024)**:  
   - GitHub Pages Setup: Develop a GitHub Pages site for the project to display findings and visualizations interactively, creating a compelling data story to engage the audience.

9. **Step 9 (15.11.2024- 18.12.2024)**:  
   - Final Report and Submission: Update ReadMe with page URL and final information.

![Proposed Timeline](src/media/timeline_chart.png)

## **Organization Within the Team**


- **Step 1**:  Milica, Marija & Eugenio

- **Step 2**: Marija, Andrea & Daniela

- **Step 3**:  Milica & Eugenio

- **Step 4**:  Daniela & Andrea

- **Step 5**: Marija & Milica

- **Step 6**: Eugenio & Daniela

- **Step 7**: Milica, Andrea & Marija

- **Step 8**:  Marija & Eugenio

- **Step 9**: Milica, Andrea & Daniela

## **Group Contributions**  
- Milica: Analysis and graphs of the impact of holidays in movie genres, data preprocessing incorporating TMDB Movies Dataset
- Daniela: Sentiment analysis of plot summaries through time, EDA graphs
- Andrea: Impact of the World Wars in movies for historical analysis, EDA
- Eugenio: Building the webpage, impact of 9/11 and space race for historical analysis
- Marija: Writing up the data story, seasonal patterns analysis, data preprocessing incorporating TMDB Movies Dataset

