import pandas as pd

reviews = pd.read_csv("C:/Users/ibont/Desktop/IBON/Proiektuak/Cursos/Kaggle Panda Tutorial/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

reviews.head()

#Exercise 1
desc = reviews['description']
desc

#Exercise 2
first_description = reviews['description'][0]
first_description

#Exercise 3
first_row = reviews.iloc[0]
first_row

#Exercise 4
first_descriptions = reviews['description'].iloc[0:10]
first_descriptions

#Exercise 5
indices=[1,2,3,5,8]
sample_reviews = reviews.loc[[1,2,3,5,8]] # edo sample_reviews = reviews.loc[indices]
sample_reviews

#Exercise 6
indices6 = [0,1,10,100]
columnas = ['country','province','region_1','region_2']
df = reviews.loc[indices6,columnas]
df

#Exercise 7
columnas = ['country','variety']
df = reviews.loc[:99,columnas]
df

#Exercise 8
italian_wines = reviews.loc[reviews.country == 'Italy']

#Exercise 9
top_oceania_wines = reviews.loc[((reviews.country == 'Australia') | (reviews.country == 'New Zealand')) & (reviews.points >= 95)]
top_oceania_wines