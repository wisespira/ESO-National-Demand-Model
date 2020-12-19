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
##Preprocessing 
from sklearn import preprocessing


ESO_Data = pd.read_csv("modelDataSet.csv")
#******************Describing Data***********************
print("******************Describing Data***********************")
print("weekday\n")
print(ESO_Data[ESO_Data["Week_Day"]==0].dailyND.describe())  
print("weekend\n")
print(ESO_Data[ESO_Data["Week_Day"]==1].dailyND.describe())  
print("London_Avg_Temp")
print(ESO_Data["London_Avg_Temp"].describe())  
print("")

#******************Correlation Testing***********************
print("******************Correlation Testing***********************")
correlationNDtemp = ESO_Data["dailyND"].corr(ESO_Data["London_Avg_Temp"])
correlationNDweekDay = ESO_Data["dailyND"].corr(ESO_Data["Week_Day"])
correlation2020_2019 = ESO_Data["dailyND"].corr(ESO_Data["dailyND2019"])
correlation2020_2019Adj = ESO_Data["dailyND"].corr(ESO_Data["dailyND2019Adj"])


print("Correlation between ND and London Temp " + str(correlationNDtemp))
print("Correlation between ND and London Weekday " + str(correlationNDweekDay))
print("Correlation between ND 2020 and ND 2019 " + str(correlation2020_2019))
print("Correlation between ND 2020 and ND 2019 Adj " + str(correlation2020_2019Adj))

weekEndAvg = ESO_Data[ESO_Data["Week_Day"]==0].dailyND.mean()
weekDayAvg = ESO_Data[ESO_Data["Week_Day"]==1].dailyND.mean()
print("")
#print("Week End average demand " +  str(weekEndAvg))
#print("Week Day average demand " +  str(weekDayAvg))

#******************P-Value Testing***********************
print("******************P-Value Testing***********************")
def getPvalue(feature,data):
	
	model = smf.ols('dailyND ~ ' + feature, data=ESO_Data).fit()
	table = sm.stats.anova_lm(model)
	p = table["PR(>F)"][0]
	coeff, p = None, round(p, 3)
	conclusion = "Correlated" if p < 0.05 else "Non-Correlated"
	print("Anova F: " +  feature + " is ", conclusion, "(p-value: "+str(p)+")")

	
getPvalue('London_Avg_Temp',ESO_Data)
getPvalue('Week_Day',ESO_Data)
getPvalue('dailyND2019',ESO_Data)
getPvalue('dailyND2019Adj',ESO_Data)
print("")


#******************Graphs***********************
plt.style.use('ggplot')



fig = plt.figure()
ax = plt.axes()
ax.axes.get_xaxis().set_ticks([])
ax.set_title('Average ND each day in 2020')
ax.set_xticks([0,31,60,91,121,152,182,213,244]) # values
ax.set_xticklabels(["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP"]) # labels
ax.plot(ESO_Data['SETTLEMENT_DATE'], ESO_Data['dailyND']);

#Should change to minMax this is a bad scaling
def robustScaler(df, column):
	df = preprocessing.RobustScaler(quantile_range=(25.0, 75.0))
	return df.fit_transform(ESO_Data[column].values.reshape(-1,1))
	

fig = plt.figure()
ax = plt.axes()
ax.axes.get_xaxis().set_ticks([])
ax.set_title('ND compared to London Avg Temp throughout the year (scaled)')
box = "legend:\nRed- London average Temp ND\nBlue- Actual ND"
ax.text(0.4, 0.975, box, transform=ax.transAxes, fontsize=10, va='top', ha="left", bbox=dict(boxstyle='round', facecolor='white', alpha=1))
ax.set_xticks([0,31,60,91,121,152,182,213,244]) # values
ax.set_xticklabels(["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP"]) # labels
ax.plot(ESO_Data['SETTLEMENT_DATE'], robustScaler(ESO_Data,"London_Avg_Temp"));
ax.plot(ESO_Data['SETTLEMENT_DATE'], robustScaler(ESO_Data,"dailyND"));
#print(robustScaler(ESO_Data,"London_Avg_Temp"))



fig, ax = plt.subplots(nrows=2, ncols=2,  sharex=False, sharey=False)
#fig.suptitle(x, fontsize=20)
x = "dailyND"
weekDayData = ESO_Data[ESO_Data["Week_Day"]==1].dailyND
WeekEndData = ESO_Data[ESO_Data["Week_Day"]==0].dailyND
	

