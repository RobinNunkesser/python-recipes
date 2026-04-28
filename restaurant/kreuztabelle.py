import pandas
import researchpy as rp
restaurant = pandas.read_csv("./artifacts/python-recipes/restaurant/data/restaurant.csv")
table, result = rp.crosstab(restaurant[' type'],restaurant[' will_wait'],test='chi-square')
print(result)
print(table)
table, result = rp.crosstab(restaurant[' patrons'],restaurant[' will_wait'],test='chi-square')
print(result)
print(table)
