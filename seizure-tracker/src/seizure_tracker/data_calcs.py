
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
                value = value + .185
                return value
            return value

        def sleep(amount_slept):
            if (amount_slept < 8):
                value = value + .115
                return value
            return value

        def stress(level):
            value = value + (level / 3 * .338)
            return value

        def alcohol(consumed):
            value = value + (consumed / 3 * .074)
            return value
        
        def menst(current):
            value = 0
            if current == True:
                value = value + .288
                return value
            return value
        
        value = medication(current) + sleep(amount_slept) + stress(level) + alcohol(consumed) + menst(current)
        risk_arr[i] = value
#the risk is the value here
    return risk_arr