
<h2 align="center"> ESO National Demand Model 📈</h2>

<p >
This project aims to use machine learning to create a predictive model for the UK's national energy demand. The data used in the model include historical national demand information gathered from the National Grid ESO as well as national weather data.  file. 
</p>
<h3 align="center">contents</h3>
<p align="center">
<a  align="center" href="#Data-Gathering">Data Gatherin</a><br>
<a  align="center" href="#Feature-engineering">Feature Engineering</a><br>
<a  align="center" href="#Initial-Analysis">Initial Analysis</a><br>
</p>
<br><br>
<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

For the model to predict the National Demand it first required National Grid data to learn off. This information was gathered from National Grid ESO's data portal in the Demand data group Historic Demand Data set. For simplicity, only the 2020 set was used. The data was into 48, 30 minute periods comprising 1-day information on ND (national Demand). <br>

The second data set gathered was weather data. Gathering any historical information on this proved difficult as such only the London daily average temperature data was added to the model.  This data was scraped from weather.com and cleaned in excel.<br>

To combine the two data sets the ND was averaged for each day and the weather for that day was appended. <br>

<a name="Feature-engineering"></a>
<h2 align="center">Feature engineering</h2>

A python function was created to map each day in the data set to be a weekday given the value 1 or a weekend with the value 0.<br>

<a name="Initial-Analysis"></a>
<h2 align="center">Initial Analysis</h2>


<p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/imgs/probability%20distribution%20of%20National%20Demand.png">
</p>



