import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm

plt.style.use('dark_background')

belgium = pandas.read_csv("./data/belgium.csv")
resols = sm.OLS(belgium['V2'],sm.tools.tools.add_constant(belgium['V1'])).fit()
resrlm = sm.RLM(belgium['V2'],sm.tools.tools.add_constant(belgium['V1'])).fit()
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(belgium['V1'], belgium['V2'], 'o', label="data")
ax.plot(belgium['V1'], resols.fittedvalues, 'r-', label="OLS")
ax.plot(belgium['V1'], resrlm.fittedvalues, 'g-', label="RLM")
legend = ax.legend(loc="best")
plt.show()
plt.savefig("/Users/nunkesser/ISD/images/itc/pythrobreg.pdf")
plt.savefig("/Users/nunkesser/ISD/images/itc/pythrobreg.svg")
