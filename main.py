
import streamlit as st
import pickle

def main():
    
    pickle_in = open("D:/datasets/model/classifier.pkl","rb")
    classifier=pickle.load(pickle_in)



    hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    st.title("Depression Measure")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">HealthCare Workers Depression Measure App</h2>
    </div>
    """
    output = []
    # st.markdown(html_temp, unsafe_allow_html=True)
    # name = st.text_input("Enter Your Name Here","type here")
    Gender = st.selectbox('Select your Gender', ['', 'Female', 'Male'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Age = st.selectbox('Select your Age', ['', '20-30', '30-40','40-50','50-60', '60 and above'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Education = st.selectbox('Select Degree type', ['', 'Graduate', 'High_school','Post graduate'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Marital_status = st.selectbox('Select Marital Status', ['', 'Married', 'Unmarried'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Economical_cond = st.selectbox('About Economical condition during Covid-19', ['', 'Satisfied', 'Unsatisfied'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Occupation  = st.selectbox('Select your Occupation', ['', 'Doctor', 'Management', 'Staff'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Excitement = st.selectbox('Were you excited about your work ?', ['', 'No', 'Yes'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Cheerful = st.selectbox('Work-balance was satisfied', ['', 'No', 'Yes'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Satisfaction = st.selectbox('Satisfied about the work hour', ['', 'No', 'Yes'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Obsessed = st.selectbox('Did you enjoy your  Covid-19 work', ['', 'No', 'Yes'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    Anxiety = st.selectbox('Presence of anxiety', ['', 'No', 'Yes'],
                            format_func=lambda x: 'Select one' if x == '' else x)

    # output.extend([Gender,Age,Education,Marital_status,Economical_cond,Occupation,Excitement,Cheerful,Satisfaction,Obsessed,Anxiety])
    if Gender == 'Female':
        output.append(0)
    elif Gender == 'Male':
        output.append(1)

    if Age == '20-30':
        output.append(0)
    elif Age == '30-40':
        output.append(1)
    elif Age == '40-50':
        output.append(2)
    elif Age == '50-60':
        output.append(3)
    elif Age == '60 and above':
        output.append(4)

    if Education == 'Graduate':
        output.append(0)
    elif Education == 'High_school':
        output.append(1)
    elif Education == 'Post graduate':
        output.append(2)

    if Marital_status == 'Married':
        output.append(0)
    elif Marital_status == 'Unmarried':
        output.append(1)

    if Economical_cond == 'Satisfied':
        output.append(0)
    elif Economical_cond == 'Unsatisfied':
        output.append(1)

    if Occupation == 'Doctor':
        output.append(0)
    elif Occupation == 'Management':
        output.append(1)
    elif Occupation == 'Staff':
        output.append(1)

    if Excitement == 'No':
        output.append(0)
    elif Excitement == 'Yes':
        output.append(1)

    if Cheerful == 'No':
        output.append(0)
    elif Cheerful == 'Yes':
        output.append(1)

    if Satisfaction == 'No':
        output.append(0)
    elif Satisfaction == 'Yes':
        output.append(1)

    if Obsessed == 'No':
        output.append(0)
    elif Obsessed == 'Yes':
        output.append(1)

    if Anxiety == 'No':
        output.append(0)
    elif Anxiety == 'Yes':
        output.append(1)

    press = st.button("Submit")

    if press and len(output) == 11:
        pred = classifier.predict([output])
        print(output)
        if (pred[0] == 1):
            st.write('Depressed')
        else:
            st.write('Not Depressed')
            st.balloons()

if __name__== '__main__':  
    main() 

