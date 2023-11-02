#calculator


operation_list = {"addition" , "susbtraction" , "multiplication" , "division" , "exponent"}

print("welcame to calculator")

for operation in operation_list:
    print(operation)

name = input("pliz enter your name: ")
namber_1 = int (input("pliz enter your ferst namber: "))
namber_2 = int (input("pliz enter your sec namber: "))

operation = input("what`s yuor operation: ")

if operation == "addition":
    add = namber_1 + namber_2
    print(f"addition is {add}")
elif operation == "susbtraction":
    add = namber_1 - namber_2
    print(f"susbtraction is {add}")
elif operation == "multiplication":
    add = namber_1 * namber_2
    print(f"multiplication is {add}")
elif operation == "division":
    add = namber_1 / namber_2
    print(f"division is {add}")
elif operation == "exponent":
    add = namber_1 ** namber_2
    print(f"exponent is {add}")
else:
    operation = input("S")
while operation == "done":
    break

