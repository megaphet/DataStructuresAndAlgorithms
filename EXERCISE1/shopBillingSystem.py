quantities = [6, 10, 17, 3, 90]
total = sum(quantities)
average = total / len(quantities)
minimum = min(quantities)
maximum = max(quantities)
report = (
    f"Quantities sold are: \t{quantities}\n"
    f" Total quantity sold:\t{total}\n"
    f" Average of the quantities sold:\t{average}\n"
    f" The minimum quantity sold:\t{minimum}\n"
    f" The maximum quantity sold:\t{maximum}"
)
print(report)
print("\v")

# Output:
# Quantities sold are: 	[6, 10, 17, 3, 90]
#  Total quantity sold:	126
#  Average of the quantities sold:	25.2
# The minimum quantity sold:	3
#  The maximum quantity sold:	90

summary = f"Total: {total}, Average: {average}, Min: {minimum}, Max: {maximum}"
print(summary)
# Output: Total: 126, Average: 25.2, Min: 3, Max: 90
print("\v")

threshold = 7
if average > threshold and maximum > 11:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")
# Output: Status: Above Standard
print("\v")

items = ["Notebook", "Pen", "Laptop", "Smartphone", "Tablet"]
print("Original list:", items)
print("\v")

# Add new item
items.append("Mouse")

# Remove item if it starts with 'T'
items = [item for item in items if not item.startswith("T")]

# Sort and display
items.sort()
print("Updated list:", items)
# Output: Udated list: ['Laptop', 'Mouse', 'Notebook', 'Pen', 'Smartphone']
print("\v")

import array

# Array of prices
price_array = array.array('i', [1000000, 25000, 750, 300,300000])
array_sum = sum(price_array)

# Compare with list version
price_list = [1000000, 25000, 750, 300,300000]
list_sum = sum(price_list)

price_array_compared_to_price_list = array_sum == list_sum
print("Array sum equals list sum:", price_array_compared_to_price_list)
# Output: Array sum equals list sum: True
print("\v")

records = [
    {"id": 1, "name": "Laptop", "Value": {price_array[0]},"Quantity sold": {quantities[0]}},
    {"id": 2, "name": "Mouse", "Values": {price_array[1]},"Quantity sold": {quantities[1]}},
    {"id": 3, "name": "Notebook", "Value": {price_array[2]},"Quantity sold": {quantities[2]}},
    {"id": 4, "name": "Pen", "Value": {price_array[3]},"Quantity sold": {quantities[3]}},
    {"id": 5, "name": "Smartphone", "Value": {price_array[4]},"Quantity sold": {quantities[4]}},
]

# Update record with id=2
for record in records:
    if record["id"] == 2:
        record["Value"] = 275
    if record["id"] == 5:
        records.remove(record)
print(records)
print("\v")

