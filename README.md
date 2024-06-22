# Stock_webpage001
The Stock Price Prediction Web App leveraging machine learning with   
Python is a groundbreaking platform designed to empower investors, traders, 
and financial analysts with accurate and timely insights for informed decision
making in stock markets. Through a user-friendly interface, users can input 
stock symbols, customize prediction parameters, and access real-time 
predictions based on historical data, technical indicators, and market sentiment 
analysis. Utilizing Python's powerful machine learning libraries such as 
TensorFlow, coupled with Flask for web development, the app seamlessly 
integrates data retrieval, preprocessing, model training, and prediction 
generation processes, employing LSTM or RNN models to capture intricate 
patterns and dependencies within stock price data. With customizable features, 
interactive visualizations, and stringent security measures, this web app 
revolutionizes stock market analysis, empowering users to optimize investment 
strategies and navigate financial markets confidently in a competitive 
landscape.

**#How it works**
We had divided our Data set into a 80:20 ratio where 80% of the data was used to train the model and 20% of the data was used to test the data. This data set was spread over a period of ten years (2020 to 2023). The Epoch values we used while training our data set were 50. We had only trained and tested our model for predicting the closing price of the selected stock. 4 graphs were plotted which included,
1.	Price vs. moving average 50

2.	Price vs. moving average 50 vs. moving average 100

3.	Price vs. moving average 100 vs. moving average 200

4.	Original price vs. predicted price.

The data values were scaled between 0 to 1 using MinMax Scaler. For 100 days moving average, the closing price of our selected stock for the 1st 100 hundred days was stored x_train (while training) and x_test (while testing). The closing price of the selected stock for 101st day is predicted form these initial 100 day values (of x_train and x_test) and is then stored in y_train (while training) and y_test (while testing).
To predict the further values, the 1st value from the initial data set is removed and the previously predicted value is appended to the data set. The average means square value for our predictions was found out to be approximately 0.0025 We tested our model for the closing stock prices of Tesla and State bank of India stocks (The respective graphs are present below.) Tesla (TSLA).
