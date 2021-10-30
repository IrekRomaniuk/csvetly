import pandas as pd
import sys, os
 
if (len(sys.argv)<2):
    sys.exit("CSV file name missing")
df = pd.read_csv(sys.argv[1])
f1=df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).agg(['min','max','mean']).transpose()
#print(f1)
f2 = pd.DataFrame(
        {
        "min": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).min().min()],
        "max": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).max().max()],
        "mean": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).mean().mean()],
        },
        index=["ALL"],
   )
#print(f2)   
result = pd.concat([f1, f2])
print(result)