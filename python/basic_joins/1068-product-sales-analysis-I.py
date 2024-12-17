# https://leetcode.com/problems/product-sales-analysis-i/description/

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    merged_df = pd.merge(sales, product, how='left', on='product_id')
    result_df = merged_df[['product_name', 'year', 'price']]

    return result_df