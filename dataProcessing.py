import numpy as np
import pandas as pd

def GetFiltered_clpr(data):
    result = {}
    for row in data['output2']:
        # print(row)
        key = row['stck_bsop_date']
        # print(newKey)
        result[key] = row['stck_clpr']
    print(result)
    columns = ["dates","values"]
    df = pd.DataFrame(columns=columns)
    result.keys()
    result.values()
    # print(result.keys(),result.values())
    return result