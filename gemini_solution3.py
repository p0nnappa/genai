# Hard-coded data as a Python variable
items = [
    {
        'Category': 'Eating Out',
        'Value': 8.72
    },
    {
        'Category': 'Groceries',
        'Value': 80.17
    },
    {
        'Category': 'Groceries',
        'Value': 13.14
    },
    {
        'Category': 'Eating Out',
        'Value': 16.3
    },
    {
        'Category': 'Utilities',
        'Value': 197.18
    },
    {
        'Category': 'Eating Out',
        'Value': 8.92
    },
    {
        'Category': 'Shopping',
        'Value': 4.34
    },
    {
        'Category': 'Shopping',
        'Value': 144.31
    },
    {
        'Category': 'Eating Out',
        'Value': 8.72
    },
    {
        'Category': 'Unknown',
        'Value': 69.95
    },
    {
        'Category': 'Utilities',
        'Value': 29.99
    },
    {
        'Category': 'Transport',
        'Value': 30.48
    },
    {
        'Category': 'Groceries',
        'Value': 88.79
    },
    {
        'Category': 'Shopping',
        'Value': 3.52
    },
    {
        'Category': 'Groceries',
        'Value': 30.36
    },
    {
        'Category': 'Eating Out',
        'Value': 5.46
    },
    {
        'Category': 'Groceries',
        'Value': 21.92
    },
    {
        'Category': 'Eating Out',
        'Value': 3.27
    },
    {
        'Category': 'Eating Out',
        'Value': 3.27
    },
    {
        'Category': 'Utilities',
        'Value': 123.07
    },
    {
        'Category': 'Entertainment',
        'Value': 222.14
    },
    {
        'Category': 'Eating Out',
        'Value': 21.66
    },
    {
        'Category': 'Shopping',
        'Value': 31.85
    },
    {
        'Category': 'Groceries',
        'Value': 16.33
    },
    {
        'Category': 'Groceries',
        'Value': 13.12
    }
]

# Sum the data by 'Category'
category_sums = {}

for item in items:
    category = item['Category']
    value = item['Value']
    if category not in category_sums:
        category_sums[category] = 0
    category_sums[category] += value

# Print the results
for category, total in category_sums.items():
    print(f'{category}: {total:.2f}')