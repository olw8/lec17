import streamlit as st
import numpy as np
import pandas as pd

st.title("Cache")
st.sidebar.markdown("""# Cache
To make apps efficient, Streamlit only recomputes whatever is necessary to update the UI.
+ The decorator `@st.cache_data` marks function
+ New cache primitives that are easier to use and much faster are being developed
+ The Streamlit cache allows your app to execute quickly even when loading data from the web, manipulating large datasets, or performing expensive computations.

[Click here for more information on Caches](https://docs.streamlit.io/get-started/fundamentals/advanced-concepts)""")

st.markdown("""caching helps improve the processing power of streamlit:
```python
import streamlit as st

@st.cache_data  # 👈 This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    return the_output
```
What does it cache?
+ The input parameters that you called the function with
+ The value of any external variable used in the function
+ The body of the function
+ The body of any function used inside the cached function

Everytime the cached function is called, `Streamlit` checks these four things.

If this is the first time `Streamlit` has seen these four components
+ with these exact values and 
+ in this exact combination and order, 

it runs the function and stores the result in a local cache. 

Then, next time the cached function is called, if none of these components changed, Streamlit will skip executing the function altogether and, instead, 
return the output previously stored in the cache.


There are two choices when caching:
+ `st.cache_data` is recommended for returning data or a serializable data object (e.g. str, int, float, DataFrame, dict, list). 
    + It creates a new copy of the data at each function call, making it safe against mutations and race conditions. 
    + Use this in most cases. If it fails, try `st.cache_resource`.
+ `st.cache_resource` is recommended for global resources like your SQL server information or ML models or unserializable objects that you don\'t want to load multiple times. 
    + It returns the cached object itself, which is shared across all reruns and sessions without copying or duplication. If you mutate an object that is cached using `st.cache_resource`, 
    that mutation will exist across all reruns and sessions.

<img src="https://docs.streamlit.io/images/caching-high-level-diagram.png" width=800>
            
Here's an example:
""",unsafe_allow_html=True)

with st.echo():
    import streamlit as st
    import pandas as pd

    @st.cache_data
    def load_metadata():
        DATA_URL = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz"
        return pd.read_csv(DATA_URL, nrows=100000)

    @st.cache_data
    def create_summary(metadata, summary_type):
        one_hot_encoded = pd.get_dummies(metadata[["frame", "label"]], columns=["label"])
        return getattr(one_hot_encoded.groupby(["frame"]), summary_type)()


    # Piping one st.cache function into another forms a computation DAG.
    summary_type = st.selectbox("Type of summary:", ["sum", "any"])
    metadata = load_metadata()
    summary = create_summary(metadata, summary_type)
    
    # define left and right columns
    left, right = st.columns(2)
    
with left:
    st.write('## Metadata', metadata)

with right:
    st.write('## Summary', summary)