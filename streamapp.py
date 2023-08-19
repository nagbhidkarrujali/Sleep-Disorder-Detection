
# Import the Libraries
import streamlit as st 
import pandas as pd
import numpy as np
import joblib

# Load the pickel file 
sleepdisorder = joblib.load('Sleep_Disorder_Prediction.pkl')

# Function to take inputs
def predict_disorder(gender,
                     age,
                     occupation,
                     sleepduration,
                     qualityofsleep,
                     physicalactivitylevel,
                     stresslevel,
                     bmicategory,
                     heartrate,
                     dailysteps,
                     systolic,
                     diastolic):
    
    inputs_dict = {'Gender':gender,                              
                    'Age': float(age),                            
                    'Occupation' :occupation,        
                    'Sleep Duration':float(sleepduration),                 
                    'Quality of Sleep':float(qualityofsleep),               
                    'Physical Activity Level':float(physicalactivitylevel),        
                    'Stress Level':float(stresslevel),                     
                    'BMI Category':bmicategory,                    
                    'Heart Rate':float(heartrate),                         
                    'Daily Steps':float(dailysteps),                                        
                    'Systolic':float(systolic),                         
                    'Diastolic':float(diastolic)}
    
    df = pd.DataFrame(inputs_dict, index = [0])
    
    disorder_pred = sleepdisorder.predict(df)[0]
    return disorder_pred


#function to define the app_layout
def app_layout():

    st.title('Sleep Disorder Prediction')
    st.header('Enter Your Medical detail:') 

    ## Creating the user input fields

    gender = st.radio('Gender:', 
                        ['Male', 'Female'], 
                        horizontal=True)

    age = st.number_input('Age Of Person:', 
                          min_value=15,
                          max_value=70, 
                          value=15)
    
    occupation = st.selectbox('Occupation:',
                                ['Nurse' ,'Doctor' ,'Engineer' ,
                                'Lawyer' ,'Teacher' ,'Accountant' ,
                                'Salesperson' ,'Software Engineer' ,
                                'Scientist' ,'Sales Representative','Manager' ])

    sleepduration = st.number_input('Sleep Duration Time : Number Of hours the person sleeps per day ',
                                    min_value=3.0, 
                                    max_value=24.0, 
                                    value=3.0)
    
    qualityofsleep = st.number_input('Sleep Quality time: A subjective rating of the quality of sleep, ranging from 1 to 10.',
                                    min_value=1, 
                                    max_value=10, 
                                    value=1)
    
    physicalactivitylevel = st.number_input('Physical Activity Level : The number of minutes the person engages in physical activity daily.')

    stresslevel = st.number_input('Stress Level : A subjective rating of the stress level experienced by the person, ranging from 1 to 10. ')

    bmicategory = st.radio('Body Mass Index Category :',
                            ['Overweight','Normal','Obese'],
                            horizontal=True)
        
    heartrate = st.number_input('Heart Rate : The resting heart rate of the person in beats per minute.', 
                                min_value=50, 
                                max_value=100, 
                                value=50)

    dailysteps = st.number_input('Daily Steps : The number of steps the person takes per day.')

    systolic = st.number_input('Systolic BP : ')

    diastolic = st.number_input('Diastolic BP : ')

    if st.button('Predict Health'):
        disorder = predict_disorder(gender,
                                    age,
                                    occupation,
                                    sleepduration,
                                    qualityofsleep,
                                    physicalactivitylevel,
                                    stresslevel,
                                    bmicategory,
                                    heartrate,
                                    dailysteps,
                                    systolic,
                                    diastolic)
        st.success(f'The Personr is havong {(disorder)}')
        
        if (disorder=="none"):
               st.markdown("None : The individual does not exhibit any specific sleep disorder.")
        elif (disorder=="Isomania"):
               st.markdown("Insomnia : The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.")
        elif (disorder=="Sleep Apnea"):
               st.markdown("Sleep Apnea : The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.")

if __name__=='__main__':
  app_layout()
