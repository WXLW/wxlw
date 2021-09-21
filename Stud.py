#!/usr/bin/env python
# coding: utf-8
from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


model= load_model('Final RPF_Lightgbm Model 20Sep2021')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    st.write("""

    # StudATEML

    
    """)
    st.write("""

    An App For Predicting Shear Resistance of Headed Studs in Steel-Concrete Composite Structures via Auto-Tuning Ensemble Learning Technique

    
    """)
    #st.write("""

    ## ML-based Practical Bond Strength Prediction App For SRC Structures

    #This app predicts the **Bond strength** between H-steel section and concrete!
 
    #""")
#    #st.write('This App Predicts the **Shear Resistance** of Headed Stud connectors in Steel-Concrete Composite Structures!')
    
    from PIL import Image
    image = Image.open('LightGBM.png')

    st.image(image, width=1050)#,use_column_width=False)
    
    st.sidebar.header('User Input Features')
    
    Stud_shank_diameter= st.sidebar.slider('Stud shank diameter, ds (mm) ', 4.75, 31.8, 19.0)

    Stud_height= st.sidebar.slider('Stud height, hs (mm) ', 20, 400, 100)

    Weld_collar_diameter= st.sidebar.slider('Weld collar diameter, dw (mm) ', 7.75, 44.5, 23.0)

    Weld_collar_height= st.sidebar.slider('Weld collar height, hw(mm) ', 1.5, 8.4, 2.0)

    Stud_longitudinal_spacing= st.sidebar.slider('Stud longitudinal spacing , sl (mm) ', 19, 1000, 200)

    Stud_transverse_spacing= st.sidebar.slider('Stud transverse spacing , st (mm) ', 19, 1000, 200)

    Concrete_slab_thickness= st.sidebar.slider('Concrete slab thickness , tc (mm) ', 30, 500, 200)

    Stirrup_ratio= st.sidebar.slider('Stirrup ratio, ' +chr(961)+'sv (%)', 0.0, 3.79, 0.54)

    Stud_tensile_strength= st.sidebar.slider('Stud tensile strength, fsu(MPa)', 372.0, 900.0, 525.0)

    Concrete_cylinder_strength= st.sidebar.slider('Concrete cylinder strength, fcm(MPa)', 13.7, 200.0, 50.0)

    Concrete_elastic_modulus= st.sidebar.slider('Concrete elastic modulus, Ecm(GPa)', 10.4, 53.5, 38.0)

    Stirrup_yield_strength= st.sidebar.slider('Stirrup yield strength, fy(MPa)', 250.0, 613.0, 400.0)

    Concrete_type= st.selectbox('Concrete type',['NSC','LWC','CRC', 'SFRC','HSC','UHPC','CG','ECC'])

    Interface_condition= st.selectbox('Interface condition',['Bond', 'Oiled'])



    input_dict = {'fsuAs': Stud_tensile_strength*1/4*3.141592653*(Stud_shank_diameter**2), 'dwhw': Weld_collar_diameter*Weld_collar_height, 
          'hs/ds' :Stud_height/Stud_shank_diameter, 'tc/ds': Concrete_slab_thickness/Stud_shank_diameter, 'sqrt(Ec*fc)': (Concrete_cylinder_strength*Concrete_elastic_modulus)**0.5,
          'fyrsv':Stirrup_yield_strength*Stirrup_ratio/100,'sl':Stud_longitudinal_spacing,'st':Stud_transverse_spacing,
          'Interface condition':Interface_condition,'Concrete type':Concrete_type, 
                 }
    input_df = pd.DataFrame([input_dict])    
    
    if st.button("Predict"):
       output = predict(model=model, input_df=input_df)
       output = round(output, 1)
       output =  str(output) +'kN'

       st.success('The Shear Resistance of Headed Studs in Concrete slab is  :  {}'.format(output))
    st.info('***Written by Dr. Xianlin Wang,  Department of bridge engineering,  Tongji University,  E-mail:xianlinwang96@gmail.com***')
       
    #output = predict(model=model, input_df=input_df)    
    
    #st.write(output)
        
if __name__ == '__main__':
    run()
