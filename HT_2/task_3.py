# Write a script which accepts a <number> from user and print out 
# a sum of the first <number> positive integers.

number = int(input())
total = 0
for i in range(number + 1):
	total += i
print(total)
	
