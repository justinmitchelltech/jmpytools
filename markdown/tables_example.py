from tables import csv_to_md, df_to_md
import os
import pandas as pd 


os.chdir("pytools/markdown")

# Create tables from csv's
csv_to_md("csv_example_2.csv", "tables_example.md", caption="Table from .csv")
csv_to_md("csv_example_1.csv", "tables_example.md", mode='a', caption="Appended Table")

# Create table from Pandas DataFrame
df = pd.DataFrame({ "Col 1": [1, 2, 3], 
                    "Col 2": [4, 5, 6]  })
df_to_md(df, "tables_example.md", mode='a', caption="DataFrame")
