## PROBLEM

Create an ETL script, which imports, parses, aggregates and outputs the data in 1 required format, and for bonus points, several optional formats (more details below).

The source data can be seen below in CSV format.

The data is formatted as such to supply an hourly snapshot of the percentage of free memory. Each unique entry (hostname) is stored on each column. Each row below the column represents a snapshot of the collected data, stored via the 'Date / Time' timestamp stored in epoch time.

The format of the column keys are 'node type#hostname#metric', so as an example, the hostname for the string 'host#HOST1#% Free Memory avg 1h' could be identified as HOST1. Columns are comma delimited.

Please create a process which will intake the below provided CSV source, and generate 1 line of output for the following aggregations:

- The minimum value for each unique hostname.
- The maximum value for each unique hostname.
- The average value for each unique hostname.

Additionally, generate the following aggregated values:

- The minimum value for all results.
- The maximum value for all results.
- The average value for all results.

Data for your results should be stored in a result format which you can utilize to output your results to STDOUT. Optionally, we'd like for you also to provide formatted output for some of the following options:

- XML
- JSON
- YAML

These results can be written to external files, for extra credit.

You will be allowed full use of the search engine of your choice.

## SOLUTION

I used pandas which is powerful, flexible and easy to use open source data analysis and manipulation tool.
See code in *csv2agg.py* and snippet creating frame below. Last row provides minimum, maximim andaverag value for all results.
```
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
```

## RESULTS

See results in json, xml and yml formats TO STDOUT (also in files result.*)

