import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from CEGE0037_Functions import *

# Streamlit App
st.set_page_config(layout="wide")  # Set layout to wide
st.title('CEGE0037: Reliability, Risk and Resilience Engineering 24/25')
st.title('Group Project Tools')
st.write("---")
st.title("Tool 1")
# Create two columns for layout: one for Inputs and one for Analyses
col1, col2 = st.columns([1,1])

with col1:
    st.header("Inputs")
    st.write("---")

    # Add a file uploader to the webpage
    st.write("You need to add a building dataset with a column named 'water_height'. The building dataset is provided in the geodatabase file, and the water height information should be extracted from the flood raster file.")
    uploaded_file_of_buildings = st.file_uploader("Choose the Excel file of list of buildings with 'water_height'.", type=["xlsx"])

    if uploaded_file_of_buildings is not None:
        st.write("Filename of list of buildings:", uploaded_file_of_buildings.name)

    # vulnerability_models_list = 'Core Materials/vulnerabilityInventory_TV0_updated.xlsx'
    # flood_damage_dict = vulnerability_funtions(vulnerability_models_list)
    flood_damage_dict = {
        'Adb+LC+LR+1s+Com': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'Adb+LC+LR+1s+Ind': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'Adb+LC+LR+1s+Res': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'Adb+LC+LR+2s+Com': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'Adb+LC+LR+2s+Ind': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'Adb+LC+LR+2s+Res': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'Adb+LC+LR+3s+Com': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'Adb+LC+LR+3s+Ind': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'Adb+LC+LR+3s+Res': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'Adb+LC+LR+4s+Com': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'Adb+LC+LR+4s+Ind': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'Adb+LC+LR+4s+Res': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'Agri': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'BrX+LC+LR+1s+Com': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'BrX+LC+LR+1s+Ind': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'BrX+LC+LR+1s+Res': [(0, 0), (0.5, 0.66), (1, 0.98), (1.5, 1.0), (2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0)],
        'BrX+LC+LR+2s+Com': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'BrX+LC+LR+2s+Ind': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'BrX+LC+LR+2s+Res': [(0, 0), (0.5, 0.33), (1, 0.49), (1.5, 0.62), (2, 0.72), (3, 0.87), (4, 0.93), (5, 0.98), (6, 1.0)],
        'BrX+LC+LR+3s+Com': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'BrX+LC+LR+3s+Ind': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'BrX+LC+LR+3s+Res': [(0, 0), (0.5, 0.22), (1, 0.32666666666666666), (1.5, 0.41333333333333333), (2, 0.48), (3, 0.58), (4, 0.62), (5, 0.6533333333333333), (6, 0.6666666666666666)],
        'BrX+LC+LR+4s+Com': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'BrX+LC+LR+4s+Ind': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'BrX+LC+LR+4s+Res': [(0, 0), (0.5, 0.165), (1, 0.245), (1.5, 0.31), (2, 0.36), (3, 0.435), (4, 0.465), (5, 0.49), (6, 0.5)],
        'RCi+xC+LR+1s+Com': [(0, 0), (0.5, 0.396), (1, 0.588), (1.5, 0.6), (2, 0.6), (3, 0.6), (4, 0.6), (5, 0.6), (6, 0.6)],
        'RCi+xC+LR+1s+Ind': [(0, 0), (0.5, 0.396), (1, 0.588), (1.5, 0.6), (2, 0.6), (3, 0.6), (4, 0.6), (5, 0.6), (6, 0.6)],
        'RCi+xC+LR+1s+Res': [(0, 0), (0.5, 0.396), (1, 0.588), (1.5, 0.6), (2, 0.6), (3, 0.6), (4, 0.6), (5, 0.6), (6, 0.6)],
        'RCi+xC+LR+2s+Com': [(0, 0), (0.5, 0.198), (1, 0.294), (1.5, 0.372), (2, 0.432), (3, 0.522), (4, 0.558), (5, 0.588), (6, 0.6)],
        'RCi+xC+LR+2s+Ind': [(0, 0), (0.5, 0.198), (1, 0.294), (1.5, 0.372), (2, 0.432), (3, 0.522), (4, 0.558), (5, 0.588), (6, 0.6)],
        'RCi+xC+LR+2s+Res': [(0, 0), (0.5, 0.198), (1, 0.294), (1.5, 0.372), (2, 0.432), (3, 0.522), (4, 0.558), (5, 0.588), (6, 0.6)],
        'RCi+xC+LR+3s+Com': [(0, 0), (0.5, 0.132), (1, 0.19599999999999998), (1.5, 0.248), (2, 0.288), (3, 0.348), (4, 0.372), (5, 0.39199999999999996), (6, 0.39999999999999997)],
        'RCi+xC+LR+3s+Ind': [(0, 0), (0.5, 0.132), (1, 0.19599999999999998), (1.5, 0.248), (2, 0.288), (3, 0.348), (4, 0.372), (5, 0.39199999999999996), (6, 0.39999999999999997)],
        'RCi+xC+LR+3s+Res': [(0, 0), (0.5, 0.132), (1, 0.19599999999999998), (1.5, 0.248), (2, 0.288), (3, 0.348), (4, 0.372), (5, 0.39199999999999996), (6, 0.39999999999999997)],
        'RCi+xC+LR+4s+Com': [(0, 0), (0.5, 0.099), (1, 0.147), (1.5, 0.186), (2, 0.216), (3, 0.261), (4, 0.279), (5, 0.294), (6, 0.3)],
        'RCi+xC+LR+4s+Ind': [(0, 0), (0.5, 0.099), (1, 0.147), (1.5, 0.186), (2, 0.216), (3, 0.261), (4, 0.279), (5, 0.294), (6, 0.3)],
        'RCi+xC+LR+4s+Res': [(0, 0), (0.5, 0.099), (1, 0.147), (1.5, 0.186), (2, 0.216), (3, 0.261), (4, 0.279), (5, 0.294), (6, 0.3)],
        'RCi+xC+MR+5s+Com': [(0, 0), (0.5, 0.0792), (1, 0.1176), (1.5, 0.14880000000000002), (2, 0.1728), (3, 0.2088), (4, 0.22320000000000004), (5, 0.2352), (6, 0.24)],
        'RCi+xC+MR+5s+Ind': [(0, 0), (0.5, 0.0792), (1, 0.1176), (1.5, 0.14880000000000002), (2, 0.1728), (3, 0.2088), (4, 0.22320000000000004), (5, 0.2352), (6, 0.24)],
        'RCi+xC+MR+5s+Res': [(0, 0), (0.5, 0.0792), (1, 0.1176), (1.5, 0.14880000000000002), (2, 0.1728), (3, 0.2088), (4, 0.22320000000000004), (5, 0.2352), (6, 0.24)],
        'RCi+xC+MR+6s+Com': [(0, 0), (0.5, 0.066), (1, 0.09799999999999999), (1.5, 0.124), (2, 0.144), (3, 0.174), (4, 0.186), (5, 0.19599999999999998), (6, 0.19999999999999998)],
        'RCi+xC+MR+6s+Ind': [(0, 0), (0.5, 0.066), (1, 0.09799999999999999), (1.5, 0.124), (2, 0.144), (3, 0.174), (4, 0.186), (5, 0.19599999999999998), (6, 0.19999999999999998)],
        'RCi+xC+MR+6s+Res': [(0, 0), (0.5, 0.066), (1, 0.09799999999999999), (1.5, 0.124), (2, 0.144), (3, 0.174), (4, 0.186), (5, 0.19599999999999998), (6, 0.19999999999999998)],
        'RCi+xC+MR+7s+Com': [(0, 0), (0.5, 0.05657142857142857), (1, 0.08399999999999999), (1.5, 0.10628571428571428), (2, 0.12342857142857142), (3, 0.14914285714285713), (4, 0.15942857142857145), (5, 0.16799999999999998), (6, 0.1714285714285714)],
        'RCi+xC+MR+7s+Ind': [(0, 0), (0.5, 0.05657142857142857), (1, 0.08399999999999999), (1.5, 0.10628571428571428), (2, 0.12342857142857142), (3, 0.14914285714285713), (4, 0.15942857142857145), (5, 0.16799999999999998), (6, 0.1714285714285714)],
        'RCi+xC+MR+7s+Res': [(0, 0), (0.5, 0.05657142857142857), (1, 0.08399999999999999), (1.5, 0.10628571428571428), (2, 0.12342857142857142), (3, 0.14914285714285713), (4, 0.15942857142857145), (5, 0.16799999999999998), (6, 0.1714285714285714)],
        'RCi+xC+MR+8s+Com': [(0, 0), (0.5, 0.0495), (1, 0.0735), (1.5, 0.093), (2, 0.108), (3, 0.1305), (4, 0.1395), (5, 0.147), (6, 0.15)],
        'RCi+xC+MR+8s+Ind': [(0, 0), (0.5, 0.0495), (1, 0.0735), (1.5, 0.093), (2, 0.108), (3, 0.1305), (4, 0.1395), (5, 0.147), (6, 0.15)],
        'RCi+xC+MR+8s+Res': [(0, 0), (0.5, 0.0495), (1, 0.0735), (1.5, 0.093), (2, 0.108), (3, 0.1305), (4, 0.1395), (5, 0.147), (6, 0.15)],
        'StMin+LC+LR+Res': [(0, 0), (0.5, 0.02475), (1, 0.03675), (1.5, 0.0465), (2, 0.054), (3, 0.06525), (4, 0.06975), (5, 0.0735), (6, 0.075)]
    }

    st.write("---")
    st.write("**The vulnerability curve table and graph are provided only for visualization.**")

    # Create a dropdown menu for dictionary keys
    selected_key = st.selectbox("Select a flood vulnerability", options=list(flood_damage_dict.keys()))

    # Get the selected data
    selected_data = flood_damage_dict[selected_key]

    # Convert to DataFrame for table display
    df = pd.DataFrame(selected_data, columns=["Flood Height (m)", "Loss Ratio"])
    table_col, plot_col= st.columns([2, 4])

    with table_col:
        st.write("Table of Data:")
        st.dataframe(df, height=400, use_container_width=True)

    with plot_col:
        # st.write("Plot of Flood Height vs. Loss Ratio:") # Smaller size (6 inches wide, 3 inches high)
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot(df["Flood Height (m)"], df["Loss Ratio"], marker="o", linestyle="-", color="blue")
        ax.set_xlabel("Flood Height (m)", fontsize=5)
        ax.set_ylabel("Loss Ratio", fontsize=5)
        ax.set_title(f"Flood Height vs. Loss Ratio for {selected_key}", fontsize=6)
        # Adjust font size for axis tick labels
        ax.tick_params(axis='both', labelsize=5)
        ax.set_xlim(0, 6)  # Limit x-axis between 0 and 6
        ax.set_ylim(0, 1)  # Limit y-axis between 0 and 1
        ax.grid(True)

        # Display the plot in Streamlit
        st.pyplot(fig)

