# https://leetcode.com/problems/article-views-i/description/

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    # Filter the rows so that author_id and viewer_id are the same
    filtered = views[
        views['author_id'] == views['viewer_id']]

    # Rename the author_id column to just id
    result = filtered[
        ['author_id']].rename(columns={'author_id': 'id'})
        
    # Order the column and drop any duplicates
    result = result.drop_duplicates().sort_values(by='id').reset_index(drop=True)
    
    return result