
<h2 align="center">National Demand Model 📈</h2>

<p align="center">
This project aims to use machine learning to create a predictive model for the UK's national energy demand. The data used in the model include historical national demand information gathered from the National Grid ESO as well as Londons weather data. 
</p>
<h3 align="center">contents</h3>
<p align="center">
<a  href="#Data-Gathering">Data Gathering</a><br>
<a   href="#Feature-engineering">Feature Engineering</a><br>
<a  href="#Initial-Analysis">Analysis</a><br>
</p>
<br><br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

The UK's histoical National energy demand was gathered from National Grid ESO's data portal, within the Demand data group (https://data.nationalgrideso.com/demand/historic-demand-data). For simplicity, only the 2020 set was used. The data came split into 48, 30 minute periods which comprised 1-day information on ND (national Demand). <br>

The second data set gathered was weather data. Gathering any historical information on this proved difficult as such only the London daily average temperature data was added to the model. This data was scraped from weather.com and cleaned in excel.<br>

To combine the two data sets the ND was averaged for each day and the weather for that day was appended. <br>

<a name="Feature-engineering"></a>
<h2 align="center">Feature engineering</h2>

A python function was used to map each day in the data set as a weekday, given the value 1, or a weekend with the value 0.<br>

<a name="Initial-Analysis"></a>
<h2 align="center">Initial Analysis</h2>


<p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>



