import streamlit as st 
import pickle

model=pickle.load(open('model.pkl','rb'))

st.title('Salary prediction system')

yeo=st.text_input("enter year of experience: ")

if st.button("predict"):
    yoe=float(yeo)
    data=[[yoe]]
    result=model.predict(data)
    st.success(result)