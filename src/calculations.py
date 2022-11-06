import csv

def calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amoun, menstruate) -> float:
    """Outputs a percent risk based off of input parameters."""
    print(f"Seizure occurred: {seizure_occurred}")
    print(f"Med Taken: {med_taken}")
    print(f"Drinks consumed: {alc_consumed}")
    print(f"Stress level: {stress_level}")
    print(f"Hours of Sleep: {sleep_amount}")
    print(f"Menstruating: {menstruate}")

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data:
        seizure_occurred = row[0] == 'yes'
        med_taken = row[1] == 'yes'
        alc_consumed = row[2]
        stress_level = row[3]
        sleep_amount = row[4]
        menstruate = row[5]
        calculate_risk(seizure_occurred, med_taken, alc_consumed, stress_level, sleep_amount, menstruate)
        print(" ")

"""
def risk(value):
    value = 0
    taken = False
    amount_slept = 8
    level = 6
    consumed = False
    current = False

    risk_arr = [0] * 7

    for i in range(7):
        def medication(taken):
            if (taken == False):
                value = value + .1
                return value
            return value

        def sleep(amount_slept):
            if (amount_slept < 8):
                value = value + .14
                return value
            return value

        def stress(level):
            if (level >= 5):
                value = value + .41
                return value
            return value

        def alcohol(consumed):
            if (consumed == True):
                value = value + .09
                return value
            return value
        
        def menst(current):
            value = 0
            if current == True:
                value == value + .35
                return value
            return value
        
        value = medication(current) + sleep(amount_slept) + stress(level) + alcohol(consumed) + menst(current)
        risk_arr[i] = value
#the risk is the value here
    return risk_arr

"""