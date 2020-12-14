## for data
import pandas as pd
import numpy as np
## for statistical tests

#******************ESO set-up***********************
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
		
	if(date < datetime.strptime('01-SEP-2020', '%d-%b-%Y')):
		if(currentDate==date):
			daysAvgND = daysAvgND + row["ND"]
		else:		
			ESO_DataSubSet = ESO_DataSubSet.append({'SETTLEMENT_DATE': date.strftime('%d-%b-%Y'),'ND': str(daysAvgND/48),'Week_Day':getWeekDay()}, ignore_index=True)
			daysAvgND = row["ND"]
			currentDate = date
	else:
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
print(ESO_Data.dtypes)

#data used for the rest of project
ESO_Data.to_csv('modelData.csv')