tmp_dtf = pd.DataFrame(WeekEndData)
tmp_dtf.boxplot(column="dailyND",vert=False, ax=ax[1][0], color="#000000")
	

tmp_dtf = pd.DataFrame(weekDayData)
tmp_dtf.boxplot(column="dailyND",vert=False, ax=ax[1][1], color="#000000")	

ax[0][0].title.set_text('Average Daily ND\n on Weekends')
variable = WeekEndData.fillna(WeekEndData.mean())
breaks = np.quantile(variable, q=np.linspace(0, 1, 11))
variable = variable[ (variable > breaks[0]) & (variable < breaks[10]) ]
sns.distplot(variable, hist=True, kde=True, kde_kws={"shade": True}, axlabel = "Daily Average ND",ax=ax[0][0], color="#ffbe0b")
des = WeekEndData.describe()
ax[0][0].axvline(des["25%"], ls='--')
ax[0][0].axvline(des["mean"], ls='--')
ax[0][0].axvline(des["75%"], ls='--')
ax[0][0].grid(True)
des = round(des, 2).apply(lambda x: str(x))
box = '\n'.join(("min: "+des["min"], "25%: "+des["25%"], "mean: "+des["mean"], "75%: "+des["75%"], "max: "+des["max"]))
ax[0][0].text(0.95, 0.95, box, transform=ax[0][0].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

ax[0][1].title.set_text('Average Daily ND\n on Weekdays')
variable = weekDayData.fillna(weekDayData.mean())
breaks = np.quantile(variable, q=np.linspace(0, 1, 11))
variable = variable[ (variable > breaks[0]) & (variable < breaks[10]) ]
sns.distplot(variable, hist=True, kde=True, kde_kws={"shade": True}, axlabel = "Daily Average ND", ax=ax[0][1], color="#fb5607")
des = weekDayData.describe()
ax[0][1].axvline(des["25%"], ls='--')
ax[0][1].axvline(des["mean"], ls='--')
ax[0][1].axvline(des["75%"], ls='--')
ax[0][1].grid(True)
des = round(des, 2).apply(lambda x: str(x))
box = '\n'.join(("min: "+des["min"], "25%: "+des["25%"], "mean: "+des["mean"], "75%: "+des["75%"], "max: "+des["max"]))
ax[0][1].text(0.95, 0.95, box, transform=ax[0][1].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))


fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].scatter(ESO_Data["dailyND"], ESO_Data["dailyND2019"], color="#fb5607")
#ax[0].vlines(x=max_pred, ymin=0, ymax=max_error, color='black', linestyle='--', alpha=0.7, label="max error")
ax[0].grid(True)
ax[0].set(xlabel="2020 ND", ylabel="2019 ND", title="Each day in 2020 Average ND \ncompared to 2019 ND")

box = "Correlation: "+ str(correlation2020_2019)
ax[0].text(0.6, 0.975, box, transform=ax[0].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

ax[0].hlines(y=ESO_Data["dailyND"].min(), xmin=np.min(ESO_Data["dailyND"]), xmax=np.max(ESO_Data["dailyND"]))
ax[0].legend()


ax[1].scatter(ESO_Data["dailyND"], ESO_Data["dailyND2019Adj"], color="#ffbe0b")
ax[1].grid(True)
ax[1].set(xlabel="2020 ND", ylabel="2019 ND Adjusted", title="Each day in 2020 Average ND compared to 2019 ND\n Shifted a day forward")

box = "Correlation: "+ str(correlation2020_2019Adj)
ax[1].text(0.6, 0.975, box, transform=ax[1].transAxes, fontsize=10, va='top', ha="right", bbox=dict(boxstyle='round', facecolor='white', alpha=1))

ax[1].hlines(y=ESO_Data["dailyND"].min(), xmin=np.min(ESO_Data["dailyND"]), xmax=np.max(ESO_Data["dailyND"]))
ax[1].legend()
plt.show()


#plt.show()

#plt.title('Average Daily National Demand Against \naverage Daily Temperature in London')
#sns.regplot(x=ESO_Data['dailyND'],y=ESO_Data['Week_Day'])
#plt.show()



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



