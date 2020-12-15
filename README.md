
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
This project aims to use machine learning to create a predictive model for the UK's national energy demand. The model uses historical ND (national demand) data gathered from the National Grid ESO as well as Londons weather data. 
</p>
<h3 align="center">contents</h3>
<p align="center">
<a  href="#Data-Gathering">Data Gathering</a><br>
<a  href="#Initial-Analysis">Analysis</a><br>
</p>
<br><br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

The UK's histoical ND was gathered from National Grid ESO's data portal, within the Demand data group (https://data.nationalgrideso.com/demand/historic-demand-data). For simplicity, only the 2020 set was used. The data came split into 48, 30 minute periods which comprised 1-day information on ND. <br>

Gathering large ammounts of historical weather information proved difficult as such only the London daily average temperature data was added. This data was scraped from weather.com and cleaned in excel.<br>

To combine the two data sets the ND was averaged for each day and the weather for that day was appended. <br>
<h3 align="center">Data Engineering</h3>

A weekday/weekend data was added to the data set by looping through it with a python function appending 1 for weekdays and 0 for weekends.<br>

<a name="Initial-Analysis"></a>
<h2 align="center">Analysis</h2>
<h3 align="center">Datas Description</h3>

<h3 align="center">Feature selection</h3>


<p align="center">
 <img width="200" src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>



