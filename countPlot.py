
import pandas as pd

import seaborn as sns



df = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_3011530.csv")

sns.countplot(y="IncomeGroup", hue="Region", data=df);