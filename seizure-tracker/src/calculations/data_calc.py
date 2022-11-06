import csv, os

def calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amount, menstruate):
    """Outputs a percent risk based off of input parameters."""
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

def calculate_risk_trend():
    value = 0
    with open("C:/Users/adamd/personal_workspace/hacknc22/seizure-tracker/src/calculations/data.csv", newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        row_count = 1
        for row in data:
            seizure_occurred = row[0] == 'yes'
            med_taken = row[1] == 'yes'
            alc_consumed = int(row[2])
            stress_level = int(row[3])
            sleep_amount = int(row[4])
            menstruate = row[5]
            value = value + calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amount, menstruate)
            row_count = row_count + 1
        
    return value / row_count