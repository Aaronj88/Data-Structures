'''mylist = []
num_repeat = int(input("How many numbers would you like in your list?"))
for i in range (0,num_repeat):
    num = int(input("Choose a number to add:        "))
    mylist.append[num]'''


nums = list(map(int, input("Enter the numbers you want to add with commas in between here:            ").split(",")))
print(nums)



num_search = int(input("Enter the number you would like to search for here:         "))

#Method No.1:
if num_search in nums:
    print("Yes, this number is one of your previously entered numbers.")

else:
    print("No, this number is not one of your previously entered numbers.")


#Method No.2:
for i in range(len(nums)):
    if nums[i] == num_search:
        print("Yes, this number is one of your previously entered numbers.")

    else:
        print("No, this number is not one of your previously entered numbers.")


#Method No.3:
for i in nums:
    if i == num_search:
        print("Yes, this number is one of your previously entered numbers.")

    else:
        print("No, this number is not one of your previously entered numbers.")





