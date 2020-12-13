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
## for machine learning
from sklearn import model_selection, preprocessing, feature_selection, ensemble, linear_model, metrics, decomposition
## for explainer
from lime import lime_tabular
from datetime import datetime

#ESO set-up
ESO_Data = pd.read_csv("demanddata_2019.csv")
cols = ["SETTLEMENT_DATE","SETTLEMENT_PERIOD","ND"]
ESO_Data = ESO_Data[cols]


ESO_Data = ESO_Data["SETTLEMENT_DATE"<'10-MAR-2019']

for index, row in ESO_Data.iterrows():
	date = datetime.strptime(row[["SETTLEMENT_DATE"]], '%d-%b-%Y')
	if(date < datetime.strptime('10-MAR-2019', '%d-%b-%Y')):
		print(row["SETTLEMENT_DATE"])
	else:
		break


ESO_Data = ESO_Data.rename(columns={"ND":"Y"})



#Weather.com data set-up
weatherData = pd.read_csv("data from weather.com.csv")
cols = ["Date","London Avg Temp"]
weatherData = weatherData[cols]
#print(weatherData.head())








def dataAnalysis(dtf):
	x = "Y"
	fig, ax = plt.subplots(nrows=1, ncols=2,  sharex=False, sharey=False)
	fig.suptitle(x, fontsize=20)
	### distribution
	ax[0].title.set_text('distribution')
	variable = dtf[x].fillna(dtf[x].mean())
	breaks = np.quantile(variable, q=np.linspace(0, 1, 11))
	variable = variable[ (variable > breaks[0]) & (variable < breaks[10]) ]
	sns.distplot(variable, hist=True, kde=True, kde_kws={"shade": True}, ax=ax[0])
	des = dtf[x].describe()
	ax[0].axvline(des["25%"], ls='--')
	ax[0].axvline(des["mean"], ls='--')
	ax[0].axvline(des["75%"], ls='--')
	ax[0].grid(True)
	des = round(des, 2).apply(lambda x: str(x))
	box = '\n'.join(("min: "+des["min"], "25%: "+des["25%"], "mean: "+des["mean"], "75%: "+des["75%"], "max: "+des["max"]))
	ax[0].text(0.95, 0.95, box, transform=ax[0].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

	### boxplot 
	ax[1].title.set_text('outliers (log scale)')
	tmp_dtf = pd.DataFrame(dtf[x])
	tmp_dtf[x] = np.log(tmp_dtf[x])
	tmp_dtf.boxplot(column=x, ax=ax[1])
	plt.show()







