# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
category1= "Candy Aisle"
category2= "Pasta Aisle"
candy1= items[0:9]
candy2= items[11:20]
dry_goods=items[22:]

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

message="We have " +candy1+ " for " +bubblegum_price+" in the " +category1
message2 = "We have " + candy2 + " for " + chocolate_price + " in the " + category1
message3 = "We have " + dry_goods + " for " + pasta_price + " in the " + category2
print("We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
print("We have " + candy2 + " for " + chocolate_price + " in the " + category1)
print("We have " + dry_goods + " for " + pasta_price + " in the " + category2)
