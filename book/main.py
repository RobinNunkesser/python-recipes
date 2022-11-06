import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create DataFrame
df = pd.DataFrame({'Day': ['2009', '2010', '2011', '2012', '2013'],
                   'Windows': [0.22, 0.46, 0.49, 0.59, 0.54],
                   'Android': [0.33, 0.46, 0.50, 0.49, 0.60],
                   'iOS': [0.33, 0.46, 0.50, 0.49, 0.60],
                   'macOS': [0.33, 0.46, 0.50, 0.49, 0.60],
                   'Linux': [0.33, 0.46, 0.50, 0.49, 0.60],
                   'Others': [0.33, 0.46, 0.50, 0.49, 0.60]})


#set seaborn plotting aesthetics
sns.set(style='white')

#create stacked bar chart
df.set_index('Day').plot(kind='bar', stacked=True)
#add overall title
plt.title('Customers by Time & Day of Week', fontsize=16)

#add axis titles
plt.xlabel('Day of Week')
plt.ylabel('Number of Customers')

#rotate x-axis labels
plt.xticks(rotation=45)

#plt.yticks(fmt='%.0f%%')

plt.savefig("/Users/nunkesser/Downloads/pythrobreg.pdf")