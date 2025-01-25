import numpy as np
import pandas as pd
import scipy.io
import scipy.spatial
from scipy.interpolate import interp1d

def vulnerability_funtions():
    """
    This is the definition of the vulnerability_funtions function, which takes a single argument
    vulnerability_models - the name of an Excel file that contains the data to be processed.
    """
    df = pd.read_excel(vulnerability_models_list, sheet_name=1)

    # initialize an empty dictionary to store the results
    vulnerability_dict = {}

    # loop through each row in the dataframe
    for index, row in df.iterrows():
        # get the value of the "vulnStrFL" column for the current row
        vulnStrFL = row['vulnStrFL']

        # get a list of tuples, each tuple containing the value of the "LR(hw=x)" column
        # (where x is a number) and the corresponding "hw" value
        lr_hw_pairs = [(hw, row['LR(hw={})'.format(hw)]) for hw in [0, 0.5, 1, 1.5, 2, 3, 4, 5, 6]]

        # add the current vulnStrFL value as the key in the "result" dictionary,
        # and the corresponding lr_hw_pairs list as the value
        vulnerability_dict[vulnStrFL] = lr_hw_pairs
    return vulnerability_dict


def interpolation(d, x):
    """
    This function performs linear interpolation on two points `d` and a value `x`.
    Arguments:
        d: (List[Tuple[float, float]]) - a list of two tuples, each tuple containing an `x` value and a corresponding `y` value
        x: (float) - the value at which the interpolation should be performed
    Returns:
        output_int: float - the linearly interpolated value at `x`
    """
    # Perform linear interpolation calculation
    x_val = np.array([t[0] for t in d])
    y_val = np.array([t[1] for t in d])
    # output_int = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))
    f = interp1d(x_val, y_val)
    output_int = float(f(x))

    # Return the interpolated value
    return output_int

def physical_impact_buildings(Buildings, flood_damage_dict):
    """
    This function calculates the physical impact of a flood on buildings.
    `Buildings` is a Pandas DataFrame that contains the data of the buildings.
    `flood_damage_dict` is a dictionary that maps vulnerability strings to damage functions.
    The function returns a list of damage levels for each building.
    """
    # Get the vulnerability strings and water heights from the buildings data
    vulnerability_strings = Buildings['vulnStrFL']
    water_height = Buildings['water_height']  # Need to estimate this one and add it to "Buildings"

    # Initialize an empty list to store the damage levels
    dmg_level = []

    # Loop through each building
    for i in range(len(vulnerability_strings)):
        # Get the vulnerability string and the corresponding damage function
        vuln_string = vulnerability_strings[i]
        try:
            vuln_function = flood_damage_dict[vuln_string]
        except:
            vuln_string = vuln_string.replace('\n', '')
            vuln_function = flood_damage_dict[vuln_string]

        # Calculate the damage level using the interpolation function
        damage = interpolation(vuln_function, water_height[i])

        # Append the damage level to the list
        dmg_level.append(damage)

    # Return the list of damage levels
    return dmg_level


# GOAL 2
def water_permeation_and_recovery_days(buildings_df, permeation_rate, loss_ratio_limit, days_for_recovery_vulnerability):
    """
        Water permeation time and recovery time are calculated in weeks.
    """
    recovery_time_array = []
    water_permeation_time_array = []
    # days_for_recovery_vulnerability = restoration_times()

    for i, row in buildings_df.iterrows():
        water_that_should_permeate = row['water_height'] - 0.25
        if water_that_should_permeate > 0:
            water_permeation_time = water_that_should_permeate / permeation_rate
        else:
            water_permeation_time = 0

        recovery_time = restoration_time_calculation(row, days_for_recovery_vulnerability, loss_ratio_limit)

        recovery_time_array.append(recovery_time)
        water_permeation_time_array.append(water_permeation_time)

    buildings_df['water_permeation_time_in_days'] = water_permeation_time_array
    buildings_df['recovery_time_in_days'] = recovery_time_array

    return buildings_df

def restoration_time_calculation(row, days_for_recovery_vulnerability, loss_ratio_limit):

    vulnerability_strings = days_for_recovery_vulnerability['vulnStrFL'].tolist()

    vulnStrFL_row = row['vulnStrFL'].strip()
    Loss_Ratio = row['Loss_Ratio']
    recovery_time = 0

    for index, vulnerability_string in enumerate(vulnerability_strings):
        if vulnerability_string == vulnStrFL_row:
            if Loss_Ratio < loss_ratio_limit:
                recovery_time = 0
            else:
                LR00 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 0.0"]
                LR02 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 0.2"]
                LR04 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 0.4"]
                LR06 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 0.6"]
                LR08 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 0.8"]
                LR10 = days_for_recovery_vulnerability.loc[index, "Loss Ratio = 1.0"]

                if 0.0 <= Loss_Ratio < 0.2:
                    recovery_time = ((Loss_Ratio - 0.0) / 0.2) * (LR02 - LR00) + LR00
                elif 0.2 <= Loss_Ratio < 0.4:
                    recovery_time = ((Loss_Ratio - 0.2) / 0.2) * (LR04 - LR02) + LR02
                elif 0.4 <= Loss_Ratio < 0.6:
                    recovery_time = ((Loss_Ratio - 0.4) / 0.2) * (LR06 - LR04) + LR04
                elif 0.6 <= Loss_Ratio < 0.8:
                    recovery_time = ((Loss_Ratio - 0.6) / 0.2) * (LR08 - LR06) + LR06
                elif 0.8 <= Loss_Ratio <= 1.0:
                    recovery_time = ((Loss_Ratio - 0.8) / 0.2) * (LR10 - LR08) + LR08
                else:
                    raise ValueError("Loss_Ratio must be between 0 and 1.")

    return np.round(recovery_time, 2)