```
pip install -r requirements.txt
python csv2agg.py data.csv
### STDOUT
          min    max       mean
HOST1   77.85  77.89  77.862500
HOST2   77.69  77.73  77.708333
HOST3   77.75  77.79  77.774167
HOST4   78.03  78.06  78.045000
HOST5   85.92  87.47  86.842500
HOST6   93.28  93.64  93.495000
HOST7   96.50  96.83  96.682917
HOST8   90.07  92.09  90.807917
HOST9   96.10  96.52  96.349130
HOST10  99.23  99.57  99.404000
HOST11  94.84  94.98  94.901250
HOST12  54.27  54.84  54.766250
HOST13  39.54  40.80  40.522917
HOST14  51.16  51.38  51.274167
HOST15  81.26  81.30  81.288750
HOST16  85.09  93.46  92.102500
HOST17  60.58  61.20  61.169583
HOST18  79.35  97.42  82.982917
HOST19  82.42  83.14  82.770833
HOST20  71.12  73.03  71.924167
HOST21  54.34  61.11  57.691667
HOST22  57.55  61.31  59.982917
HOST23  35.76  41.91  37.352083
HOST24  33.64  40.69  36.760000
HOST25  32.32  45.79  36.956250
HOST26  41.43  46.13  43.363750
HOST27  43.53  47.21  45.066250
HOST28  43.23  49.01  45.638333
HOST29  31.82  41.61  36.365455
ALL     31.82  99.57  68.546604
### JSON
{"HOST1":{"min":77.85,"max":77.89,"mean":77.8625},"HOST2":{"min":77.69,"max":77.73,"mean":77.7083333333},"HOST3":{"min":77.75,"max":77.79,"mean":77.7741666667},"HOST4":{"min":78.03,"max":78.06,"mean":78.045},"HOST5":{"min":85.92,"max":87.47,"mean":86.8425},"HOST6":{"min":93.28,"max":93.64,"mean":93.495},"HOST7":{"min":96.5,"max":96.83,"mean":96.6829166667},"HOST8":{"min":90.07,"max":92.09,"mean":90.8079166667},"HOST9":{"min":96.1,"max":96.52,"mean":96.3491304348},"HOST10":{"min":99.23,"max":99.57,"mean":99.404},"HOST11":{"min":94.84,"max":94.98,"mean":94.90125},"HOST12":{"min":54.27,"max":54.84,"mean":54.76625},"HOST13":{"min":39.54,"max":40.8,"mean":40.5229166667},"HOST14":{"min":51.16,"max":51.38,"mean":51.2741666667},"HOST15":{"min":81.26,"max":81.3,"mean":81.28875},"HOST16":{"min":85.09,"max":93.46,"mean":92.1025},"HOST17":{"min":60.58,"max":61.2,"mean":61.1695833333},"HOST18":{"min":79.35,"max":97.42,"mean":82.9829166667},"HOST19":{"min":82.42,"max":83.14,"mean":82.7708333333},"HOST20":{"min":71.12,"max":73.03,"mean":71.9241666667},"HOST21":{"min":54.34,"max":61.11,"mean":57.6916666667},"HOST22":{"min":57.55,"max":61.31,"mean":59.9829166667},"HOST23":{"min":35.76,"max":41.91,"mean":37.3520833333},"HOST24":{"min":33.64,"max":40.69,"mean":36.76},"HOST25":{"min":32.32,"max":45.79,"mean":36.95625},"HOST26":{"min":41.43,"max":46.13,"mean":43.36375},"HOST27":{"min":43.53,"max":47.21,"mean":45.06625},"HOST28":{"min":43.23,"max":49.01,"mean":45.6383333333},"HOST29":{"min":31.82,"max":41.61,"mean":36.3654545455},"ALL":{"min":31.82,"max":99.57,"mean":68.5466035051}}
### YML
- index: HOST1
  max: 77.89
  mean: 77.8625
  min: 77.85
- index: HOST2
  max: 77.73
  mean: 77.70833333333333
  min: 77.69
- index: HOST3
  max: 77.79
  mean: 77.77416666666666
  min: 77.75
- index: HOST4
  max: 78.06
  mean: 78.045
  min: 78.03
- index: HOST5
  max: 87.47
  mean: 86.84250000000002
  min: 85.92
- index: HOST6
  max: 93.64
  mean: 93.495
  min: 93.28
- index: HOST7
  max: 96.83
  mean: 96.68291666666669
  min: 96.5
- index: HOST8
  max: 92.09
  mean: 90.80791666666669
  min: 90.07
- index: HOST9
  max: 96.52
  mean: 96.3491304347826
  min: 96.1
- index: HOST10
  max: 99.57
  mean: 99.40400000000001
  min: 99.23
- index: HOST11
  max: 94.98
  mean: 94.90124999999999
  min: 94.84
- index: HOST12
  max: 54.84
  mean: 54.76624999999999
  min: 54.27
- index: HOST13
  max: 40.8
  mean: 40.52291666666667
  min: 39.54
- index: HOST14
  max: 51.38
  mean: 51.274166666666666
  min: 51.16
- index: HOST15
  max: 81.3
  mean: 81.28875000000001
  min: 81.26
- index: HOST16
  max: 93.46
  mean: 92.1025
  min: 85.09
- index: HOST17
  max: 61.2
  mean: 61.16958333333334
  min: 60.58
- index: HOST18
  max: 97.42
  mean: 82.98291666666667
  min: 79.35
- index: HOST19
  max: 83.14
  mean: 82.77083333333333
  min: 82.42
- index: HOST20
  max: 73.03
  mean: 71.92416666666666
  min: 71.12
- index: HOST21
  max: 61.11
  mean: 57.69166666666666
  min: 54.34
- index: HOST22
  max: 61.31
  mean: 59.982916666666675
  min: 57.55
- index: HOST23
  max: 41.91
  mean: 37.35208333333333
  min: 35.76
- index: HOST24
  max: 40.69
  mean: 36.76
  min: 33.64
- index: HOST25
  max: 45.79
  mean: 36.956250000000004
  min: 32.32
- index: HOST26
  max: 46.13
  mean: 43.36375
  min: 41.43
- index: HOST27
  max: 47.21
  mean: 45.066250000000004
  min: 43.53
- index: HOST28
  max: 49.01
  mean: 45.63833333333334
  min: 43.23
- index: HOST29
  max: 41.61
  mean: 36.36545454545455
  min: 31.82
- index: ALL
  max: 99.57
  mean: 68.54660350506565
  min: 31.82

### XML
<?xml version='1.0' encoding='utf-8'?>
<data>
  <row>
    <index>HOST1</index>
    <min>77.85</min>
    <max>77.89</max>
    <mean>77.8625</mean>
  </row>
  <row>
    <index>HOST2</index>
    <min>77.69</min>
    <max>77.73</max>
    <mean>77.70833333333333</mean>
  </row>
  <row>
    <index>HOST3</index>
    <min>77.75</min>
    <max>77.79</max>
    <mean>77.77416666666666</mean>
  </row>
  <row>
    <index>HOST4</index>
    <min>78.03</min>
    <max>78.06</max>
    <mean>78.045</mean>
  </row>
  <row>
    <index>HOST5</index>
    <min>85.92</min>
    <max>87.47</max>
    <mean>86.84250000000002</mean>
  </row>
  <row>
    <index>HOST6</index>
    <min>93.28</min>
    <max>93.64</max>
    <mean>93.495</mean>
  </row>
  <row>
    <index>HOST7</index>
    <min>96.5</min>
    <max>96.83</max>
    <mean>96.68291666666669</mean>
  </row>
  <row>
    <index>HOST8</index>
    <min>90.07</min>
    <max>92.09</max>
    <mean>90.80791666666669</mean>
  </row>
  <row>
    <index>HOST9</index>
    <min>96.1</min>
    <max>96.52</max>
    <mean>96.3491304347826</mean>
  </row>
  <row>
    <index>HOST10</index>
    <min>99.23</min>
    <max>99.57</max>
    <mean>99.40400000000001</mean>
  </row>
  <row>
    <index>HOST11</index>
    <min>94.84</min>
    <max>94.98</max>
    <mean>94.90124999999999</mean>
  </row>
  <row>
    <index>HOST12</index>
    <min>54.27</min>
    <max>54.84</max>
    <mean>54.76624999999999</mean>
  </row>
  <row>
    <index>HOST13</index>
    <min>39.54</min>
    <max>40.8</max>
    <mean>40.52291666666667</mean>
  </row>
  <row>
    <index>HOST14</index>
    <min>51.16</min>
    <max>51.38</max>
    <mean>51.274166666666666</mean>
  </row>
  <row>
    <index>HOST15</index>
    <min>81.26</min>
    <max>81.3</max>
    <mean>81.28875000000001</mean>
  </row>
  <row>
    <index>HOST16</index>
    <min>85.09</min>
    <max>93.46</max>
    <mean>92.1025</mean>
  </row>
  <row>
    <index>HOST17</index>
    <min>60.58</min>
    <max>61.2</max>
    <mean>61.16958333333334</mean>
  </row>
  <row>
    <index>HOST18</index>
    <min>79.35</min>
    <max>97.42</max>
    <mean>82.98291666666667</mean>
  </row>
  <row>
    <index>HOST19</index>
    <min>82.42</min>
    <max>83.14</max>
    <mean>82.77083333333333</mean>
  </row>
  <row>
    <index>HOST20</index>
    <min>71.12</min>
    <max>73.03</max>
    <mean>71.92416666666666</mean>
  </row>
  <row>
    <index>HOST21</index>
    <min>54.34</min>
    <max>61.11</max>
    <mean>57.69166666666666</mean>
  </row>
  <row>
    <index>HOST22</index>
    <min>57.55</min>
    <max>61.31</max>
    <mean>59.982916666666675</mean>
  </row>
  <row>
    <index>HOST23</index>
    <min>35.76</min>
    <max>41.91</max>
    <mean>37.35208333333333</mean>
  </row>
  <row>
    <index>HOST24</index>
    <min>33.64</min>
    <max>40.69</max>
    <mean>36.76</mean>
  </row>
  <row>
    <index>HOST25</index>
    <min>32.32</min>
    <max>45.79</max>
    <mean>36.956250000000004</mean>
  </row>
  <row>
    <index>HOST26</index>
    <min>41.43</min>
    <max>46.13</max>
    <mean>43.36375</mean>
  </row>
  <row>
    <index>HOST27</index>
    <min>43.53</min>
    <max>47.21</max>
    <mean>45.066250000000004</mean>
  </row>
  <row>
    <index>HOST28</index>
    <min>43.23</min>
    <max>49.01</max>
    <mean>45.63833333333334</mean>
  </row>
  <row>
    <index>HOST29</index>
    <min>31.82</min>
    <max>41.61</max>
    <mean>36.36545454545455</mean>
  </row>
  <row>
    <index>ALL</index>
    <min>31.82</min>
    <max>99.57</max>
    <mean>68.54660350506565</mean>
  </row>
</data>
```