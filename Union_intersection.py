Array1=[10,12,31,42,35,16,10]
Array2=[21,10,13,16,42,31,19]
i=0
list=[]
while i <len(Array1):
    if Array1[i]not in Array2:
        list.append(Array1[i])
    if Array2[i] in Array1:
        list.append(Array2[i])
    else:
        list.append(Array2[i])
    i+=1
print(list)
j=0
list2=[]
while j <len(Array2):
                if Array2[j]in Array1:
                    list2.append(Array2[j])
                j+=1
print(list2)




    