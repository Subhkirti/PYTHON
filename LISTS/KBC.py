option=[2,1,4]
print('Welcome to KBC:-KAUN BANEGA CODER')
print('question no.1:-')
print('What is the capital of india?')
print('Options are:-')
print('1.Chandigarh','2.Delhi', '3.Chennai','4. Bhopal')
lifeline=input("Do you want to use 50-50lifeline? y/n:")
if lifeline=="y":
	print('1.Chandigarh','2.Delhi')
	i=int(input('please enter your option number:'))
	if i!=option[0]:
		print('sorry you failed')
	else:

		print('question no.2:-')
		print('How many vowels are there?')
		print('Options are:-')
		print("1.Five", "2.Nine", "3.Seven", "4.Eight")
		p=int(input('enter your option number:'))
		if p!=option[1]:
			print('you failed')
		else:
		
			print('question no.3:-')
			print('which type of course ng will teach?')
			print('Options are:-')
			print("1.Counselling", "2.Tourism", "3.Agriculture", "4.Software engineering")
			k=int(input('enter your option no:'))
			if k!=option[2]:
				print('you failed')
			else:
				print('congrats you win')
else:
	i=int(input('please enter your option number:'))
	if i!=option[0]:
		print('sorry you failed')
	else:

		print('question no.2:-')
		print('How many vowels are there?')
		print('Options are:-')
		print("1.Five", "2.Nine", "3.Seven", "4.Eight")
		p=int(input('enter your option number:'))
		if p!=option[1]:
			print('you failed')
		else:
		
			print('question no.3:-')
			print('which type of course ng will teach?')
			print('Options are:-')
			print("1.Counselling", "2.Tourism", "3.Agriculture", "4.Software engineering")
			k=int(input('enter your option no:'))
			if k!=option[2]:
				print('you failed')
			else:
				print('congrats you win')