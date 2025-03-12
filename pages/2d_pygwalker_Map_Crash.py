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
    html = get_streamlit_html(df, use_kernel_calc=True, spec_io_mode="r", spec="./lec17/spec/crash_config.json")
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    crash = pd.read_csv("./lec17/data/accident.csv", encoding = "ISO-8859-1")
    vehicle = pd.read_csv("./lec17/data/vehicle.csv", encoding = "ISO-8859-1")
    person = pd.read_csv("./lec17/data/person.csv", encoding = "ISO-8859-1")

    return crash, vehicle, person

st.set_page_config(
    page_title="Crash Data with pygwalker",
    layout="wide"
)
init_streamlit_comm()

st.title("Crash Data with pygwalker")
st.markdown("""Use [pygwalker](https://github.com/kanaries/pygwalker) for interactive visualization of geospatial data. More docs [here](https://docs.kanaries.net/pygwalker).
Here we have 1-year of `crash`,`vehicle`, and `pedestrian` data joined with two left outer joins. Fatality Analysis and Reporting (FARS) data in Washington [data dictionary](https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813556). 
Let's try to make some queries and save to our `streamlit\lec17\spec\crash_config.json` file. We will calculate a few fields, modify our charts, then export the code to the config file to save for later.""")

@st.cache_data
def get_df() -> pd.DataFrame:
    crash = pd.read_csv("./lec17/data/accident.csv", encoding = "ISO-8859-1")
    vehicle = pd.read_csv("./lec17/data/vehicle.csv", encoding = "ISO-8859-1")
    person = pd.read_csv("./lec17/data/person.csv", encoding = "ISO-8859-1")

    return crash, vehicle, person

crash, vehicle, person = get_df()

joined = crash.merge(vehicle, on="ST_CASE").merge(person, on="ST_CASE")

df_select = st.selectbox("Select a dataframe:", ["crash", "vehicle", "person", "joined"], index=3)
df = eval(df_select)
st.write("Crash, Vehicle, and Person joined on `ST_CASE`",df.head())

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