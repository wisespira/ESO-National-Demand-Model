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
from sklearn.linear_model import LinearRegression

ESO_Data = pd.read_csv("modelDataSet.csv", index=False)
ESO_Data = ESO_Data.rename(columns={"dailyND":"Y"})

## split data
ESO_train, ESO_test = model_selection.train_test_split(ESO_Data, 
                      test_size=0.3)
## print info
print("X_train shape:", ESO_train.drop("Y",axis=1).shape, "| X_test shape:", ESO_test.drop("Y",axis=1).shape)
print("y_train mean:", round(np.mean(ESO_train["Y"]),2), "| y_test mean:", round(np.mean(ESO_test["Y"]),2))
print(ESO_train.shape[1], "features:", ESO_train.drop("Y",axis=1).columns.to_list())