#This is a dictionary. It contains "key value pairs". I am setting
#value to each ticker
stock = {"rem": "Remington", "win": "Winchester", "be": "Bear",
	"pse": "PSE"}
#This is a list of tuples inside it. Tuples are a form of list,
#they just connot be changed.
purchases = [("rem", 200, "1/14/2010", 48),
	("win", 170, "7/11/1999", 30),
	("be", 150, "3/9/2017", 1),
	("win", 145, "3/7/2000", 7),
	("pse", 200, "8/9/2000", 90)]
#looping through each purchase.
for purchase in purchases:
	ticker = purchase[0]#making ticker be the value of the first argument.

	number_of_shares = purchase[1]
	purchase_price = purchase[3]
	total_price = number_of_shares * purchase_price
	full_company_name = stock[ticker]

for ticker, name in stock.items():
	total_investment = 0
	for purchase in purchases:
		if purchase[0] == ticker:
			total_investment += (purchase[1] * purchase[3])
	print(name + ": $" + str(total_investment))

	#print("I purchased {} stock for ${} ".format(full_company_name, total_price))
	#print(purchase[0] + str(total_price))