import pandas as pd

pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("C:/Users/ibont/Desktop/IBON/Proiektuak/Cursos/Kaggle Panda Tutorial/winemag-data-130k-v2.csv", index_col=0)

#Exercise 1
reviews_written = reviews.groupby(['taster_twitter_handle']).size()

#Exercise 2
best_rating_per_price = reviews.groupby(['price']).points.max()

#Exercise 3
price_extremes = reviews.groupby(['variety']).price.agg([min,max])

#Exercise 4
sorted_varieties = reviews.groupby(['variety']).price.agg([min,max]).sort_values(by=['min','max'],ascending=False)

#Exercise 5
reviewer_mean_ratings = reviews.groupby(['taster_name']).points.mean()

#Exercise 6
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)
