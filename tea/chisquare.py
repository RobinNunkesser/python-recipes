import pandas
import researchpy as rp

tea = pandas.read_csv("./data/tea.csv")
table, result = rp.crosstab(tea['shape'],tea['refined'],test='chi-square')

