import pandas as pd

# Read the CSV file
df = pd.read_csv('./data/Video_Games_Sales_as_at_22_Dec_2016.csv')

# Select the desired columns
selected_columns = ['Year_of_Release', 'Platform', 'Genre', 'Global_Sales']
df_selected = df[selected_columns]

# Drop rows with missing values
df_selected = df_selected.dropna()

# Convert Year_of_Release to string and modify the format
df_selected['Year_of_Release'] = df_selected['Year_of_Release'].astype(int).astype(str) + '-01-01'

# Multiply Global_Sales by 1000000
df_selected['Global_Sales'] = df_selected['Global_Sales'] * 1000000

# Sort by Year_of_Release
df_selected = df_selected.sort_values('Year_of_Release')

# Write the selected columns to a new CSV file
df_selected.to_csv('./data/output3.csv', index=False)
