import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import researchpy as rp
sns.set_theme(style="whitegrid")
tea = pandas.read_csv("./tea/data/tea.csv")
table, result = rp.crosstab(tea['shape'],tea['refined'], test= 'chi-square')
print(table)
print(result)
#sns.countplot(x="socio.professional.category",hue="sex",data=tea)
#plt.xticks(rotation=45, ha='right')
#plt.tight_layout()
#plt.show()
