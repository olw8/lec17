import streamlit as st
import pymssql
import pandas as pd

# define username / password / database
st.markdown("""# Connecting to SQL Server with `pymssql`
Let's connect to our SQL server with the `pymssql` package.
## Provide SQL Server Parameters:
Define our variables:""")

with st.echo():
    username = st.text_input("Enter your username:", placeholder="Username")
    password = st.text_input("Enter a password:", type="password",placeholder="Password")
    database = st.text_input("Enter your SQL Server database:", placeholder="Database name",value="CEE412_CET522_W25")
    server='128.95.29.66'


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
        return pymssql.connect(server, 
            username, password, "{}".format(database))

with st.echo():
    if len(password) > 0:
        st.write('Password has been entered, attempting to connect...')
        conn = init_connection()
        c1 = conn.cursor()
        st.write("Connected to database: {} via username: {}".format(database, username))
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
        with c1:
            c1.execute(query)
            # retrieve data
            data = c1.fetchall()
            # retrieve column names
            column_names = [item[0] for item in c1.description]
            # create dataframe from the retrieved data
            df = pd.DataFrame(data)
            # and name its columns with retrieved column names
            df.columns = column_names
        return df

st.divider()

st.markdown("## Running a single query with `pymssql`:")

with st.echo():
    if len(password) > 0: # pauses code if no password specified
        df = run_query(f'SELECT * FROM [{database}].[dbo].[E1_CEOs]')
        df

st.divider()

st.markdown("""## Specify which Table
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
        df = run_query(f'SELECT * FROM [{database}].[dbo].[{table}]')

        st.write("Table:",table,"| Rows:",n_rows)

        st.write(df.head(n_rows))