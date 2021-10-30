import pandas as pd
import sys, os
 
if (len(sys.argv)<2):
    sys.exit("CSV file name missing")
df = pd.read_csv(sys.argv[1])
#print(df)
#print(df.filter(regex='host').min())
print(df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).agg(['min','max','mean']))
print(df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).min().min(),df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).max().max(),
df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).mean().mean())