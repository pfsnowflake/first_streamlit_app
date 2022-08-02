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

# Let's put a pick list here 
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)


