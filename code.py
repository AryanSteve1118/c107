import csv
import pandas as pd 
import plotly.graph_objects as go 

def setup(id):
    df=pd.read_csv("data.csv")
    s_df=df.loc[df["student_id"]==id]
    x1=s_df.groupby("level")["attempt"].mean()
    print(x1)
    id=input("Enter Student Id : ")
    setup(id)

    fig=go.Figure(go.Bar(
    x=x1,y=['Level 1','Level 2','Level 3','Level 4'],orientation="h"
    ))

    fig.show()