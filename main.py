import pandas as pd
import seaborn as sb


data = pd.read_csv("modified_data.csv", delimiter=',')

# Group the DataFrame by 'Sex'
groups = data.groupby('sex')

# Access the DataFrames for each group
male_df = groups.get_group(0)
female_df = groups.get_group(1)


male_df.to_csv('male_data.csv', index=False)
female_df.to_csv('female_data.csv', index=False)

