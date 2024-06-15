import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

subs = [(1993, 34),
        (1994, 56),
        (1995, 91),
        (1996, 145),
        (1997, 215),
        (1998, 318),
        (1999, 492),
        (2000, 740),
        (2001, 962),
        (2002, 1159),
        (2003, 1418),
        (2004, 1765),
        (2005, 2205),
        (2006, 2745),
        (2007, 3368),
        (2008, 4030),
        (2009, 4640),
        (2010, 5290),
        (2011, 5890),
        (2012, 6261),
        (2013, 6662),
        (2014, 6996),
        (2015, 7132),
        (2016, 7452),
        (2017, 7697),
        (2018, 7915),
        (2019, 8214),
        (2020, 8268),
        (2021, 8489),
        (2022, 8617),
        (2023, 8891)
        ]

subsdf = pd.DataFrame(subs, columns=['Jahr', 'Mobilfunkanschlüsse (in Millionen)'])
plt.style.use('dark_background')
plot = sns.barplot(subsdf, x="Jahr", hue="Jahr", legend=False, y="Mobilfunkanschlüsse (in Millionen)")
# ylabels = ['{:,.2f}'.format(y) + 'K' for y in plot.get_yticks() / 1000]
# plot.set_yticklabels(ylabels)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("/Users/nunkesser/repos/work/images/hsd/black/mobilesubscriptions.svg")
