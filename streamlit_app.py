# print('Hello Bihas')
import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector

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
# New api to dispaly api response
st.header('Fruityvice Fruit Advice!!')
# New api to dispaly api response
def get_fruity_vice_data(this_fruit_choice):
    fruityvice_response = r.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruityvice_normalized= pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized




try:
    fruit_choice = st.text_input('What fruit would you like information about?',)
    if not fruit_choice:
        st.error('Please select a fruit to get information')
    else:
        back_from_function = get_fruity_vice_data(fruit_choice)
        st.dataframe(back_from_function)

        # st.write('The user entered ', fruit_choice)
except URLError as e:
    st.error()

        
    
# st.text(fruityvice_response.json())



st.stop()


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
# st.text("Hello from Snowflake:")
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add?','Jackfruit')
st.write('Thanks for adding ',add_my_fruit)

# not work properly but go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
