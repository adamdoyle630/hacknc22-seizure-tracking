#import pandas as pd
#import numpy as np
import csv

""""
# reading CSV file
data = pd.read_csv("data.csv")

#read CSV
dataArray = np.loadtxt('data.csv',delimiter=',',names=True)


plt.figure()
for col_name in dataArray.dtype.names:
    plt.plot(dataArray[col_name], label=col_name)
plt.legend()
plt.show()


# converting column data to list
seizure_occurred_data = data['seizure occurred'].tolist()
med_taken_data = data['medication taken'].tolist()
alc_cons_data = data['alcohol consumed'].tolist()
stress_lev_data = data['stress level'].tolist()
sleep_amt_data = data['sleep amount'].tolist()
menstrual_data = data['menstrual'].tolist()
"""

def calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amount, menstruate):
    """Outputs a percent risk based off of input parameters."""
    print(f"Seizure occurred: {seizure_occurred}")
    print(f"Med Taken: {med_taken}")
    print(f"Seizure occurred: {seizure_occurred}")
    value = 0
    if not med_taken:
        value = value + .185
    if sleep_amount < 8:
        value = value + .115
    if menstruate:
        value = value + .288
    
    value = value + (stress_level / 3 * .338)
    value = value + (alc_consumed / 3 * .074)

    if value > 1:
        value = 1

    return value * 100

"""with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    for i in range(1, len(data)):
        seizure_occurred = data[i][0] == 'yes'
        med_taken = data[i][0] == 'yes'
        alc_consumed = data[i][1]
        stress_level = data[i][2]
        sleep_amount = data[i][3]
        menstruate = data[i][4]
        percent_risk = calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amount, menstruate)
        print(percent_risk)
        print(" ")
        """

def test(value) -> int:
    return int(value)