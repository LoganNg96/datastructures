amount = int(input("Enter a number, I will give you the odd numbers and the even numbers: "))
nums = []
for x in range(amount):
    numbers = int(input("Now give me the numbers one by one: "))
    nums.append(numbers)

odd_total = 0
even_total = 0
for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_total += nums[i]
    else:
        odd_total += nums[i]

print(odd_total)
print(even_total)

