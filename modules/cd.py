first_array = []
common_divisors = []
def run(a, b, c):
    for divisor in range(1, c + 1):
        result = a / divisor
        if result.is_integer():
            first_array.append(divisor)
            print("Found! Divisor:", divisor, "Result:", result)
    print("Phase 2")
    for divisor in first_array:
        result =  b / divisor
        if result.is_integer():
            common_divisors.append(divisor)
            print("Found! Divisor:", divisor, "Result:", result)

    print("First array:", first_array)
    print ("Second array:", common_divisors)
    print("Number a: "+ str(a))
    print("Number b: "+ str(b))
    print("Max divisor: "+ str(c))
    if common_divisors:
        print("Common divisors:", common_divisors)
        print("Greatest common divisor:", max(common_divisors))
    else:
        print("No common divisors found")
run(20, 65, 65)

