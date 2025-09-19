import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re

# Load data (assuming metadata.csv is in the same directory)
@st.cache_data
def load_data():
    df = pd.read_csv('metadata_sample cln.csv')
    # Basic cleaning
    df = df.dropna(subset=['title', 'publish_time'])
    df['abstract'] = df['abstract'].fillna('')
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Sidebar for filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
source_filter = st.sidebar.multiselect("Select sources", df['source_x'].unique(), default=df['source_x'].unique())

# Filter data
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1]) & (df['source_x'].isin(source_filter))]

st.write(f"Showing {len(filtered_df)} papers")

# Visualizations
st.header("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)

st.header("Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind='barh', ax=ax)
ax.set_title('Top 10 Publishing Journals')
st.pyplot(fig)

st.header("Word Cloud of Titles")
titles = filtered_df['title'].dropna()
text = ' '.join(titles)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Word Cloud of Paper Titles')
st.pyplot(fig)

st.header("Sample Data")
st.dataframe(filtered_df.head(10))