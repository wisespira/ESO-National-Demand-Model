
<h2 align="center"> ESO National Demand Model 📈</h2>

<p align="center">
 The aim of this project is to uses machine learning to create a predictive model for the UK's national energy demand. The data used in the model includes historical national demand infomation gathered from the National Grid ESO as well as national weather data. To run use the National Demand Predictor.py file. When selecting features 
</p>
<h3 align="center">contents</h3>

<a href="#Data-Gathering">Content</a>
<!--ts-->
* Obtaining data
   * [Data Gathering](#Data-Gathering)
   * [Feature Engineering](#Feature-engineering)
* [Initial Analysis](#Initial-Analysis)
<!--te-->

<a name="Data-Gathering"></a>
<h2 align="center">Data Gathering</h2>

For the model to predict the National Demand it first required National Grid data to learn off. This infomation was gathered from National Grid ESO's data portal in the Demand data group Historic Demand Data set. For simplistity only the 2020 set was used. The data seem to be stuctured into 48, 30 minit periods comprising 1 days infomtion on ND (national Demand). <br>

The second data set gathered was weather data. There were no free data sourses for the UK avarage so the model was forced to use london daily avarage temperature data scraped from 'weather.com'. <br>

To combine the two data sets the ND was avaraged for each day and the weather for that day was appended. <br>

<a name="Feature-engineering"></a>
<h2 align="center">Feature engineering</h2>

Adding holidays

<a name="Initial-Analysis"></a>
<h2 align="center">Initial Analysis</h2>


<p align="center">
 <img src="https://raw.githubusercontent.com/wisespira/ESO-National-Demand-Model/master/probability%20distribution%20of%20National%20Demand.png">
</p>



