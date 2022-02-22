from mdtables import csv_to_md, df_to_md
import os
import pandas as pd 


os.chdir("jmpytools/genpurpose")

# Create tables from csv's
csv_to_md("mdtables_example-csv-table_2.csv", "mdtables_examples.md", caption="Table from .csv")
csv_to_md("mdtables_example-csv-table_1.csv", "mdtables_examples.md", mode='a', caption="Appended Table")

# Create table from Pandas DataFrame
df = pd.DataFrame({ "Col 1": [1, 2, 3], 
                    "Col 2": [4, 5, 6]  })
df_to_md(df, "mdtables_examples.md", mode='a', caption="DataFrame")
