# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
    merged_df = pd.merge(visits, transactions, how='left', on='visit_id')

    result_df = (
        merged_df[merged_df['transaction_id'].isna()]  
        .groupby(['customer_id'], as_index=False)  
        .agg(count_no_trans=('visit_id', 'nunique'))
    )

    return result_df