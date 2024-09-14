import tabula
import pandas as pd


def extract_tables_from_pdf(pdf_file_path):
    # Read the PDF file and extract multiple tables
    dfs = tabula.read_pdf(pdf_file_path, pages="all", multiple_tables=True)

    for i, df in enumerate(dfs):
        table_num = i + 1
        print(f"Table {table_num} after adjustments:\n", df.head())
        
        csv_file_name = f"table_{table_num}.csv"
        df.to_csv(csv_file_name, index=False)
        
        print(f"Table {table_num} saved as {csv_file_name}")

extract_tables_from_pdf("GOAL.pdf")
