import pandas as pd
import sys, os
 
if (len(sys.argv)<2):
    sys.exit("CSV file name missing")
df = pd.read_csv(sys.argv[1])
print(df)
#print(df['SourceIP'][1])
sys.exit("Exited")
print(f"File: {sys.argv[1]}\n{df.count()} lines")
for index, row in df.iterrows():
    #   if row['Disabled'] =='skip':
    #         continue
    pass