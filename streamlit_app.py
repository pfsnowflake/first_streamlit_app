import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfest Menu')
streamlit.title('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.title('🥗 Kale, Spinach & Rocket Smoothie ')
streamlit.title('🐔Hard-Boiled Free-Range Egg')
streamlit.title('🥑🍞 Avocado Toast')
streamlit.title('🍌🍓 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here 
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to disply fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Take json verson of response and Normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Format response
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The Fruit load list contains:")
streamlit.text(my_data_row)
