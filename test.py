# Create a dictionary with 20 keys, each containing a list of 5 values
dic_test = {i: [j for j in range(i * 5, i * 5 + 5)] for i in range(20)}

# Value to search for
target_value = 64

# Initialize iteration counter
iterations = 0
found = False

# Search for the target value
for key, values in dic_test.items():
    for value in values:
        iterations += 1
        if value == target_value:
            found = True
            print(f"Found {target_value} at key {key} after {iterations} iterations.")
            break
    if found:
        break

if not found:
    print(f"{target_value} not found after {iterations} iterations.")