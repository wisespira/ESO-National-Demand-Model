
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
This project uses multilinear regression (MLR) to predict the national energy demand for England and Wales. The model is currently happily sitting with an average accuracy of ~92% and R^2 of ~0.72. The data used includes historical ND (national demand) data gathered from the National Grid ESO and London's daily average temperature scraped from weather.com to make its predictions. The project is still ongoing. Therefore, this readme contains both an account of the project and notes for further research.
</p>

<h3 align="center">contents</h3>
<p align="center">
<a  href="#Structure">Project Structure</a><br>
<a  href="#Data-Gathering">Data Gathering</a><br>
<a  href="#Data-Engineering">Feature Engineering</a><br>
<a  href="#Initial-Analysis">Data Analysis</a><br>
<a  href="#Feature-selection">Feature selection</a><br>
<a  href="#Model-Design">Model Design</a><br>
<a  href="#Model-Design">Preprocessing</a><br>
<a  href="#Performance">Performance</a><br>
 <!--- <a  href="#Summary">Summary</a><br>--->
</p>
<br>

<a name="Structure"></a>
<h2 align="center">Project Structure</h2>
<p>
Model.py - MLR Model and performance logic<br>
dataAnalysis.py - Data description and visualisations<br>
generateModelData.py - Generates modelDataSet.csv from data contained in 'ESO and Weather Data' directory
</p>

<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

England and Wales historical ND was gathered by the National Grid ESO's data portal (https://data.nationalgrideso.com/demand/historic-demand-data). Only the 2019 and 2020 set was used for simplicity. These sets came in the form of 48, 30 minute periods which comprised 1-days information on ND. <br>

Gathering large amounts of historical weather information proved difficult as such only London's daily average temperature data was added. This data was scraped from 'The Weather Channel' (https://weather.com/en-GB/weather/monthly/) and then cleaned in excel (see 'ESO and Weather Data/data from weather.com.xlsx' ).<br>

To combine the two data sets, the ND was first averaged for each day, then joined with the weather data.<br>
<a name="Data-Engineering"></a>
<h3 align="center">Data Engineering</h3>

Weekday/weekend data was added to the data set with a python function. The function looped through the set appending, 1 for weekdays and 0 for weekends. An adjusted copy of the 2019 data was also added, in which all data was sifted up one day. The reasoning for this was an assumption that day of the week would be more relevant than the date. <br>

<a name="Initial-Analysis"></a>
<h2 align="center">Data Analysis</h2>

A surface level analysis was conducted for any potential insights. 

<br>
 <p align="center">
<img  width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>

The average daily demand was right-skewed, it was unclear why this was. Possible factors included infrequent events like holidays/sporting events or a shorter period of the year where people were required heating. It may even be due to the data not featuring the full year or something else entirely. 

<p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/AverageNDEachDay2020.png">
 </p>
 
One trend found from Average ND throughout the year was the beginning of spring drop in average ND. This drop could account for the right skew, as most of the data takes place in spring and summer. Another observation is the pattern of one-off low ND, followed by a few days of high ND.
 
 
<p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/weekdayWeekendComparison.png">
  </p>  

Although the two data sets looked near-identical, the weekdays did have a notably higher upper quartile giving weekdays a higher impact on the right skew. It will be necessary to break the data down into days to find further insight.

 <p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/2019adjVS2019.png">
</p>

The assumption proved correct that the days of the week were more relevant in general. However, It would be interesting to look for dates which the calender aligned set did better as it may highlight other key elements.  

<a name="Feature-selection"></a>
<h3 align="center">Feature Selection</h3>
All variables were correlated, then one-way ANOVA tested against the 2020 ND. All but the weekday/weekend variable had predictive qualities, as shown below. <br>  <br>
 <p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/cor%26pvalueExcel.png">
</p>
Although both '2019 ND' and '2019 ND Adjusted' were explanatory variables, to remove potential multicollinearity problems, only the 2019 ajustend was used as it had a higher correlation. 
<a name="Model-Design"></a>
<h2 align="center">Model Design</h2>
There were a few obvious candidates for the design, including decision trees, multilinear regression (MLR), or neural network models.<br>

Although a linear relationship between independent and dependent variables was not fully proven in the analysis stage, MLR was chosen due to its simplistic setup and easy performance testing.

<a name="Preprocessing"></a>
<h3 align="center">Preprocessing</h3>

Was not fully implemented, currently commented out.

<a name="Performance"></a>
<h2 align="center">Performance</h2>

 <p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/results.png">
 </p>
 The overall performance was good, with a Mean Absolute Perc Error of around 8%.
    <p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/PredictedVsTrue.png">
 </p>


  <p align="center">
  <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/PredictedVsTrue2.png">
</p>
The areas highlighted are some of the models more noticeable under/over predictions, further investigation into why is needed.
<a name="Summary"></a>
 <!--- <h2 align="center">Summary</h2>
Overall the MLR model proved fairly accurate, only having an average error of 8%. 
