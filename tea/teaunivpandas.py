import pandas
import matplotlib.pyplot as plt

plt.style.use('dark_background')

tea = pandas.read_csv("data/tea.csv")
tea['socio.professional.category'].value_counts().plot.bar()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/itc/teapyth.pdf")
plt.savefig("/Users/nunkesser/repos/work/images/itc/teapyth.svg")
plt.show()
