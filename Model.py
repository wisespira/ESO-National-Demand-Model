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
from datetime import datetime
from sklearn.linear_model import LinearRegression

plt.style.use('ggplot')
#plt.style.use('dark_background')
ESO_Data = pd.read_csv("modelDataSet.csv")
ESO_Datafull = pd.read_csv("modelDataSet.csv")
ESO_Data = ESO_Data.rename(columns={"dailyND":"Y"})
##Feature Selection 

ESO_Data = ESO_Data.drop('dailyND2019', 1)
ESO_Data = ESO_Data.drop('Week_Day', 1)
ESO_Data = ESO_Data.drop('SETTLEMENT_DATE', 1)
ESO_Data = ESO_Data.drop('Unnamed: 0', 1)

print(ESO_Data.head())
##Preprocessing 
##Should scale the data

## scale X
#ESO_Data_scalerX = preprocessing.RobustScaler(quantile_range=(25.0, 75.0))
#X = ESO_Data_scalerX.fit_transform(ESO_Data.drop("Y", axis=1))
#ESO_Data_scaled= pd.DataFrame(X, columns=ESO_Data.drop("Y", axis=1).columns, index=ESO_Data.index)
## scale Y
#ESO_Data_scalerY = preprocessing.RobustScaler(quantile_range=(25.0, 75.0))
#ESO_Data_scaled["Y"] = ESO_Data_scalerY.fit_transform(ESO_Data["Y"].values.reshape(-1,1))
#print(dtf_scaled.head())

#ESO_Data = dtf_scaled



##*************Set-Up***************
## split data
ESO_train, ESO_test = model_selection.train_test_split(ESO_Data,test_size=0.3)
## print info

X_names = ['London_Avg_Temp', 'dailyND2019Adj']
X_train = ESO_train[X_names].values
y_train = ESO_train["Y"].values
X_test = ESO_test[X_names].values
y_test = ESO_test["Y"].values

## call model
model = linear_model.LinearRegression()
## K fold validation
scores = []
#Breaks training data into 5 chunks and shuffels them 
cv = model_selection.KFold(n_splits=5, shuffle=True)
fig = plt.figure()
i = 1
colours = ["#ffbe0b","#fb5607","#ff006e","#8338ec","#3a86ff"]
##*************train***************
#Loop through the 5 chunks fitting the model and making a prediction
for train, test in cv.split(X_train, y_train):
    model = model.fit(X_train[train],y_train[train])
    prediction = model.predict(X_train[test])
    trueValue = y_train[test]
    score = metrics.r2_score(trueValue, prediction)
    scores.append(score)
	#ittrativly add the scatter plots
    plt.scatter(prediction, trueValue , lw=2, alpha=0.75,label='Fold %d (R2 = %0.2f)' % (i,score), c = colours[i-1])
    print(model.coef_)
    i += 1
plt.plot([min(y_train),max(y_train)], [min(y_train),max(y_train)],linestyle='--', lw=2, color='#013220')
plt.xlabel('Predicted Value')
plt.ylabel('True Value')
plt.title('K-Fold Validation on training set')
plt.legend()
#plt.show()

model = model.fit(X_train,y_train)

##*************Test***************
predicted = model.predict(X_test)
print(model.coef_)

## Key Performance Indicators
print("R2 (explained variance):", round(metrics.r2_score(y_test, predicted), 2))
print("Mean Absolute Perc Error (Σ(|y-pred|/y)/n):", round(np.mean(np.abs((y_test-predicted)/predicted)), 2))
print("Mean Absolute Error (Σ|y-pred|/n):", "{:,.0f}".format(metrics.mean_absolute_error(y_test, predicted)))
print("Root Mean Squared Error (sqrt(Σ(y-pred)^2/n)):", "{:,.0f}".format(np.sqrt(metrics.mean_squared_error(y_test, predicted))))
## residuals
residuals = y_test - predicted
max_error = max(residuals) if abs(max(residuals)) > abs(min(residuals)) else min(residuals)
max_idx = list(residuals).index(max(residuals)) if abs(max(residuals)) > abs(min(residuals)) else list(residuals).index(min(residuals))
max_true, max_pred = y_test[max_idx], predicted[max_idx]
print("Max Error:", "{:,.0f}".format(max_error))


## Plot predicted vs true Vale
fig = plt.figure()
ax = plt.axes()
from statsmodels.graphics.api import abline_plot
ax.scatter(predicted, y_test, color="black")
abline_plot(intercept=0, slope=1, color=colours[1], ax=ax)
ax.vlines(x=max_pred, ymin=max_true, ymax=max_true-max_error, color=colours[1], linestyle='--', alpha=0.7, label="max error")
ax.grid(True)
ax.set(xlabel="Predicted", ylabel="True Value", title="Predicted vs True")
ax.legend()
    
## Plot predicted vs residuals
#ax[1].scatter(predicted, residuals, color="red")
#ax[1].vlines(x=max_pred, ymin=0, ymax=max_error, color=colours[1], linestyle='--', alpha=0.7, label="max error")
#ax[1].grid(True)
#ax[1].set(xlabel="Predicted", ylabel="Residuals", title="Predicted vs Residuals")
#ax[1].hlines(y=0, xmin=np.min(predicted), xmax=np.max(predicted))
#ax[1].legend()




fig = plt.figure()
ax = plt.axes()
#ax.axes.get_xaxis().set_ticks([])
#ax.axes.get_xaxis().set_ticks()
ax.set_xticks([0,31,60,91,121,152,182,213,244]) # values
ax.set_xticklabels(["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP"]) # labels
#ax.set_xticks(np.arange(3), ['Tom', 'Dick', 'Sue'])
print(ax.axes.get_xaxis())
box = "Legend:\nYellow- Predicted ND\nRed- Actual ND"
ax.text(0.6, 0.975, box, transform=ax.transAxes, fontsize=10, va='top', ha="left", bbox=dict(boxstyle='round', facecolor='white', alpha=1))
ax.set_title('Predicted vs Actual ND')
ax.plot(ESO_Datafull['SETTLEMENT_DATE'], model.predict(ESO_Data[X_names].values), color = colours[0]);
ax.plot(ESO_Datafull['SETTLEMENT_DATE'], ESO_Datafull['dailyND'],color = colours[1]);

#ax.plot(ESO_Datafull['SETTLEMENT_DATE'], ESO_Datafull['dailyND2019'], color = colours[3]);
#ax.plot(ESO_Datafull['SETTLEMENT_DATE'], ESO_Datafull['dailyND2019Adj'], color = colours[3]);
plt.show()

