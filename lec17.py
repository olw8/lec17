import streamlit as st

st.markdown("""# lec17 More Advanced Streamlit
CEE412/CET522 | lec17 | Ollie Wiesner

Materials were made possible by [Streamlit](https://streamlit.io/).""")

# code for the sidebar
st.sidebar.title("More Advanced Streamlit")

st.sidebar.markdown("""This is the main page detailing more advanced featuers about streamlit!

Much of this is written in Markdown, which we saw in our `Jupyter Notebook`. A `#` denotes the level of heading. Read more about Markdown syntax: [Basic](https://www.markdownguide.org/basic-syntax/) or [Advanced](https://www.markdownguide.org/extended-syntax/).

We can also put `sidebar` into our commands to add data here. e.g. use `st.sidebar.title` 
to add a sidebar title.""")

left, right = st.columns(2)

with left:
    st.markdown("""## Agenda
Today's lecture, we will cover:
+ SQL Server Connections
    + `pyobdc`
    + `sqlalchemy`
    + `pymssql`
+ `pygwalker`
    + Data Dashboard + Mapping Data
+ `streamlit-folium`
+ Caching
+ HTML
+ Computer Vision Page
                """)

with right:
    st.markdown("""## Streamlit Resources
Here are a few resources you can use:
+ [Streamlit documentation](https://docs.streamlit.io/)
+ [Streamlit API reference (help section)](https://docs.streamlit.io/develop/api-reference)
+ [Components: third-party modules](https://streamlit.io/components)
+ [Knowledge base](https://docs.streamlit.io/knowledge-base)""")