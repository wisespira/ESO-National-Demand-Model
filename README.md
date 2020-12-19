
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
This project uses Multiple linear regression to create a predictive model for England and Wales national energy demand. The model is currently happily sitting with an average accuracy of 92%. The data used includes historical ND (national demand) data gathered from the National Grid ESO and London's daily average temperature scraped from weather.com to make its predictions. There is still much work to be done and as such, this readme contains both an account of the project and notes for further research. 
</p>
<h3 align="center">contents</h3>
<p align="center">
<a  href="#Data-Gathering">Data Gathering</a><br>
<a  href="#Data-Engineering">Feature Engineering</a><br>
<a  href="#Initial-Analysis">Data Analysis</a><br>
<a  href="#Feature-selection">Feature selection</a><br>
<a  href="#Model-Design">Model Design</a><br>
<a  href="#Model-Design">Preprocessing</a><br>
<a  href="#Performance">Performance</a><br>
<a  href="#Summary">Summary</a><br>
</p>
<br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

England and Wales historical ND was gathered from National Grid ESO's data portal (https://data.nationalgrideso.com/demand/historic-demand-data). For simplicity, only the 2019 and 2020 set was used. The data came split into 48, 30 minute periods which comprised 1-days information on ND. <br>

Gathering large amounts of historical weather information proved difficult, as such only the London daily average temperature data was added. This data was scraped from 'The Weather Channel' (https://weather.com/en-GB/weather/monthly/) and then cleaned in excel (see 'ESO and Weather Data/data from weather.com.xlsx' ).<br>

To combine the two data sets the ND was averaged for each day then the weather data was joined. <br>
<a name="Data-Engineering"></a>
<h3 align="center">Data Engineering</h3>

Weekday/weekend data was added to the data set with a python function by looping through the set appending 1 for weekdays and 0 for weekends. An adjusted copy of the 2019 data was also added in which all data was sifted up one day. The reasoning for the adjusted copy was an assumption that day of the week would be more relevant than the date. <br>

<a name="Initial-Analysis"></a>
<h2 align="center">Data Analysis</h2>

A surface level analysis was conducted for any potential insights. 

<br>
 <p align="center">
<img  width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>

The avarage daily demand was right skewed, posibly due to infrequent events like holidays/sporting events or to the short period of the year people where require heating, it may even be due to the data not featureing the full year or somthing else entirly. 

<p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/AverageNDEachDay2020.png">
 </p>
 
One trend found from Average ND throughout the year was the beginning of spring drop in average ND, considering most of the data is in spring and summer, this could account for the right skew. Another interesting observation is the pattern of one-off low ND followed by a few days of high ND.
 
 
<p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/weekdayWeekendComparison.png">
  </p>  

Although the two data sets looked near-identical the weekdays did have a notably higher upper quartile giving weekdays a greater impact on the right skew. It will be necessary to break the data down into days to find further insight.

 <p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/2019adjVS2019.png">
</p>

The assumption proved correct that the days of the week were more relevant in general. However, It would be interesting to look for dates which the calender aligned set did better, this may highlight other important elements.  

<a name="Feature-selection"></a>
<h3 align="center">Feature Selection</h3>
All variables were correlation and one-way ANOVA tested against the 2020 ND. From the results show below, all but the weekday/weekend variable were shown to have predictive qualities. <br>  <br>
 <p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/cor%26pvalueExcel.png">
</p>
Although both '2019 ND' and '2019 ND Adjusted' were explanatory variables to remove any potential multicollinearity problems only the 2019 Ajustend was used as it had a higher correlation. 
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
The areas highlighted are some of the more noticeable under/over predictions by the model, further investigation into why is needed.
<a name="Summary"></a>
<h2 align="center">Summary</h2>
Overall the MLR model proved fairly accurate, only having an average error of 8%. 
