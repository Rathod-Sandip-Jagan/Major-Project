Week 4: Implementation 
3. Initial Model Implementation 
Selected Models for Baseline Testing: 
SARIMA: 
Used for benchmarking traditional time-series forecasting. 
Observed limitations in handling sudden market shocks or weather variations. 
Linear Regression: 
Used as a basic multivariate model combining price, weather, and seasonal indicators. 
Random Forest Regressor: 
Initial ML model with promising results. 
Able to capture nonlinear patterns. 
Feature importance analysis revealed weather and lag price as key predictors.
Evaluation Metrics Introduced 
To assess model performance: 
MAE (Mean Absolute Error) 
RMSE (Root Mean Square Error) 
MAPE (Mean Absolute Percentage Error) 
Mean Absolute Error: 0.7647499999999998
Mean Squared Error: 1.1132983749999998
Root Mean Squared Error: 1.0551295536568008
Baseline results showed: 
Traditional models like SARIMA were okay for smooth trends but struggled withvolatility. 
Random Forest showed better handling of fluctuations. 
Challenges 
Difficulty in aligning weather data granularity with price data (daily vs. weekly). 
High variability in unstructured market intelligence data. 
SARIMA models are too rigid for multi-feature integration.