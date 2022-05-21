x=input()
nums=[int(i) for i in x]
xor = 0
for num in nums:
    xor ^= num
print(xor)