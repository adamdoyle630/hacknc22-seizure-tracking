
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