def adding(a, b):
	print(a+b)

def substraction(a, b):
	return a-b

def multiplication(a, b):
	return a*b

def division(a, b):
	print(a/b)

contin = True
while contin:
	a = float(input('Give number: '))
	b = float(input('Give second number: '))
	print('What do you want to do? \n1. adding\n2. substarction\n3. multiplication\n4. division')
	choice = int(input('>> '))
	if choice == 1:
		adding(a, b)
	elif choice	==	2:
		print(substarction(a, b))
	elif choice == 3:
		print(multiplication(a, b))
	elif choice == 4:
		if b != 0:
			division(a, b)
	else:
		print("There isn't option like that! Try again!")

	again = input('Do you want to calculate once again? (y/n)')
	if again == 'y':
		pass
	elif again == 'n':
		contin = False
print('Thank you for using our calculator')