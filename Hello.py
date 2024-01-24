import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load CSV data based on selected crime
def load_data(crime):
    file_path = f"{crime}.csv"
    df = pd.read_csv(file_path)
    return df

# Streamlit app
st.title("Prison Sentence Visualization Dashboard")

# Sidebar with crime selection
crime_options = ["0000 All Crimes", "0001 Violent", "0002 Sex Offense", "0003 Property"]
selected_crime = st.sidebar.selectbox("Select Crime Category", crime_options)

# Load data based on selected crime
df = load_data(selected_crime)

# Line chart for average sentence over the years
st.subheader(f"Average Sentence Over the Years - {selected_crime}")
fig_avg_sentence = plt.figure()
sns.lineplot(x="Year of Release", y="Avg sentence in years", data=df)
st.pyplot(fig_avg_sentence)

# Bar chart for percent released by parole
st.subheader(f"Percent Released by Parole Over the Years - {selected_crime}")
fig_parole = plt.figure()
sns.barplot(x="Year of Release", y="Percent released by Parole", data=df)
st.pyplot(fig_parole)

# You can add more visualizations based on your specific needs

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
