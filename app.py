import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

#Find the largest among the 3 given numbers(value greater than the other two).

st.write("""
# Largest Number finding App

This app finds the largest of the 3 numbers given
""")
#Get Input


st.header('User Input Parameters')

def user_input_numbers():
    num1 = st.number_input("First Number",min_value=0,max_value=20000)
    num2 = st.number_input("Second Number",min_value=0,max_value=20000)
    num3 = st.number_input("Third Number",min_value=0,max_value=20000)
    
    numbers = [num1,num2,num3]
    return numbers

nums = user_input_numbers()

st.write("The largest of the 3 numbers given is:")
st.write(max(nums))

