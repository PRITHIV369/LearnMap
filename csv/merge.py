import pandas as pd
def merge_csv_on_column(file1, file2, column, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    merged_df = pd.merge(df1, df2, on=column)
    merged_df.to_csv(output_file, index=False)
    print("Merged CSV files successfully!")
file1 = "csv/merged_file6.csv"
file2 = "csv/cooking.csv"
column = "skill"
output_file = "csv/merged_file9.csv"
merge_csv_on_column(file1, file2, column, output_file)
