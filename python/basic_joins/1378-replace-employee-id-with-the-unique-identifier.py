# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    merged_df = pd.merge(employees, employee_uni, how='left', on='id')
    result_df = merged_df[['unique_id','name']]

    return result_df