with col2:
    st.header("Output")
    st.write("---")
    st.write("Loss ratio of Tomorrowville buildings following flood damage:")

    # Handle the Buildings file and calculate the damage levels
    if uploaded_file_of_buildings is not None:
        try:
            # Load the building data
            Buildings = pd.read_excel(uploaded_file_of_buildings)

            # Calculate the damage level using the physical_impact_buildings function
            dmg_level = physical_impact_buildings(Buildings, flood_damage_dict)

            # Add damage level to Buildings DataFrame
            Buildings['Loss_Ratio'] = dmg_level

            st.dataframe(Buildings, height=400, use_container_width=True)

        except Exception as e:
            st.error(f"Error processing buildings file: {e}")

    st.write("Note: To complete the analysis for Goal 1, download the table and perform the calculations using Excel, Python, or MATLAB.")

st.write("---")

# Create two columns for layout: one for Inputs and one for Analyses
col3, col4 = st.columns([1,1])
with col3:

    st.title("Tool 2")

    st.header("Inputs")
    st.write("---")
    st.write("The requested value here represents the permeation rate of water levels in buildings.")
    # start = st.number_input(label="Start day for resilience curve instances (days)", min_value=0, max_value=10000, value=0, step=1)
    # end = st.number_input(label="End day for resilience curve instances (days)", min_value=0, max_value=10000, value=0, step=1)
    # num_intervals = st.number_input(label="Number of instances", min_value=3, max_value=1000, value=3, step=1)
    permeation_rate_mm_day = st.number_input(label="Permeation Rate (mm/day)", min_value=1, max_value=10000, value=1, step=1)
    permeation_rate = permeation_rate_mm_day / 1000
    st.text(f"Permeation Rate: {permeation_rate:.3f} meters/day")
    st.write("---")

    loss_ratio_limit = st.number_input(label="Loss ratio threshold that you assume for occupiability of buildings.", min_value=0.00, max_value=1.00, value=0.00, step=0.01)
    st.write("---")
    # intervals = np.linspace(start, end, num_intervals, endpoint=True)
    # time_list = list(intervals)

    # Define initial data as a dictionary
    data = [
        {"vulnStrFL": "Adb+LC+LR+1s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+2s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+3s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+4s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+1s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+2s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+3s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+4s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+1s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+2s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+3s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+4s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+5s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+6s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+7s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+8s+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+1s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+2s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+3s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+4s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+1s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+2s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+3s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+4s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+1s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+2s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+3s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+4s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+5s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+6s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+7s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+8s+Com", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+1s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+2s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+3s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Adb+LC+LR+4s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+1s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+2s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+3s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "BrX+LC+LR+4s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+1s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+2s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+3s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+4s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+5s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+6s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+7s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "RCi+xC+LR+8s+Ind", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "StMin+LC+LR+Res", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
        {"vulnStrFL": "Agri", "Loss Ratio = 0.0": 0, "Loss Ratio = 0.2": 40, "Loss Ratio = 0.4": 80, "Loss Ratio = 0.6": 120, "Loss Ratio = 0.8": 160, "Loss Ratio = 1.0": 200},
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    st.write("**Restoration time for building typologies of Tomorrowville**")
    st.write("Here, you are expected to enter the number of days required for restoration based on building types corresponding to loss ratios. You can assign days to loss ratios below the threshold you set; however, the restoration time calculation will only apply to values above the threshold.")
    st.write("Please edit the table below as needed and click 'Save & Run' to submit.")

    # Display the table editor
    days_for_recovery_vulnerability = st.data_editor(df, num_rows="dynamic", height=400, use_container_width=True)

    # Function to validate if any cell contains negative values
    def validate_no_negative_values(df):
        for column in df.columns:
            if df[column].dtype in ['float64', 'int64']:  # Only check numerical columns
                if (df[column] < 0).any():
                    st.error(f"Negative values detected in column '{column}'. Please correct them.")
                    return False
        return True

    flag_save = 0
    # When user submits or updates the DataFrame, validate
    if st.button("Save & Run"):
        if validate_no_negative_values(days_for_recovery_vulnerability):
            st.success("Data saved successfully!")
            flag_save = 1

            buildings_df = water_permeation_and_recovery_days(Buildings, permeation_rate, loss_ratio_limit, days_for_recovery_vulnerability)
        else:
            st.warning("Please fix the negative values before saving.")


with col4:
    st.title("")
    st.header("Output")
    st.write("---")

    # Convert back to dictionary on save
    if flag_save == 1:
        st.success("Restoration time for building typologies has been saved!")
        st.dataframe(days_for_recovery_vulnerability, height=400, use_container_width=True)  # Display the updated DataFrame

        # Display the Buildings DataFrame
        st.write("---")
        st.write("Dataset of Tomorrowville buildings with downtime information:")
        st.dataframe(buildings_df, height=400, use_container_width=True)

    st.write(
        "Note: To complete the analysis for Goal 2, download the table and perform the calculations using Excel, Python, or MATLAB.")
st.write("---")

st.write('You can find the repo [here](https://github.com/alitatici/CEGE0037_GroupProjectTools).')

