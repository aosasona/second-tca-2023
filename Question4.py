import pandas

data = pandas.read_excel("./food-data.xlsx")


"""
Calculate average price increase between September 2021 and 2022
To understand how inflation has affected the price of these items
"""
avg_yearly_increase = (data["Price in September 2022 pence)"].mean() - data["Price in September 2021 (pence)"].mean()) / data["Price in September 2021 (pence)"].mean() * 100
print(f"-- Average yearly increase: {avg_yearly_increase:.2f}%")



"""
Top 3 most expensive food items in September 2021 
To understand which items had the highest profit margins or were considered "better" or as "luxury" in this time frame (2021)
"""
most_expensive_2021 = data.nlargest(3, "Price in September 2021 (pence)")
print("-- Top 3 expensive food items in 2021\n", most_expensive_2021)



"""
Top 3 most expensive food items in September 2022
To understand which items had the highest profit margins or were considered "better" or as "luxury" in this time frame (2022)
"""
most_expensive_2022 = data.nlargest(3, "Price in September 2022 pence)")
print("-- Top 3 expensive food items in 2022\n", most_expensive_2022)



"""
Item that has the highest price increase percentage between September 2021 and September 2022
To identify which item is most affected by price inflation
"""
highest_price_increase = (data['Price in September 2022 pence)'] - data['Price in September 2021 (pence)']) / data['Price in September 2021 (pence)'] * 100
highest_price_increase_item = data.loc[highest_price_increase.idxmax()]['Item']
print(f"-- The food item that has the highest price increase percentage between September 2021 and September 2022 is: {highest_price_increase_item}")



"""
Item that has the highest price decrease percentage between September 2021 and September 2022
To identify which item is least affected by price inflation
"""
highest_price_decrease = (data['Price in September 2022 pence)'] - data['Price in September 2021 (pence)']) / data['Price in September 2021 (pence)'] * 100
highest_price_decrease_item = data.loc[highest_price_decrease.idxmin()]['Item']
print(f"-- The food item that has the highest price decrease percentage between September 2021 and September 2022 is: {highest_price_decrease_item}")



"""
The average price increase of each food item between September 2021 and September 2022
To get an in-depth look into how each item was affected by price inflation (negatively and positively) 
"""
price_increase_by_items = (data.groupby('Item')['Price in September 2022 pence)'].mean() - data.groupby('Item')['Price in September 2021 (pence)'].mean()) / data.groupby('Item')['Price in September 2021 (pence)'].mean() * 100
print("-- Average price increase of each food item between September 2021 and September 2022\n", price_increase_by_items)
