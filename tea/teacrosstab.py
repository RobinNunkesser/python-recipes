import pandas
import researchpy as rp
tea = pandas.read_csv("./data/tea.csv")

def chisquare(critical):
    for columnx in range(0,tea.columns.size-1):    
        for columny in range(columnx+1,tea.columns.size-1):
            result = rp.crosstab(tea[tea.columns[columnx]], tea[tea.columns[columny]],test= 'chi-square')[1]
            chivalue, pvalue, cramerv = result['results']
            if chivalue > critical and pvalue < 0.05:
                print(tea.columns[columnx]," / ", tea.columns[columny],": ",chivalue, sep="")      
          
chisquare(3.0)
