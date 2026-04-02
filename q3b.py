def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a[2:]
    b = b[2:]
    while len(a) < len(b):
        a = "0" + a
    while len(b) < len(a):
        b = "0" + b
    result = ""
    carry = "0"
    for i in range(len(a) - 1, -1, -1):
        total = a[i] + b[i] + carry
        if total == "000":
            result = "0" + result
            carry = "0"
        elif total in ("001", "010", "100"):
            result = "1" + result
            carry = "0"
        elif total in ("011", "101", "110"):
            result = "0" + result
            carry = "1"
        elif total == "111":
            result = "1" + result
            carry = "1"
    if carry == "1":
        result = "1" + result
    while result[0] == "0":
        result = result[1:]
    return "0b" + result

        







