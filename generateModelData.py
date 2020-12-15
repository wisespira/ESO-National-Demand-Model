## for data
import pandas as pd
import numpy as np
from datetime import datetime,timedelta

#******************ESO 2020 set-up***********************
ESO_Data = pd.read_csv("./ESO and Weather Data/demand-data-2020.csv")
cols = ["SETTLEMENT_DATE","ND"]
ESO_Data = ESO_Data[cols]

currentDate = ""
ESO_DataSubSet = pd.DataFrame(columns=cols)
daysAvgND = 0
startingDay = 2 #Wedensday is 1/1/20

weekDay = 0

dayOfWeek = 3

#Ued to create the weekDay feature
def getWeekDay():
	global dayOfWeek
	if(dayOfWeek<=4):
		dayOfWeek += 1
		return 1
	elif(dayOfWeek ==5):
		dayOfWeek += 1
		return 0
	else:
		dayOfWeek=0
		return 0
		
#Take Avarage Demand for each SETTLEMENT_DATE
for index, row in ESO_Data.iterrows():
	date = datetime.strptime(row["SETTLEMENT_DATE"], '%d-%b-%Y')
	#initilise date <--could be refactored
	if(currentDate == ""):
		currentDate = date
	
	if(currentDate==date):
		daysAvgND = daysAvgND + row["ND"]
		
	else:
		ESO_DataSubSet = ESO_DataSubSet.append({'SETTLEMENT_DATE': currentDate.strftime('%d-%b-%Y'),'ND': str(daysAvgND/48),'Week_Day':getWeekDay()}, ignore_index=True)
		daysAvgND = row["ND"]
		currentDate = date
	if(date > datetime.strptime('01-SEP-2020', '%d-%b-%Y')):
		break	
		
print(ESO_DataSubSet.head())
ESO_Data = ESO_DataSubSet
ESO_Data = ESO_Data.rename(columns={"ND":"dailyND"})


#******************Weather.com data set-up***********************
weatherData = pd.read_csv("./ESO and Weather Data/data from weather.com.csv")
cols = ["Date","London Avg Temp"]
weatherData = weatherData[cols]
#print(weatherData.head())

#This works as the dates are in line (both start on 1st JAN 2020, Should refactor <----
ESO_Data = ESO_Data.join(weatherData["London Avg Temp"])
ESO_Data["dailyND"] = ESO_Data.dailyND.astype(float)
#data used for the rest of project
ESO_Data = ESO_Data.rename(columns={'London Avg Temp':'London_Avg_Temp'})

#******************ESO 2019 ND data***********************

ESO_DataSubSet_2019 = pd.DataFrame(columns=cols)
currentDate = ""
ESO_Data_2019 = pd.read_csv("./ESO and Weather Data/demanddata_2019.csv")
for index, row in ESO_Data_2019.iterrows():
	date = datetime.strptime(row["SETTLEMENT_DATE"], '%d-%b-%Y')
	#initilise date <--could be refactored
	if(currentDate == ""):
		currentDate = date
		
	if(date < datetime.strptime('01-SEP-2019', '%d-%b-%Y')):
		if(currentDate==date):
			daysAvgND = daysAvgND + row["ND"]
		else:		
			ESO_DataSubSet_2019 = ESO_DataSubSet_2019.append({'SETTLEMENT_DATE': date.strftime('%d-%b-%Y'),'ND': str(daysAvgND/48)}, ignore_index=True)
			daysAvgND = row["ND"]
			currentDate = date
	else:
		break	
#print("2019 Data\n")
#print(ESO_DataSubSet_2019.head())
ESO_Data_2019 = ESO_DataSubSet_2019
ESO_Data_2019 = ESO_DataSubSet_2019.rename(columns={"ND":"dailyND2019"})

#ESO_Data = ESO_Data.join(ESO_Data_2019["dailyND2019"])


#******************Done***********************

#print(ESO_Data.dtypes)
ESO_Data.to_csv('modelDataSet.csv')


