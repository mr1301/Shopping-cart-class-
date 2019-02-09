import datetime
import csv

products =[]
csv_file_path = "products.csv"  # a relative filepath

with open(csv_file_path, "r") as csv_file:  # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file)  # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        #d = dict(row)
        d = {"id": row["id"], "name": row["name"], "price": float(row["price"])}
        #print(type(d), d["name"], d["price"])
        products.append(d)












today = datetime.date.today()
#print(str(today))  # > '2017-07-02'

now = datetime.datetime.now()
#print(str(now))  # > '2017-07-02 23:43:25.915816'
#print(now.strftime("%Y-%m-%d"))  # > '2017-07-02'
#print(now.strftime("%H:%M:%S"))

#print("CHECK OUT AT", now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), "AM")



#**************** Above = Time Module, Below = Inputs*******************


#TODO read csv file
  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017





















# TODO: write some Python code here to produce the desired functionality...
#print(products)

#**************class notes shopping-cart *************************************************

#for p in products:
 # print (p)
#x = 3 #when x is 3 the loop will execute infinitely because x will always be 3
#x = 2 + 1
#X = X + 1  # if you evaluate x will be equal to 4. so scrap 3o, evaluate 31, and plug into 32

# Print("Started at: " + t) #time on receipt
#x = 1
#while x < 5:
  #y = input("Please input a product id: ")
  #print(y)
  #print(x)
  #x = x+1 #this is a command/ variable assignment to make it a mathematical formula use ==
#x = 1
#running_total = 0

#while x < 5: #todo: while True
  #selected_id = 1 # input("please select a product id (1-20) ")
  #matching_products = [p for p in products if p["id"] == selected_id] # for each item in our list of items return the item if it matches a certain criterion. interpret from for.
  #product = matching_products[0]
  #price = product["price"] #4.95
  #running_total = running_total + price
  #x = x + 1

#print("The total price is: " + str(running_total))
#todo: calculate tax, add tax + total
#modules (date & time)
#Filteringlists
#accumulators and counters

#***************************** Instructions***************************************************
#A grocery store name of your choice.
#A grocery store phone number and/or website URL and/or address of choice.
#The date and time of the beginning of the checkout process, formatted in a human-friendly way.
#The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50).
#The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices.
#The amount of tax owed, calculated by multiplying the total cost by a District of Columbia sales tax rate of 6%.
#The total amount owed, formatted as US dollars and cents (e.g. $4.77), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items.
#A friendly message thanking the customer and/or encouraging the customer to shop again.


#********* Information input ******************************************************************

total_price = 0
selected_ids = []
while True:
  selected_id = input("Please input a product identifier")  #9 is str
  if selected_id == "done":
    break
  else:
    #match_products = [p for p in products if str(p["id"]) == str(selected_id)]
    #match_product = match_products[0]
    #total_price = total_price + match_product["price"]
    #print("Selected Product: " + match_product["name"] + " " + str(match_product["price"]))
     selected_ids.append(selected_id)

#******************Information Output*************************************************************

print("                             ")
print("                             ")
print("-----------------------------")
print("THE SOUP BOWL - GEORGETOWN   ")
print("202-997-0229", "WWW.TSB.COM  ")
print("TIME", now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), "AM")
print("-----------------------------")
print("SELECTED PRODUCTS:           ")
print("-----------------------------")

#print(selected_ids)
for selected_id in selected_ids:
  match_products = [p for p in products if str(p["id"]) == str(selected_id)]
  match_product = match_products[0]
  total_price = total_price + match_product["price"]
  print("- " + match_product["name"] + " " + "${0:.2f}".format(match_product["price"]))

print("-----------------------------")
print("SUB-TOTAL: ${0:.2f}".format(total_price))
Tax = (total_price* 0.06)
print("TOTAL-TAX: ${0:.2f}".format(Tax))
Total_Pay = total_price + Tax
print("TOTAL-PAY: ${0:.2f}".format(Total_Pay))
print("-----------------------------")
print("THANK YOU,", "SEE YOU AGAIN SOON")
print("-----------------------------")

#TODO read from csv.file
