import os
import pandas as pd

# Example complex list of items with attributes
my_list = [
    {'name': 'apple', 'color': 'red', 'price': 0.75},
    {'name': 'banana', 'color': 'yellow', 'price': 0.50},
    {'name': 'cherry', 'color': 'red', 'price': 1.50},
    {'name': 'orange', 'color': 'orange', 'price': 2.50},

]

output_folder = 'data'
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, 'output.csv')

# Convert list of dictionaries to a DataFrame and save as CSV
df = pd.DataFrame(my_list)
df.to_csv(output_path, index=False)

print(f'Saved list to {output_path}')
