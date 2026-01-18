# A comparative analysis of wind speed data in two locations with a view to determining the best site for construction of a new windfarm
In this notebook, I perform a comparative data analysis between two locations: Gurteen in Tipperary and Ballyhaise in Cavan. For the purposes of this assignment, I have imagined myself in the role of a data analyst who has been employed by a wind farm contractor to determine the best of two sites for the construction of a new wind farm. The contractor has two sites in two different locations (Gurteen in Tipperary and Ballyhaise in Cavan), both sitting at approx. 75m above sea level. I analyse historical Met Eireann data for two stations (Gurteen and Athenry, which both sit at approx. 75m above sea level) to determine which of the two locations is best for the construction of a new wind farm.

## Met Eireann Data
For each of the two locations, there is data on wind speeds dating back to 2010. (I downloaded)[https://www.met.ie/climate/available-data/historical-data] the mean monthly data for each station.

## Necessary packages
For this project, you will need to import `pandas` and `prophet`.

## References
Below you will find a list of references for this project, all of which are referenced at relevant points in my Jupyter notebook.

- [Met Eireann Data](https://www.met.ie/climate/available-data/historical-data)
- [Handling missing values](https://www.geeksforgeeks.org/machine-learning/handling-missing-values-machine-learning/)
- [Wind turbine functional ranges](https://businessnorway.com/articles/wind-speed-for-wind-turbines-unlocking-optimal-output)
- [Time forecasting with prophet](https://www.kaggle.com/code/prashant111/tutorial-time-series-forecasting-with-prophet)
