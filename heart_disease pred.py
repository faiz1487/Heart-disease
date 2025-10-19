# -*- coding: utf-8 -*-
from PIL import Image
import cv2
import pickle
import requests
import streamlit as st
from plotly import graph_objs as go
from matplotlib import pyplot as plt
from streamlit_option_menu import option_menu
import pandas as pd

# loading the saved models


st.image('C://Users//hp/Desktop//final project//heart disease//rce_logo.jpg')
heart_disease_model =pickle.load(open('C:/Users/hp/Desktop/final project/heart disease/heart_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          [
                           'Heart Disease Prediction',
                           ],
                          icons=['heart'],
                          default_index=0)

    
# sidebar for navigation
with st.sidebar:
    
     option_menu('project Submitted by',
                          
                          ['Anushka kumari',
                           'Shrestha Arya',
                           'Vinayak sharma',
                           'Faizan kaishar'],
                          icons=['person','person','person','person'],
                          default_index=0)    

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.image("C:/Users/hp/AppData/Local/Programs/Python/Python310/Lib/site-packages/streamlit/static/rce logo.jpg")

    
    st.title('Roorkee College of Engineering') 
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input('Sex')
        
    with col3:
        Chestpain = st.text_input('Chest Pain types')
        
    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')
        
    with col2:
        Cholesterol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        FastingBS= st.text_input('FastingBS')
        
    with col1:
        RestingECG = st.text_input('Resting Electrocardiographic results')
         
    with col2:
        MaxHR= st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        ExerciseAngina = st.text_input('Exercise Induced Angina')
        
    with col1:
        ST_Slope= st.text_input('Slope of the peak exercise ST segment')
        
    with col2:
        Oldpeak= st.text_input('Oldpeak')    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[Age,Sex,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,ST_Slope,Oldpeak]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease :broken_heart::broken_heart::broken_heart:'
        else:
          heart_diagnosis = 'The person does not have any heart disease :sparkling_heart::sparkling_heart::sparkling_heart:'
        to_add = {"Age":[Age],"Sex":[Sex],"Chestpain":[Chestpain],"RestingBP":[RestingBP],"Cholesterol":[Cholesterol],"FastingBS":[FastingBS],"RestingECG":[RestingECG],"MaxHR":[MaxHR],"ExerciseAngina":[ExerciseAngina],"ST_Slope":[ST_Slope],"Oldpeak":[Oldpeak],"heart_prediction":heart_prediction}
        to_add =pd.DataFrame(to_add)
        to_add.to_csv('C:/Users/hp/Desktop/final project/heart disease/heart.csv',mode ='a',header =False,index=False)
        
    st.success(heart_diagnosis)
