# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:38:20 2024

@author: ustpb
"""


# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

#read in the NEtflix CSV as DataFrame
netflix_df = pd.read_csv('netflix_data.csv')


# Subset the DataFrame for type "Movie"
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]

# Select only the columns of interest
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# Filter for durations shorted than 60 mintures
short_movies = netflix_movies[netflix_movies["duration"] < 60]


# Define an empty list
colors = []

# Iterate over rows of netflix_movies
for index, row in netflix_movies.iterrows():
    if row["genre"] == "Children":
        colors.append("red")
    elif row["genre"] == "Documentaries":
        colors.append("blue")
    elif row["genre"] == "Stand-Up":
        colors.append("green")
    else:
        colors.append("black")

# Inspect the first 10 values in the list
colors[:10]

# Set the figure style and initialize a new figure
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies.release_year, netflix_movies.duration, c=colors)

# Creat a title and axis label
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
answer = "no"