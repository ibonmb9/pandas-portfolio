import pandas as pd

pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("C:/Users/ibont/Desktop/IBON/Proiektuak/Cursos/Kaggle Panda Tutorial/winemag-data-130k-v2.csv", index_col=0)

#Exercise 1
median_points = reviews.points.median()
print(median_points)

#Exercise 2
countries = reviews.country.unique()
print(countries)

#Exercise 3
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)

#Exercise 4
centered_price = reviews.price - reviews.price.mean()

#Exercise 5
    # 1. Encontramos el indice del vino con mayor ratio puntos/precio
best_bargain_index = (reviews['points'] / reviews['price']).idxmax()

    # 2. Usamos .loc con ese indice para sacar el titulo
best_wine_title = reviews.loc[best_bargain_index, 'title']

print("El vino con mejor relacion calidad-precio es:")
print(best_wine_title)

#Exercise 6
