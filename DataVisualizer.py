import os 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set Page Configurations
st.set_page_config(page_title="Data Visualizer", layout="centered", page_icon="📊")

# Title
st.title("📊 Data Visualizer-Web App")

# Getting the Working Directory 
working_dir = os.path.dirname(os.path.abspath(__file__)) #Strips out the path of the script (aka the DataVisualizer.py)
folder_path = f"{working_dir}/data" #creates a path to a data folder inside that directory.(Includes the data in the file without imorting them)

# List all the Files
files_list = [f for f in os.listdir(folder_path) if f.endswith('.csv')] #Takes all the csv files in the data through a for loop

# Dropdown list
selected_file = st.selectbox("Select a File", files_list, index=None)

if selected_file:
    # Get the complete path of the selected file
    file_path = os.path.join(folder_path, selected_file)

    # Reading the csv file
    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)
    columns = df.columns.tolist()
    with col1:
        st.write("")
        st.write(df.head())
    with col2:
        # User selection of df columns 
        x_axis = st.selectbox("Select the X-axis", options=columns + ["None"], key="x_axis",index=None)
        y_axis = st.selectbox("Select the Y-axis", options=columns + ["None"], key="y_axis",index=None)

        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]
        selected_plot = st.selectbox("Select a Plot", options=plot_list, index=None, key="selected_plot")

# Button to generate Plots:
if st.button("Generate Plot"):
    fig, ax = plt.subplots(figsize=(6, 4))

    if selected_plot == "Line Plot":
        sns.lineplot(x=x_axis, y=y_axis, data=df, ax=ax)
    elif selected_plot == "Bar Chart":
        sns.barplot(x=x_axis, y=y_axis, data=df, ax=ax)  # Corrected typo
    elif selected_plot == "Scatter Plot":
        sns.scatterplot(x=x_axis, y=y_axis, data=df, ax=ax)
    elif selected_plot == "Distribution Plot":
        sns.histplot(x=x_axis, data=df, kde=True, ax=ax)  # Added data parameter
    elif selected_plot == "Count Plot":
        sns.countplot(x=x_axis, data=df, ax=ax)  # Added data parameter

    # Adjust the Labels
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    # Title
    plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
    plt.xlabel(x_axis, fontsize=12)
    plt.ylabel(y_axis, fontsize=12)

    st.pyplot(fig)