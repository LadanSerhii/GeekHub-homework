# Write a script which accepts a <number> from user and then <number> 
# times asks user for string input. At the end script must print 
# out result of concatenating all <number> strings.

number = int(input())
total_str = ''
for i in range(number):
	total_str += input()
print(total_str)
	
