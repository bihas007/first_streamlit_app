print('Hello Bihas')
import streamlit as st
import pandas as pd
import requests as r

st.title('My Parents New Healthy Diner')
st.header('Breakfast Menu')
   
st.text('🥣 Omega 3 & Blueberry oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# st.multiselect("Pick some fruits: ",list(my_fruit_list.index))
# st.dataframe(my_fruit_list)

fruits_selected = st.multiselect("Pick some fruits: ",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)
st.header('Fruityvice Fruit advice')
fruityvice_response = r.get("https://fruityvice.com/api/fruit/watermelon")
# st.text(fruityvice_response.json())


fruityvice_normalized= pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)
