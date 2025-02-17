import numpy as np
import pandas as pd

def GetFiltered_clpr(data):
    result = {}
    columns = ["dates","values"]
    df = pd.DataFrame(columns=columns)

    print(df)

    for row in data['output2']:
        newRow = pd.DataFrame([{"dates": row['stck_bsop_date'], "values": row['stck_clpr']}])
        # print(newRow)
        df = pd.concat([df, newRow], ignore_index=True)
        # df = pd.concat([df, newRow])
    
    print(df)
    return result