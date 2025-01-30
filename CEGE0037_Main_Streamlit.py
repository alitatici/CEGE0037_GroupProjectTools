import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from CEGE0037_Functions import *

# Streamlit App
st.set_page_config(layout="wide")  # Set layout to wide
st.title('CEGE0037: Reliability, Risk and Resilience Engineering 24/25')
st.title('Group Project Tools')
st.write("---")
tab1, tab2 = st.tabs(["Tool 1", "Tool 2"])

with tab1:
    st.title("Tool 1")
    st.write("You can use this tool for the first goal of the assessment.")
    # Create two columns for layout: one for Inputs and one for Analyses
    col1, col2 = st.columns([1,1])

    with col1:
        st.header("Inputs")
        st.write("---")

        # Add a file uploader to the webpage
        st.write("You need to add a building dataset with a column named 'water_height'. The building dataset is provided in the geodatabase file, and the water height information should be extracted from the flood raster file.")
        uploaded_file_of_buildings = st.file_uploader("Choose the Excel file of list of buildings with 'water_height'.", type=["xlsx"], key="file_uploader_tab1")

        if uploaded_file_of_buildings is not None:
            st.write("Filename of list of buildings:", uploaded_file_of_buildings.name)

        # vulnerability_models_list = 'Core Materials/vulnerabilityInventory_TV0_updated.xlsx'
        # flood_damage_dict = vulnerability_funtions(vulnerability_models_list)
        flood_damage_dict = vulnerability_funtion_manual()

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
        st.write("Loss ratio of Tomorrowville buildings following flood damage, calculated based on their corresponding vulnerability curves.")

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

        st.write("Note: To complete the analysis for the first goal of the assessment, download the table and perform the calculations using Excel, Python, or MATLAB.")

    st.write("---")

with tab2:
    st.title("Tool 2")
    st.write("You can use this tool for the second goal of the assessment.")

    # Create two columns for layout: one for Inputs and one for Analyses
    col3, col4 = st.columns([1,1])
    with col3:
        st.header("Inputs")
        st.write("---")

        # Add a file uploader to the webpage
        st.write(
            "You need to add a building dataset with a column named 'water_height'. The building dataset is provided in the geodatabase file, and the water height information should be extracted from the flood raster file.")
        uploaded_file_of_buildings_2 = st.file_uploader("Choose the Excel file of list of buildings with 'water_height'.",
                                                      type=["xlsx"], key="file_uploader_tab2")

        if uploaded_file_of_buildings_2 is not None:
            st.write("Filename of list of buildings:", uploaded_file_of_buildings_2.name)


        st.write("---")

        # Handle the Buildings file and calculate the damage levels
        if uploaded_file_of_buildings_2 is not None:
            try:
                # Load the building data
                Buildings_goal_2 = pd.read_excel(uploaded_file_of_buildings_2)

                # Calculate the damage level using the physical_impact_buildings function
                dmg_level = physical_impact_buildings(Buildings_goal_2, flood_damage_dict)

                # Add damage level to Buildings DataFrame
                Buildings_goal_2['Loss_Ratio'] = dmg_level

            except Exception as e:
                st.error(f"Error processing buildings file: {e}")


        st.write("The requested value here represents the permeation rate of water levels in buildings.")
        st.write("This permeation rate will be used specifically at building locations.")
        # start = st.number_input(label="Start day for resilience curve instances (days)", min_value=0, max_value=10000, value=0, step=1)
        # end = st.number_input(label="End day for resilience curve instances (days)", min_value=0, max_value=10000, value=0, step=1)
        # num_intervals = st.number_input(label="Number of instances", min_value=3, max_value=1000, value=3, step=1)
        permeation_rate_mm_day = st.number_input(label="Permeation Rate (mm/day)", min_value=0, max_value=10000, value=1, step=1)
        permeation_rate = permeation_rate_mm_day / 1000
        st.text(f"Permeation Rate: {permeation_rate:.3f} meters/day")
        st.write("---")

        loss_ratio_limit = st.number_input(label="Provide the minimum loss ratio that would render a building unoccupiable.", min_value=0.00, max_value=1.00, value=0.00, step=0.01)
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
        st.write("Please enter the number of days required to fully restore (and therefore occupy) different building typologies for different loss ratios that a flood might cause.")
        st.write("Note that you should only enter non-zero numbers for loss ratios above the occupiability threshold you set previously (i.e., it is assumed that buildings experiencing loss ratios below the threshold set can be restored while being occupied).")
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

                buildings_df = water_permeation_and_recovery_days(Buildings_goal_2, permeation_rate, loss_ratio_limit, days_for_recovery_vulnerability)
            else:
                st.warning("Please fix the negative values before saving.")


    with col4:
        st.header("Output")
        st.write("---")

        # Convert back to dictionary on save
        if flag_save == 1:
            st.success("Restoration time for building typologies has been saved!")
            
            st.write("Restoration time corresponding to the specified loss ratios input by the user for different building typologies:")
            st.dataframe(days_for_recovery_vulnerability, height=400, use_container_width=True)  # Display the updated DataFrame

            # Display the Buildings DataFrame
            st.write("---")
            st.write("Dataset of Tomorrowville buildings with downtime information:")
            st.dataframe(buildings_df, height=400, use_container_width=True)

        st.write(
            "Note: To complete the analysis for the second goal of the assessment, download the table and perform the calculations using Excel, Python, or MATLAB.")
    st.write("---")

# Run the app with `streamlit run CEGE0037_Main_Streamlit.py`
# streamlit run CEGE0037_Main_Streamlit.py

