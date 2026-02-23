products = []
prices = []
quantities = []
total_amount  = 0
changes = 0

print("^_^------------Mall Calculator---------^_^\n\n\n")
    
while True:    
    product = input("Enter Product: ")
    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number and quantity must be a whole number.\n")
        continue

    if price < 0:
        print("Price cannot be negative.\n")
        continue

    if quantity < 0:
        print("Quantity cannot be negative.\n")
        continue

    choice = input("\nWould you like to add  another product? Type Y for yes Q to quit: ")
    print()
    
    products.append(product)
    prices.append(price) 
    quantities.append(quantity)
    
    if choice.upper( )== "Q":
       break 
 
print("---------------------------------------------\n") 
print("Food/Product you order:\n ")   
 
for productName in products:
      print(productName)

for i in range(len(prices)):
      total_amount += prices[i] * quantities[i] 
      


print("---------------------------------------------\n")
    
amount = float(input("\n\nEnter Amount: "))

print(f"Total: {total_amount:.2f}")

if (amount >= total_amount) :
    
    changes = (amount - total_amount)
    print(f"Change: {changes: .2f}\n\n")
    
    
    
    print("---------------------------------------------\n")
    print("Receipt\n")
    print("---------------------------------------------\n")

    print(f"Total: {total_amount:.2f}")
    print(f"Amount: {amount:.2f}")
    print(f"Change: {changes:.2f}\n")    


    print("---------------------------------------------\n")
    print("Ordered Food\n")
    print("---------------------------------------------\n")

    print(f" {'Food':<15} | {'Quantity' :^10} | {'Price':>8}")

    for i in range(len(products)):
      print(f" {products[i] :<15} | {quantities[i]:^10} | {prices[i]:>8.2f}")
      
    print("---------------------------------------------\n\n")

    print("^_^ Comeback Again\n\n")

    print("---------------------------------------------\n\n")
    

else:
    print("Insufficient Money\n")
    
    print("---------------------------------------------\n\n")

    print("^_^ Comeback Again\n\n")

    print("---------------------------------------------\n\n")
    