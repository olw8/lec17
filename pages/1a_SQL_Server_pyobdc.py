import streamlit as st
import pyodbc
import pandas as pd

st.markdown("""# Accessing SQL Server through Streamlit using `pyodbc`

In lecture, we covered three different ways to access the SQL server through `python`. Here, we will demo how to use `pyodbc`.            

## Establish Connection Parameters:""")

with st.echo():
    dsn = st.text_input("Enter your Data Source Name (DSN) for `pyobdc 18`:",placeholder="DSN")
    username = st.text_input("Enter your username:",placeholder="Username")
    password = st.text_input("Enter a password:", type="password",placeholder="Password")
    database = st.text_input("Enter your SQL Server database:", placeholder="Database name",value="CEE412_CET522_W25")

st.markdown("""### Initialize connection with `@st.cache_resource`
We can cache our query connection to save for later""")

"""
```python
@st.cache_resource # insert this before the function below
```"""
with st.echo():
    # Uses st.cache_resource to only run once.
    @st.cache_resource
    def init_connection():
        return pyodbc.connect(
            f"DSN={dsn};UID={username};PWD={password}"
        )

    if len(password) > 0:
        st.write('Password has been entered, attempting to connect...')
        cnxn = init_connection()
        cursor = cnxn.cursor()
        st.write("Connected to DSN: {} via username: {}".format(dsn, username))
    else:
        st.write("Please enter Password before you continue")

st.markdown("""### Define query function within `@st.cache_data`:
Uses `st.cache_data` to only rerun when the query changes or after 10 min.""")

"""
```python
@st.cache_data(ttl=600) # insert this before the function below
```"""

with st.echo():
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def run_query(query):
        with cursor:
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            return columns, cursor.fetchall()

st.divider()

st.markdown("## Running a single query with `pyodbc`:")

with st.echo():
    if len(password) > 0: # pauses code if no password specified
        columns, rows = run_query(f"SELECT * from [{database}].[dbo].[E1_Countries];")

        # Converting the results to a DataFrame
        data = [dict(zip(columns, row)) for row in rows]
        df = pd.DataFrame(data)

        # Print results.
        st.write(df.head())

st.divider()
st.markdown("""## Specify which Table with Widgets
We've established the connection, now let's create parameters to feed into our query:
            
First, we can create a drop down to select the table and number of rows to display""")
with st.echo():
    table = st.selectbox("Which table would you like to connect to?",
        ("E1_CEOs","E1_Countries","E1_Companies"))
with st.echo():
    n_rows = st.slider("Select the number of rows to display",1,25)

st.markdown("""### Re-Run a Query with Widgets
Now, we can use the Widget to select a specific table from our SQL Server and certain number of rows""")

with st.echo():
    if len(password) > 0: # pauses code if no password specified
        columns, rows = run_query(f"SELECT * from [{database}].[dbo].[{table}];")

        # Converting the results to a DataFrame
        data = [dict(zip(columns, row)) for row in rows]
        CEOs = pd.DataFrame(data)
        
        st.write("Table:",table,"| Rows:",n_rows)
        # Print results.
        st.write(CEOs.head(n_rows))

st.divider()

st.markdown("## Running multiple queries with `pyodbc`:")

with st.echo():
    if len(password) > 0: # pauses code if no password specified

        # Reading the data from each table
        tables = ["E1_CEOs", "E1_Companies", "E1_Countries"]
        dataframes = {}

        for table in tables:
            columns, rows = run_query(f"SELECT * FROM [{database}].[dbo].[{table}]")
            data = [dict(zip(columns, row)) for row in rows]
            dataframes[table] = pd.DataFrame(data)

        # copying to dataframe object from dataframes dictionary
        CEOs = dataframes['E1_CEOs']
        Companies = dataframes['E1_Companies']
        Countries = dataframes['E1_Countries']

        # Print results.
        st.write(CEOs.head(),Companies.head(),Countries.head())