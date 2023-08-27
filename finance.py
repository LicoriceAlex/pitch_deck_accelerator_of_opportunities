import numpy as np

import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import pandas as pd
pd.options.plotting.backend = "plotly"

# revenue = 100_000
# revenue_new = 110_000
# clients = 300

def cagr(new, old, t=1):
    return (new / old) ** (1 / t) - 1

def calc_stuff(revenue=100_000, revenue_new=110_000, clients=300):
    apru = revenue / clients
    
    churn = 0.15
    lt = 1 / churn
    ltv = apru * lt
    
    c = cagr(revenue_new, revenue)
    y = np.array([revenue, revenue_new, revenue_new * (1 + c), revenue_new * (1 + c) * (1 + c), revenue_new * (1 + c) * (1 + c) * (1 + c)])
    
    fig = pd.DataFrame(y, index=[2022, 2023, 2024, 2025, 2026]).plot.bar(labels = {"value" : "Выручка", "index" : "Год"})
    fig.update_layout(showlegend=False)
    fig.write_image("revenue.png")
    
    return apru, churu, ltv

def make_req(money : int, raund : str, need : str):
    d = {}
    
    need = need.split(';')
    for n in need:
        name, perc = n.split(' ')
        perc = float(perc)
        d[name] = perc
        
    df = pd.DataFrame(d, index=["Part"]).T

    df["name"] = df.index
    
    # return df

    fig = px.pie(df, values='Part', names="name", title=f"{money} на {raund} рануд")
    fig.write_image("pie.png")
    
    # return apru, churn, ltv

# calc_stuff(revenue=100_000, revenue_new=revenue * 1.1, clients=300)
# make_req(need = "маркетинг 0.5;прдажи 0.5;себе 0.5", money = "100 млн", raund = "seed")