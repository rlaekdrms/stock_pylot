from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import pandas as df
def GetFiltered_clpr(data):
    columns = ["dates","values"]
    result = {}
    df = pd.DataFrame(columns=columns)
    for row in data['output2']:
        new_row =  pd.DataFrame([{"dates":int(row['stck_bsop_date']),"values":int(row['stck_clpr'])}])
        df = pd.concat([df,new_row],ignore_index=True)
        # print(row)
        key = row['stck_bsop_date']
        # print(newKey)
        result[key] = row['stck_clpr']
    df.sort_values("dates",ascending=True)
    print(df)
    plt.plot(df["values"],"orange")
    plt.show()
    return result
