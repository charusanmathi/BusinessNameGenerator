import streamlit as st
import langchain_helper

# st.title("Restaurant name generator")
#
# cuisine = st.sidebar.selectbox("Pick a Cuisine",
#                                ("Indian", "Italian", "American", "Arabic", "IndoChinese", "Mexican",
#                                 "Japanese", "Korean", "French", "Thai", "Filipino"))


st.set_page_config(page_title="Restaurant Name Generator", page_icon=":fork_and_knife:")
st.title("Restaurant Name Generator")
st.sidebar.header("Select Cuisine")
cuisine = st.sidebar.selectbox("Pick a Cuisine",
                               ("Indian", "Italian", "American", "Arabic", "Indo-Chinese",
                                "Mexican", "Japanese", "Korean", "French", "Thai", "Filipino"))

if cuisine:
    response = langchain_helper.get_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("****Menu Items****")

    for item in menu_items:
        st.write(item)


