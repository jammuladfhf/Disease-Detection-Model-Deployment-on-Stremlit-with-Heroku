# -*- coding: utf-8 -*-
"""
Date : 8-Aug-2022

@author: Narender Jammula
"""
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#loading saved models

diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))

heart_diseas_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


#sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                            ['Diabeties Prediction', 
                             'Heart Disease Prediction',
                             'Parkinsons Prediction'],
                            icons = ['bandaid', 'activity', 'Lungs fill'],
                            default_index=0)
    
# Diabetics predction page

if (selected == 'Diabeties Prediction'):
    
    st.title('Diabetes Prediction Using ML')
        
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
        
    #code for prediction
    diab_diagnosis = ''
    
        #creating button for prediction
    if st.button('Diabetes Test Results'):
        
        diab_predicition = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_predicition[0]==1:
            diab_diagnosis = 'The Person is Diabetic'
            
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
                 
    st.success(diab_diagnosis)

if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction Using ML')
    
    
    
if (selected == 'Parkinsons Prediction'):
    
    st.title('Parkinsons Prediction Using ML')
    
