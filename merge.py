import yfinance as yf
import pandas as pd
from glob import glob


# data=yf.download('RELIANCE.NS')
# data.to_csv('RELIANCE.csv')

equity_details=pd.read_csv('T20-GL-gainers-NIFTY-13-Apr-2023.csv')


for name in equity_details.Symbol[:5]:
        try:
                data=yf.download(f'{name}.NS')
                data.to_csv(f'data_file_{name}.csv')
        except Exception as e:
                print(f'{name}===>{e}')


stock_files=sorted(glob('data_file_*'))


combined_csv=pd.concat((pd.read_csv(file).assign(filename=file)
      for file in stock_files),ignore_index=True)

combined_csv.to_csv("combined_csv.csv",index=False,encoding="utf-8-sig")

# with open('combined_csv.csv', 'rU') as myfile:
#     filtered = (line.replace('\r', '') for line in myfile)
#     for row in csv.reader(filtered):

df=pd.read_csv("combined_csv.csv")
for col in df:
        df[col]=df[col].replace("\n","",regex=True).replace(".csv","",regex=True)
df.to_csv('combined_csv2.csv',index=False)
# print(data)

# columns.str.replace('.csv', '')
# extension='csv'

# all_filenames=[i for i in glob.glob('*.{}',format(extension))]

# combined_csv=pd.concat([pd.read_csv(f) for f in all_filenames])

# combined_csv.to_csv("combined_csv.csv",index=False,encoding="utf-8-sig")











