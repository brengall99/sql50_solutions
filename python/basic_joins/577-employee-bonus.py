# https://leetcode.com/problems/employee-bonus/description/

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    df_merged = pd.merge(employee, bonus ,how='left', on='empId')

    df_filtered = df_merged[
        (df_merged['bonus'] < 1000) |
        (df_merged['bonus'].isna())
        ]

    return df_filtered[['name', 'bonus']]