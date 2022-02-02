import pandas as pd
import plotly.express as px

df=pd.read_csv("COVIDdata.csv")
#fig=px.scatter(df,x='date',y='cases',color="country",size_max=5,title="COVID CASES BY COUNTRY")
fig=px.line(df,x="date",y="cases", color="country", title="COVID CASES BY COUNTRY")
fig.show()