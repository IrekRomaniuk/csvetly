import pandas as pd
import yaml
import sys
 
if (len(sys.argv)<2):
    sys.exit("CSV file name missing")
df = pd.read_csv(sys.argv[1])
f1=df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).agg(['min','max','mean']).transpose()
f2 = pd.DataFrame(
        {
        "min": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).min().min()],
        "max": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).max().max()],
        "mean": [df.filter(regex='host').rename(columns=lambda x: x.split("#")[1]).mean().mean()],
        },
        index=["ALL"],
   )  
result = pd.concat([f1, f2])
print('### STDOUT')
print(result)

result_json = result.to_json(r'result.json',orient='index')
print('### JSON')
result_json = result.to_json(orient='index')
print(result_json)

result_yaml = yaml.dump(
    result.reset_index().to_dict(orient='records'),
    default_flow_style=False)  
with open('result.yml', 'w') as file:
    yaml.dump(result.reset_index().to_dict(orient='records'), file, default_flow_style=False)   
print('###YAML')      
print(result_yaml)

print('### YML')
print(result.to_xml())
with open('result.xml', 'w') as f:  # Writing in XML file
    for line in result.to_xml():
        f.write(line)