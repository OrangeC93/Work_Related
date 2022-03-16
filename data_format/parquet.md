https://towardsdatascience.com/csv-files-for-storage-no-thanks-theres-a-better-option-72c78a414d1d#:~:text=Both%20CSV%20and%20Parquet%20formats,organize%20the%20data%20in%20columns.&text=In%20a%20nutshell%2C%20column%20storage,be%20done%20for%20each%20column.

CSVs are what you call row storage, while Parquet files organize the data in columns.
- Column storage files are more lightweight, as adequate compression can be done for each column. 
- Parquet is a more efficient data format for bigger files. You will save both time and money by using Parquet over CSVs.

![image](pics/raw_data.png)
```python
import pandas as pd
df = pd.read_csv('data/prices.csv')
df.head()

df.to_parquet('data/prices.parquet')

df_parquet = pd.read_parquet('data/prices.parquet')
df_parquet.head()
```
![image](pics/csv_parquet.png)


Both datasets are identical. The command df.equals(df_parquet) will print True to the console.
