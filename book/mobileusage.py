import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

usage = pd.read_csv("./data/mobile_usage.csv")
sns.set(style='darkgrid')
sns.barplot(usage, orient="h", color='gray')
plt.xlabel('Nutzungshäufigkeit in Prozent')
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/mobile/smartphoneuse_neu.pdf")