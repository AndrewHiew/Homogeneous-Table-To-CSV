import tabula
import pandas as pd

dfs = tabula.read_pdf("GOAL.pdf", pages="all", multiple_tables=True)

# Iterate through each table extracted
for i, df in enumerate(dfs):
    df = df.fillna(method='ffill')
    
    print(f"Table {i+1} preview:\n", df.head())
    if i == 0:
        df.columns = [' '.join(df.iloc[0:2, col].astype(str).values).strip() for col in range(df.shape[1])]
        df = df.iloc[2:] 

    # Save each table as an individual CSV
    csv_file_name = f"table_{i+1}.csv"
    df.to_csv(csv_file_name, index=False)
    
    print(f"Table {i+1} saved as {csv_file_name}")
