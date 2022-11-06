import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

osraw = pd.read_csv("./data/os_combined-ww-yearly-2009-2022.csv")
os = osraw[['Date', 'Windows', 'macOS', 'iOS', 'Android', 'Linux']]
#os.loc['Other'] = 100 - os['Android'] - os['Windows'] - os['iOS'] - os['macOS'] - os['Linux']

#set seaborn plotting aesthetics
sns.set(style='darkgrid')

#create stacked bar chart
os.set_index('Date').plot(kind='bar', stacked=True)
#add overall title
#plt.title('Customers by Time & Day of Week', fontsize=16)

#add axis titles
plt.xlabel('Jahr')
plt.ylabel('Marktanteil')

#rotate x-axis labels
plt.xticks(rotation=45)

#plt.yticks(fmt='%.0f%%')

plt.savefig("/Users/nunkesser/repos/work/images/book/oshistory.pdf")