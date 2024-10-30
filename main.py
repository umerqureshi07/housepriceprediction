import streamlit as st
import json
import pickle
import numpy as np 

with open('columns.json','r') as f:
    data=json.load(f)






st.set_page_config(page_title="My App",layout="wide")
st.image("header.jpg",width=1000)
st.title("Welcome to My App")
selected_location=st.selectbox(
    "Select Desired Location",
    data["data_columns"][3:],
)

area=st.text_input("Enter area of the house(in square feet)",value="1000")
bedrooms_bhk=st.text_input("Enter the number of BHK/Bedroom",value="3")
bathrooms=st.text_input("Enter the number of bathroom",value="2")

with open('home_prices_model.pickle','rb') as f:
    model=pickle.load(f)
def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(np.array(data["data_columns"])==selected_location)[0][0]

    x_new=np.zeros(len(data["data_columns"]))
    x_new[0]=sqft
    x_new[1]=bath
    x_new[2]=bhk
    if loc_index>=0:
        x_new[loc_index]=1
    #print(x)

    return model.predict([x_new])[0]



if st.button("start prediction"):
    try:
        area=float(area)
        bedrooms_bhk=int(bedrooms_bhk)
        bathrooms=int(bathrooms)

       
    except ValueError:
        st.warning("please enter valid numbers for all inputs.")
    try:
       predicted_price =predict_price(selected_location,area,bathrooms,bedrooms_bhk)
       st.success(str(round(predicted_price,2))+" (IND Lakh) " + str(round(predicted_price* 3.3,2))+" (PKR Lakh)" )
    except Exception as e:
        st.warning(e)


                                                           
    