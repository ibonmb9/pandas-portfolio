import pandas as pd

reviews = pd.read_csv("C:/Users/ibont/Desktop/IBON/Proiektuak/Cursos/Kaggle Panda Tutorial/winemag-data-130k-v2.csv", index_col=0)

#Exercise 1
dtype = reviews.points.dtype

#Exercise 2
point_strings = reviews.points.astype('str')

#Exercise 3
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

#Exercise 4
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending = False)