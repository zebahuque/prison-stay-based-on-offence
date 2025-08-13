import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load CSV data based on selected crime
def load_data(crime):
    file_path = f"{crime}.csv"
    df = pd.read_csv(file_path, thousands=',')  # Specify thousands=',' to handle comma in numbers
    return df

# Streamlit app
st.title("Prison Sentence Line Chart")

# Dropdown selector for crime type
crime_options = ["0000 All Crimes", "0001 Violent", "0002 Sex Offense", "0003 Property"]
selected_crime = st.selectbox("Select Crime Category", crime_options)

# Load data based on selection
if selected_crime == "0000 All Crimes":
    # Load all datasets for comparison
    crime_files = {
        "All Crimes": "0000 All Crimes",
        "Violent": "0001 Violent",
        "Sex Offense": "0002 Sex Offense",
        "Property": "0003 Property"
    }
    dfs = {name: load_data(fname) for name, fname in crime_files.items()}
    chart_title = "Line Chart - Average Sentence Duration for All Crime Categories"
    raw_data_title = "Raw Data for All Crimes"
    main_df_key = "All Crimes"
else:
    # Load just the selected crime data
    dfs = {selected_crime: load_data(selected_crime)}
    chart_title = f"Line Chart - Average Sentence Duration for {selected_crime}"
    raw_data_title = f"Raw Data for {selected_crime}"
    main_df_key = selected_crime

# Clean all loaded dataframes
numeric_columns = ["Number Released", "Avg sentence in years"]
for df in dfs.values():
    for col in numeric_columns:
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace(',', '').astype(float)

# Line Chart
st.subheader(chart_title)
fig, ax = plt.subplots(figsize=(12, 8))

# Plot data
if len(dfs) > 1:
    for name, df in dfs.items():
        sns.lineplot(x="Year of Release", y="Avg sentence in years", data=df, ax=ax, label=name)
    ax.legend()
else:
    df_single = list(dfs.values())[0]
    sns.lineplot(x="Year of Release", y="Avg sentence in years", data=df_single, ax=ax)

ax.set_xlabel("Year of Release")
ax.set_ylabel("Average Sentence Duration (years)")
ax.set_title("Average Sentence Duration Over Years")
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")  # Rotate x-axis labels for better visibility
st.pyplot(fig)

# Display the raw data
st.subheader(raw_data_title)
st.dataframe(dfs[main_df_key])



# # Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #     http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# import streamlit as st
# from streamlit.logger import get_logger

# LOGGER = get_logger(__name__)


# def run():
#     st.set_page_config(
#         page_title="Hello",
#         page_icon="👋",
#     )

#     st.write("# Welcome to Streamlit! 👋")

#     st.sidebar.success("Select a demo above.")

#     st.markdown(
#         """
#         Streamlit is an open-source app framework built specifically for
#         Machine Learning and Data Science projects.
#         **👈 Select a demo from the sidebar** to see some examples
#         of what Streamlit can do!
#         ### Want to learn more?
#         - Check out [streamlit.io](https://streamlit.io)
#         - Jump into our [documentation](https://docs.streamlit.io)
#         - Ask a question in our [community
#           forums](https://discuss.streamlit.io)
#         ### See more complex demos
#         - Use a neural net to [analyze the Udacity Self-driving Car Image
#           Dataset](https://github.com/streamlit/demo-self-driving)
#         - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#     """
#     )


# if __name__ == "__main__":
#     run()
