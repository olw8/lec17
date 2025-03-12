import streamlit as st
import sqlalchemy
import pandas as pd

# define username / password / database
st.markdown("""# Connecting to SQL Server with `sqlalchemy`
Let's connect to our SQL server with the `sqlalchemy` package. As you remember from `lec12-2.ipynb`, this package requires 
a data source name (DSN) established with `OBDC Driver 18`. If you did not set these up, jump to the `SQL Server pymssql` page.
## Provide SQL Server Parameters:
Define our variables:""")

with st.echo():
    dsn = st.text_input("Enter your Data Source Name (DSN) for `pyobdc 18`:",placeholder="DSN")
    username = st.text_input("Enter your username:",placeholder="Username")
    password = st.text_input("Enter a password:", type="password",placeholder="Password")
    database = st.text_input("Enter your SQL Server database:", placeholder="Database name",value="CEE412_CET522_W25")

st.markdown("""### Define Query Connection with `@st.cache_resource`
Now, we can use the Widget to select a specific table from our SQL Server and certain number of rows""")

"""
```python
@st.cache_resource # insert this before the function below
```"""
with st.echo():
    # Uses st.cache_resource to only run once.
    @st.cache_resource
    def init_connection():
        return f'mssql+pyodbc://{username}:{password}@{dsn}'
    
    if len(password) > 0: # pauses code if no password specified
        # Creating the connection string for SQLAlchemy
        connection_string = init_connection()

st.markdown("""### Define query function within `@st.cache_data`:
Uses `st.cache_data` to only rerun when the query changes or after 10 min.""")

"""
```python
@st.cache_data(ttl=600) # insert this before the function below
```"""
with st.echo():
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def run_query(query, connection_string):
        # Creating the SQLAlchemy engine
        engine = sqlalchemy.create_engine(connection_string)       
        df = pd.read_sql(query, engine)
            
        return df

st.divider()

st.markdown("## Running a single query with `sqlalchemy`:")

with st.echo():
    if len(password) > 0: # pauses code if no password specified
        df = run_query(f"SELECT * FROM [{database}].[dbo].[E1_CEOs]", connection_string)

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
        df = run_query(f"SELECT * FROM [{database}].[dbo].[{table}]", connection_string)
        st.write("Table:",table,"| Rows:",n_rows)
        st.write(df.head(n_rows))

st.divider()

st.markdown("## Running multiple queries with `pyodbc`:")

with st.echo():
    if len(password) > 0: # pauses code if no password specified
        # creating the tables with the engine
        CEOs = run_query(f"SELECT * FROM [{database}].[dbo].[E1_CEOs]", connection_string)
        Companies = run_query(f"SELECT * FROM [{database}].[dbo].[E1_Companies]", connection_string)
        Countries = run_query(f"SELECT * FROM [{database}].[dbo].[E1_Countries]", connection_string)
        st.write(CEOs.head(),Companies.head(),Countries.head())