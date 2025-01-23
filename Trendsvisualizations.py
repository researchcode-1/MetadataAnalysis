

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import networkx as nx




# Load the file into a DataFrame
file_name="Abstract_with_keywordsFinal.csv"
data = pd.read_csv(file_name)

print(f"Loaded {len(data)} rows from {file_name}")
print (data.shape)
# Load the data
#data = pd.read_csv("abstracts_with_keywords.csv")

# Ensure columns exist (Adjust column names if needed)
if 'extracted_keywords' not in data.columns or 'topics' not in data.columns:
    raise ValueError("The dataset must contain 'extracted_keywords' and 'topics' columns.")

# Split keywords and topics into lists
data['keywords'] = data['extracted_keywords'].apply(lambda x: x.split("; "))
data['topics'] = data['topics'].apply(lambda x: x.split("; "))



# 1. Keyword Frequency Analysis
def plot_keyword_frequency(data):
    all_keywords = [kw for keywords in data['keywords'] for kw in keywords]
    keyword_counts = pd.Series(all_keywords).value_counts().head(20)

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    keyword_counts.sort_values(ascending=True).plot(kind='barh', color='skyblue')
    plt.title("Ranking of Top 20 Keywords by Frequency")
    plt.xlabel("Frequency")
    #plt.ylabel("Keywords")
    plt.tight_layout()
    plt.show()

# 2. Topic Trends Over Time
def plot_topic_trends(data):
    # Ensure 'year' is in numeric format
    data['year'] = pd.to_datetime(data['year'], errors='coerce').dt.year
    data = data[data['year'].between(2014, 2024)]
    # Explode topics and group by year
    topic_trends = data.explode('topics').groupby(['year', 'topics']).size().unstack(fill_value=0)

    # Filter to show top 10 topics (by total count across years)
    top_topics = topic_trends.sum().sort_values(ascending=False).head(10).index
    topic_trends = topic_trends[top_topics]

    # Plot trends
    plt.figure(figsize=(14, 8))  # Increased figure size
    for topic in topic_trends.columns:
        plt.plot(topic_trends.index, topic_trends[topic], label=topic)

    plt.title("Top 10 Topic Trends Over Time", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.legend(title="Topics", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)  # Legend outside the plot
    plt.grid(alpha=0.5)
    plt.tight_layout()  # Adjust layout
    plt.show()

import matplotlib.pyplot as plt


# Step 1: Ensure 'year' column is numeric and filter valid years
data['year'] = pd.to_numeric(data['year'], errors='coerce')  # Convert to numeric, NaN for invalid
data = data[data['year'].between(2014, 2024)]  # Filter years within the range


data['topics'] = data['topics'].astype(str).str.split(';')
data = data.explode('topics')
data['topics'] = data['topics'].str.strip()  # Remove extra spaces


# Step 2: Group by year and keyword
keyword_trends = data.groupby(['year', 'topics']).size().unstack(fill_value=0)



print(data.head())  # Check the first few rows of the dataset
print(data['topics'].unique())  # Ensure keywords are present
print(keyword_trends.head())  # Check the keyword trends dataframe

# Step 3: Select top 20 keywords by total frequency
top_keywords = keyword_trends.sum().sort_values(ascending=False).head(5).index
keyword_trends = keyword_trends[top_keywords]





# Step 4: Plot the trends
plt.figure(figsize=(14, 8))
for keyword in keyword_trends.columns:
    plt.plot(keyword_trends.index, keyword_trends[keyword], label=keyword)

plt.title("Trend of Top 5 topics Over Time", fontsize=16)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.legend(title="Topics", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.grid(alpha=0.5)
plt.ylim(1, 10)
plt.tight_layout()
plt.show()







# Run analyses and visualizations
plot_keyword_frequency(data)
plot_topic_trends(data)
#plot_co_occurrence_network(data)
#plot_heatmap(data)

