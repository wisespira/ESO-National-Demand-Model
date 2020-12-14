## for data
import pandas as pd
import numpy as np
## for plotting
import matplotlib.pyplot as plt
import seaborn as sns
## for statistical tests
import scipy
import statsmodels.formula.api as smf
import statsmodels.api as sm

ESO_Data = pd.read_csv("modelDataSet.csv")

#******************Correlation Testing***********************
correlationNDtemp = ESO_Data["dailyND"].corr(ESO_Data["London Avg Temp"])
correlationNDweekDay = ESO_Data["dailyND"].corr(ESO_Data["Week_Day"])

print("Correlation between ND and London Temp " + str(correlationNDtemp))
print("Correlation between ND and London Weekday " + str(correlationNDweekDay))

print("Week End average demand " +  str(ESO_Data[ESO_Data["Week_Day"]==0].dailyND.mean()))
print("Week Day average demand " +  str(ESO_Data[ESO_Data["Week_Day"]==1].dailyND.mean()))


#plt.title('Average Daily National Demand Against \nAvarage Daily Temperature in London')
#sns.regplot(x=ESO_Data['dailyND'],y=ESO_Data['Week_Day'])
#plt.show()








#ESO_Data = ESO_Data.rename(columns={"ND":"Y"})
def probabilityDistributionGraph(data):
	x = "dailyND"
	fig, ax = plt.subplots(nrows=1, ncols=2,  sharex=False, sharey=False)
	fig.suptitle(x, fontsize=20)
	### distribution
	ax[0].title.set_text('distribution')
	variable = data[x].fillna(data[x].mean())
	breaks = np.quantile(variable, q=np.linspace(0, 1, 11))
	variable = variable[ (variable > breaks[0]) & (variable < breaks[10]) ]
	sns.distplot(variable, hist=True, kde=True, kde_kws={"shade": True}, ax=ax[0])
	des = data[x].describe()
	ax[0].axvline(des["25%"], ls='--')
	ax[0].axvline(des["mean"], ls='--')
	ax[0].axvline(des["75%"], ls='--')
	ax[0].grid(True)
	des = round(des, 2).apply(lambda x: str(x))
	box = '\n'.join(("min: "+des["min"], "25%: "+des["25%"], "mean: "+des["mean"], "75%: "+des["75%"], "max: "+des["max"]))
	ax[0].text(0.95, 0.95, box, transform=ax[0].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

	### boxplot 
	ax[1].title.set_text('outliers (log scale)')
	tmp_dtf = pd.DataFrame(data[x])
	tmp_dtf[x] = np.log(tmp_dtf[x])
	tmp_dtf.boxplot(column=x, ax=ax[1])
	plt.show()



#probabilityDistributionGraph(ESO_Data)



