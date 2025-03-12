import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    # `spec` determines your default view. If no `.json` specified, the default view will be blank
    # `spec_io_mode=` determines how you interact with `spec`
        # "r" - to read the default views;
        # "rw" - to read and overwrite default views.
    html = get_streamlit_html(df, use_kernel_calc=True, spec="./lec17/spec/geo_vis.json", spec_io_mode="r")
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    df = pd.read_csv("./lec17/data/Significant Earthquake_Dataset_1900_2023.csv")
    df["Time"] = pd.to_datetime(df["Time"]).dt.strftime('%Y-%m-%d %H:%M:%S')

    return df

st.set_page_config(
    page_title="Earthquake Visualization with pygwalker",
    layout="wide"
)
init_streamlit_comm()

st.title("Earthquake Visualization (1900-2023) with pygwalker")
st.markdown("""Use [pygwalker](https://github.com/kanaries/pygwalker) for interactive visualization of geospatial data. More docs [here](https://docs.kanaries.net/pygwalker).)""")

df = get_df()

components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)

st.divider()

""" # Source Code
```python
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

# When using `use_kernel_calc=True`, you should cache your pygwalker html, if you don't want your memory to explode
@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    # `spec` determines your default view. If no `.json` specified, the default view will be blank
    # `spec_io_mode=` determines how you interact with `spec`
        # "r" - to read the default views;
        # "rw" - to read and overwrite default views.
    html = get_streamlit_html(df, use_kernel_calc=True, spec="./streamlit/lec17/data/geo_vis.json", spec_io_mode="r") # spec determines your default
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    df = pd.read_csv("./streamlit/lec17/data/Significant Earthquake_Dataset_1900_2023.csv")
    df["Time"] = pd.to_datetime(df["Time"]).dt.strftime('%Y-%m-%d %H:%M:%S')

    return df

st.set_page_config(
    page_title="Earthquake Visualization with pygwalker",
    layout="wide"
)
init_streamlit_comm()

st.title("Earthquake Visualization (1900-2023) with pygwalker")
Use [pygwalker](https://github.com/kanaries/pygwalker) for interactive visualization of geospatial data. More docs [here](https://docs.kanaries.net/pygwalker).)

df = get_df()

components.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)
```
"""