# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

#items stored as variables 
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

#print(f"{candy1} {candy2} {dry_goods}")

#categories stored as variables 
category1 = categories[0:12]
category2 = categories[13:]

#print(f"{category1} {category2}")

#Create price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

#Output statements 
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")