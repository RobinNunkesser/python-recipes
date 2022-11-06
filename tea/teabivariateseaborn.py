import pandas
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')

tea = pandas.read_csv("data/tea.csv")
sns.countplot(x="socio.professional.category",hue="sex",data=tea)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/itc/teapyth3.pdf")
plt.savefig("/Users/nunkesser/repos/work/images/itc/teapyth3.svg")
plt.show()