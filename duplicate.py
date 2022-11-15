numbers=[1,2,2,6,9,4,4,9,9]
duplicate=[]
i=0
while i <len(numbers):
	if numbers[i] not in duplicate:
		duplicate.append(numbers[i])
	i=i+1
print(duplicate)




