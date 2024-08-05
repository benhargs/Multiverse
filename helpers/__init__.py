import pandas as pd
 
def read_in_csv(filename):
    df = pd.read_csv(filename)
    return df
 