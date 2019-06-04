a=input("enter the element")
li=list(a)
c=0
for i in li:
	if (i.isnumeric()) == False:
		c+=1
if(c!=0):
	print("The number is not numeric")
else:
	print("the number is numeric") 