from random import randint
k=0
l=0
p=0
i=0
t=int(input("mis raskusaste 1/2/3?"))
for i in range(4):
	A=randint(1,20)
	B=randint(1,20)
	if t==1:
		print(f"{A}+{B}")
		a=int(float(input("")))
	elif t==2:
		print(f"{A}-{B}")
		a=int(float(input("")))
	elif t==3:
		print(f"{A}*{B}")
		a=int(float(input("")))
	if a==A+B or a==A-B or a==A*B:
		print("oige")
		l+=1
	else:
		print("vale")
		k+=1
		p+=1
	h=l/p*100
if h<=59:
	hinne="hinne 2"
elif h>=60 and h<=74:
	hinne="hinne 3"
elif h>=75 and h<=89:
	hinne="hinne 4"
elif h>=90:
	hinne="hinne5"
print(hinne)
