import numpy as np 
import pandas as pd 
import yfinance as yf 
from keras.models import load_model 
import streamlit as st 
import matplotlib.pyplot as plt 
 
model = load_model('C:\Angular\stock.py') 
 
st.header('Stock Market Predictor') 
 
stock =st.text_input('Enter Stock Symnbol', 'GOOG') 
start = '2020-01-01' 
end = '2022-12-31' 
 
data = yf.download(stock, start ,end) 
 
st.subheader('Stock Data') 
st.write(data) 
 .
.
.
..
.
oops... its just the half of the code 
if any one want the remaining code you have to pay 1500 if your are intersted,
please feel free to conatct this number
6363002733--Sahana 
or whatsapp me
for remaning code+report+ppt
i will definitely help you 
