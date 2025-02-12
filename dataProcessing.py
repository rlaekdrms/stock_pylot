import numpy

def GetFiltered_clpr(data):
    result = {}
    for row in data['output2']:
        # print(row)
        key = row['stck_bsop_date']
        # print(newKey)
        result[key] = row['stck_clpr']
    # print(result)
    return result