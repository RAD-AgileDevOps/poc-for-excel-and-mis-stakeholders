'''
Date: 2026-10-11 08:30
Excel & MIS Consultant:   Roger De Four
Description: 
            
            Stakeholder Demonstrations ; adhoc management report on finacial dataset for fraud detection and analysis
            This script converts a Parquet file to a CSV file for further analysis and reporting. It reads the Parquet file into a pandas DataFrame, prints the number of rows and columns, and then saves the DataFrame as a CSV file with UTF-8 encoding and a specified date format.
            
            
 Author : Claude AI  generated - cse_01VHdwZeYiFKZ878piJs7d4f
         
'''






import pandas as pd

src = r"C:\Users\Admin\Documents\excel-and-mis-consultant-stakeholder-demonstrations\universal_enterprise_erp_fraud_dataset.parquet"
dst = r"C:\Users\Admin\Documents\excel-and-mis-consultant-stakeholder-demonstrations\erp_fraud_dataset.csv"

df = pd.read_parquet(src)
print(f"Loaded {len(df):,} rows x {df.shape[1]} columns")

df.to_csv(dst, index=False, encoding="utf-8-sig", date_format="%Y-%m-%d %H:%M:%S")
print("Saved:", dst)