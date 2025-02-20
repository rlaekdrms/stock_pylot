from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def GetFiltered_clpr(data):
    columns = ["dates","values"]
    df = pd.DataFrame(columns=columns)
    
    for row in data['output2']:
        new_row =  pd.DataFrame([{"dates":int(row['stck_bsop_date']),"values":int(row['stck_clpr'])}])
        df = pd.concat([df,new_row],ignore_index=True)

    df_sorted_by_values = df.sort_values(by=["dates"], ascending=True)
    
    plt.plot(df["dates"], df["values"],"orange")
    # plt.plot(df_sorted_by_values["dates"], df_sorted_by_values["values"],"b")
    plt.show()

    return df
