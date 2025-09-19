# python-covid-19-Analysis
# CORD-19 Data Analysis and Streamlit App

This project analyzes the CORD-19 metadata dataset and presents findings through a Streamlit web application.

## Overview

The CORD-19 dataset contains information about COVID-19 research papers. This analysis focuses on:
- Publication trends over time
- Top publishing journals
- Word frequency in paper titles
- Distribution by data source

## Dataset

The `metadata.csv` file from the CORD-19 dataset includes:
- Paper titles and abstracts
- Publication dates
- Authors and journals
- Source information

Download from: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge`

## Technologies Used

- Python
- Pandas
- Matplotlib

## Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the environment: `.venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt


### Streamlit App
Run the Streamlit app: `streamlit run app.py`

The app allows interactive filtering by year range and data source.

## Findings

- Most COVID-19 papers were published in 2021
- Top journals include various medical and scientific publications
- Common words in titles: covid, coronavirus, sars, etc.
- Sources are primarily from PMC, bioRxiv, etc.

## Challenges

- Handling large dataset size
- Dealing with missing values in abstracts
- Parsing dates in various formats


- Seaborn
- Streamlit
- WordCloud
