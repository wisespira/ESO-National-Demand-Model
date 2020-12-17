
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
Tis project uses machine learning to create a predictive model for England and Wales national energy demand. The model uses historical ND (national demand) data gathered from the National Grid ESO, as well as Londons weather data to make its predictions. 
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
</p>
<br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

England and Wales histoical ND was gathered from National Grid ESO's data portal (https://data.nationalgrideso.com/demand/historic-demand-data). For simplicity, only the 2019 and 2020 set was used. The data came split into 48, 30 minute periods which comprised 1-days information on ND. <br>

Gathering large ammounts of historical weather information proved difficult as such only the London daily average temperature data was added. This data was scraped from 'The Weather Channel' (https://weather.com/en-GB/weather/monthly/) and then cleaned in excel (see 'ESO and Weather Data/data from weather.com.xlsx' ).<br>

To combine the two data sets the ND was averaged for each day then the weather data was joined. <br>
<a name="Data-Engineering"></a>
<h3 align="center">Data Engineering</h3>

Weekday/weekend data was added to the data set with a python function by looping through the set appending 1 for weekdays and 0 for weekends. An ajusted copy of the 2019 data was also added inwich all data was sifted up one day to account for the day of the week shift created by the year change.<br>

<a name="Initial-Analysis"></a>
<h2 align="center">Data Analysis</h2>
<p align="center">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/AverageNDEachDay2020.png">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/weekdayWeekendComparison.png">
<img width="700" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/2019adjVS2019.png">


</p>
<a name="Feature-selection"></a>
<h3 align="center">Feature Selection</h3>
All veriables were corrilation and one-way ANOVA tested against the 2020 ND. From the results show below, all but the weelday/weekend veriable were shown to have predictive qualities. <br>  <br>
 <p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/cor%26pvalueExcel.png">
</p>
Although both '2019 ND' and '2019 ND Ajusted' were explanatory variables to remove any potential multicollinearity problems only the 2019 Ajustend was used as it had the lowest p-value. 
<a name="Model-Design"></a>
<h2 align="center">Model Design</h2>
<a name="Preprocessing"></a>
<h3 align="center">Preprocessing</h3>

<a name="Performance"></a>
<h2 align="center">Performance</h2>


