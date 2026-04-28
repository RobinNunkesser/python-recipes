import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

activities = [('Chatting or sending messages', 74.70),
              ('E-mailing', 70.95),
              ('Online banking', 62.90),
              ('Listening to music', 61.70),
              ('Watching videos', 61.10),
              ('Searching for products', 56.70),
              ('Buying products', 56.60),
              ('Uploading videos or photos', 54.55),
              ('Reading news pages', 52.30),
              ('Making internet calls', 47.45),
              ('Using online map / navigation services', 46.70),
              ('Watching movies / series', 44.85),
              ('Comparing prices', 43.30),
              ('Video gaming / online gaming', 39.05),
              ('Visiting special deal pages', 37.90),
              ('Reading blogs', 27.60),
              ('Visiting traveling pages', 26.40),
              ('Listening to internet radio', 26.35),
              ('Watching live TV', 25.90),
              ('Listening to podcasts', 25.60),
              ('Job search', 24.40),
              ('Writing comments in forums', 23),
              ('Selling products', 21.40),
              ('Writing customer reviews', 21),
              ('None of the above', 1.05),
              ('No answer', 0.30)
              ]

activitiesdf = pd.DataFrame(activities, columns=['Aktivität', 'Prozentwert'])
plt.style.use('dark_background')
plot = sns.barplot(activitiesdf, x="Prozentwert", hue="Prozentwert", legend=False, y="Aktivität", orient="h")
# xlabels = ['{:.0%}'.format(x) for x in plot.get_xticks()]
# plot.set_xticklabels(xlabels)
# plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/hsd/black/mobileactivities.svg")
