
n = input("naa ba si crush?: ").capitalize()


nums = [1,2,3]


if n == "Yes":

    print("Crush is present!")
    nums.pop(0)
    print("Your list is:", nums)
elif n == "No":
    print("Crush is present!")
    nums.pop(-1)
    print("Your list is:", nums)
    nums.pop()

else:
    print("No crush today.")

    



