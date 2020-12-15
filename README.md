
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
Tis project uses machine learning to create a predictive model for the UK's national energy demand. The model uses historical ND (national demand) data, gathered from the National Grid ESO, as well as Londons weather data to make its predictions. 
</p>
<h3 align="center">contents</h3>
<p align="center">
<a  href="#Data-Gathering">Data Gathering</a><br>
<a  href="#Data-Engineering">Feature Engineering</a><br>
<a  href="#Initial-Analysis">Data Analysis</a><br>
 <a  href="#Feature-selection">Feature selection</a><br>
<a  href="#Model-Design">Model Design</a><br>
<a  href="#Performance">Performance</a><br>
</p>
<br><br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

The UK's histoical ND was gathered from National Grid ESO's data portal, within the Demand data group (https://data.nationalgrideso.com/demand/historic-demand-data). For simplicity, only the 2020 set was used. The data came split into 48, 30 minute periods which comprised 1-day information on ND. <br>

Gathering large ammounts of historical weather information proved difficult as such only the London daily average temperature data was added. This data was scraped from weather.com and cleaned in excel.<br>

To combine the two data sets the ND was averaged for each day and the weather for that day was appended. <br>
<a name="Data-Engineering"></a>
<h3 align="center">Data Engineering</h3>

A weekday/weekend data was added to the data set by looping through it with a python function appending 1 for weekdays and 0 for weekends.<br>

<a name="Initial-Analysis"></a>
<h2 align="center">Data Analysis</h2>
<p align="center">
 <img width="200" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>
<a name="Feature-selection"></a>
<h3 align="center">Feature Selection</h3>




<a name="Model-Design"></a>
<h2 align="center">Model Design</h2>


<a name="Performance"></a>
<h2 align="center">Performance</h2>


