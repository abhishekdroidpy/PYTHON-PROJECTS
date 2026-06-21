def calculator(cart):
	prices=[float(price) for price in cart.split(",")]
	return(sum(prices))
	
	
def bill_calculator():
	cart=input("enter product prices seperated with commas: ")
	bill_amount=calculator(cart)
	
	print(f"your bill amount is {bill_amount}")
	
	
	
