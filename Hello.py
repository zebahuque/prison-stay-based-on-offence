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

# Load data based on selected crime
df = load_data(selected_crime)

# Clean numeric columns with commas
numeric_columns = ["Number Released", "Avg sentence in years"]
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.str.replace(',', '').astype(float))

# Line Chart
plt.figure(figsize=(12, 8))
st.subheader(f"Line Chart - Average Sentence Duration for {selected_crime}")
sns.lineplot(x="Year of Release", y="Avg sentence in years", data=df)
plt.xlabel("Year of Release")
plt.ylabel("Average Sentence Duration (years)")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better visibility
plt.title("Average Sentence Duration Over Years")
st.pyplot()

# Display the raw data
st.subheader("Raw Data")
st.dataframe(df)



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
