# Selection Sort

a=[4,34,67,12,3,10,5,2,78]
i=0
while i <len(a):
	j=0
	min=i
	while j <len(a):
		if a[min]<a[j]:
			min=j
		j=j+1
		a[i],a[min]=a[min],a[i]
	i=i+1
print(a)

# BUBBLE SORT
# a=[60,80,70,30,50,10]
# i=0
# attemp=0
# while i<len(a):
# 	j=0
# 	while j<len(a):
# 		if a[i]<a[j]:
# 			attemp=a[j]
# 			a[j]=a[i]
# 			a[i]=attemp
# 		j=j+1
# 	i=i+1
# print(a)


# Insertion Sort

# a=[12,54,67,3,4,58,34]
# i=0
# while i <len(a):
#    r=a[i]
#    s=i
#    while s>0 and a[s-1]>r:
#         a[s]=a[s-1]     
#         s=s-1
#    a[s]=r
#    i=i+1
# print(a)



