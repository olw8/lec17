import streamlit as st 

st.title("App model summary")

st.markdown("Now that you know a little more about all the individual pieces, let's close the loop and review how it works together:")

st.image('https://docs.streamlit.io/images/app_model.png')
st.markdown("""
1. Streamlit apps are Python scripts that run from top to bottom.
2. Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.
3. As the script executes, Streamlit draws its output live in a browser.
4. Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the browser.
5. The output value of that widget matches the new value during that rerun.
6. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast.
    + `st.cahce_resource` for database connections
    + `st.cache_data` for expensive computations
7. Session State lets you save information that persists between reruns when you need more than a simple widget.
    + `st.session_state` for user input
8. Streamlit apps can contain multiple pages, which are defined in separate .py files in a pages folder.
    + See `streamlit/lec17/pages/` for the stored files such as this one.
    + They are ordered based on lexiographical order.
9. Streamlit apps can be shared by running `streamlit run app.py` in the terminal and sharing the URL.
""")