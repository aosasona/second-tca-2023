import pandas

data = pandas.read_excel("./food-data.xlsx")

# Calculate average price increate between September 2021 and 2022
avg_yearly_increase = (data["Price in September 2022 pence)"].mean() - data["Price in September 2021 (pence)"].mean()) / data["Price in September 2021 (pence)"].mean() * 100
print(f"-- Average yearly increase: {avg_yearly_increase:.2f}%")

# Top 3 most expensive food items in September 2021
most_expensive_2021 = data.nlargest(3, "Price in September 2021 (pence)")
print("-- Top 3 expensive food items in 2021\n", most_expensive_2021)

# Top 3 most expensive food items in September 2022
most_expensive_2022 = data.nlargest(3, "Price in September 2022 pence)")
print("-- Top 3 expensive food items in 2022\n", most_expensive_2022)

# Item that has the highest price increase percentage between September 2021 and September 2022
highest_price_increase = (data['Price in September 2022 pence)'] - data['Price in September 2021 (pence)']) / data['Price in September 2021 (pence)'] * 100
highest_price_increase_item = data.loc[highest_price_increase.idxmax()]['Item']
print("-- The food item that has the highest price increase percentage between September 2021 and September 2022 is: ", highest_price_increase_item)

# The average price increase of each food item between September 2021 and September 2022
price_increase_by_items = (data.groupby('Item')['Price in September 2022 pence)'].mean() - data.groupby('Item')['Price in September 2021 (pence)'].mean()) / data.groupby('Item')['Price in September 2021 (pence)'].mean() * 100
print("-- Average price increase of each food item between September 2021 and September 2022\n", price_increase_by_items)
