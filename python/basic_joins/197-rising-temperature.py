# https://leetcode.com/problems/rising-temperature/description/

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)

    result_df = weather[
        (weather.temperature.diff() > 0) & (weather.recordDate.diff().dt.days == 1)]

    return result_df[['id']]