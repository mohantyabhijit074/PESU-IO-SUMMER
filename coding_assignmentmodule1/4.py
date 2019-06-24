a=input("enter the element")
c=0
for i in a:
	if type(i)!="int":
		c+=1
if(c==0):
	print("The number is not numeric")
else:
	print("the numer is numeric") 
