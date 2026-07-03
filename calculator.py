from functools import reduce

operations = ["divide","addition","subtraction","multiplication"]

operation = input("Select operation in words : ").lower()

if operation not in operations:
    print("Invalid operation")
else:
    if operation == "divide": 
        value = float(input("Enter number : "))
        diviser = float(input("Enter diviser : "))
        print("Answer : " ,value/diviser)
    else:
        operands = input("Enter numbers first (comma separated; negatives allowed) : ")
        operands_list = [num.strip() for num in operands.split(",") if num.strip()]
        float_list = [float(num) for num in operands_list]

        match operation:
            case "addition":
                print(sum(float_list))
            case "subtraction":
                if len(float_list) == 1:
                    print(float_list[0])
                else:
                    print(reduce(lambda x, y: x - y, float_list))
            case "multiplication":
                if len(float_list) == 1:
                    print(float_list[0])
                else:
                    print(reduce(lambda x, y: x * y, float_list))
