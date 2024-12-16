# https://leetcode.com/problems/big-countries/description/

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    df_result = world[
        (world['population'] >= 25000000) | (world['area'] >= 3000000)
    ]

    return df_result[['name', 'population', 'area']]
