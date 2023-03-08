import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

osraw = pd.read_csv("./data/os_mobile_combined-ww-yearly-2009-2022.csv")
os = osraw[['Date', 'iOS', 'Android']]

#set seaborn plotting aesthetics
#sns.set(style='darkgrid')

#create stacked bar chart
os.set_index('Date').plot(kind='bar', stacked=True)
#add overall title
#plt.title('Customers by Time & Day of Week', fontsize=16)

#add axis titles
plt.xlabel('Year')
plt.ylabel('Market share')

#rotate x-axis labels
plt.xticks(rotation=45)

#plt.yticks(fmt='%.0f%%')
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/articles/mobileixd/oshistory.pdf")