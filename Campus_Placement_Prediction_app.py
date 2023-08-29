import streamlit as st
import pandas as pd
import pickle
model = pickle.load(open('campus_placement.sav', 'rb'))


def predict_placement(input_data):
    # Process the input data and make predictions using your model
    prediction = model.predict(input_data)
    return prediction

def main():
    
    st.set_page_config(page_title="Campus Placement Prediction App",layout="wide")
    st.markdown("<h1 style='text-align: center; color: blue;'>CAMPUS PLACEMENT PREDICTION</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: black;'>Enter the required details for prediction:</h3>", unsafe_allow_html=True)
    
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    #</style> """, unsafe_allow_html=True)
    # Create input fields for the required features
    
    gender = st.selectbox('gender', ['Male', 'Female'])
    
    col1,col2 =st.columns(2)
    SSC_Board = col1.selectbox('SSC_Board',['Others','Central'])
    SSC_Percentage = col2.text_input('SSC_Percentage')
    HSC_Board = col1.selectbox('HSC_Board',['Others','Central'])
    HSC_Specialization = col2.selectbox('HSC_Specialization',['Commerce', 'Science', 'Arts'])
    
    HSC_Percentage = st.text_input('HSC_Percentage')
    
    col1,col2 =st.columns(2)
    Degree_Field_of_Study = col1.selectbox('Degree_Field_of_Study', ['Sci&Tech', 'Comm&Mgmt', 'Others'])
    Degree_Percentage = col2.text_input('Degree_Percentage')
    specialisation = col1.selectbox('specialisation', [ 'Mkt&HR','Mkt&Fin'])
    MBA_Percentage = col2.text_input('MBA_Percentage')
    
    Work_Experience = st.selectbox('Work_Experience', ['No','Yes'])
    Employability_Test_Percentage = st.text_input('Employability_Test_Percentage')

    # Convert input values to the required format
    if gender == 'Male':
        gender = 0 
    else:
        gender = 1
    if SSC_Board == 'Others':
        SSC_Board = 1
    else:
        SSC_Board = 0
    if HSC_Board == 'Others':
        HSC_Board = 1
    else:
        HSC_Board= 0
    if HSC_Specialization== 'Arts':
        HSC_Specialization = 0 
    elif HSC_Specialization == 'Commerce':
        HSC_Specialization=1 
    else:
        HSC_Specialization=2
    if Degree_Field_of_Study == 'Sci&Tech':
        Degree_Field_of_Study = 2
    elif Degree_Field_of_Study == 'Comm&Mgmt':
        Degree_Field_of_Study=0  
    else:
        Degree_Field_of_Study=1
    if Work_Experience =='No':
        Work_Experience = 0 
    else:
        Work_Experience =1
    if specialisation=='Mkt&Fin':
        specialisation=0 
    else:
        specialisation=1


    # Create a dictionary of input values
    input_data = {
        'gender': gender,
        'SSC_Percentage': SSC_Percentage,
        'SSC_Board': SSC_Board,
        'HSC_Percentage': HSC_Percentage,
        'HSC_Board': HSC_Board,
        'HSC_Specialization': HSC_Specialization,
        'Degree_Percentage': Degree_Percentage,
        'Degree_Field_of_Study': Degree_Field_of_Study,
        'Work_Experience': Work_Experience,
        'Employability_Test_Percentage': Employability_Test_Percentage,
        'specialisation': specialisation,
        'MBA_Percentage': MBA_Percentage
    }


    # Convert input data to a DataFrame
    input_df = pd.DataFrame([input_data])
    # Center the content
    col1, col2, col3 = st.columns(3)

    # Add empty columns for centering
    col1.write("")
    col2.write("")
    # Add button in the center column with increased width
    with col2:
        # Apply CSS styling to increase button width
        button_style = "<style>.stButton button {background-color: black;color: white;width: 300px;}</style>"
        st.markdown(button_style, unsafe_allow_html=True)
        if st.button('Predict'):
            prediction = predict_placement(input_df)
            # Display the predicted result
            #st.write('Predicted Placement:', prediction[0])
            if prediction[0]==1:
                # Apply styling to the output message
                styled_message = "<p style='color: green; font-size: 20px;'>CANDIDATE SUCCESSFULLY PLACED</p>"
                st.markdown(styled_message, unsafe_allow_html=True)
                st.balloons()
            else:
                result=0
                # Apply styling to the output message
                styled_message = "<p style='color: red; font-size: 20px;'>CANDIDATE NOT LIKELY TO BE PLACED</p>"
                st.markdown(styled_message, unsafe_allow_html=True)
        
                

if __name__ == '__main__':
    main()
