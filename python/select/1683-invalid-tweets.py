# https://leetcode.com/problems/invalid-tweets/description/

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    # Show 'tweet_id' for tweets that are longer than 15 chars
    df_result = tweets[tweets['content'].str.len() > 15][['tweet_id']]

    return df_result