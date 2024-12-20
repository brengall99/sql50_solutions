# https://leetcode.com/problems/average-time-of-process-per-machine/description/

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:

    starts = activity[activity['activity_type'] == 'start']
    ends = activity[activity['activity_type'] == 'end']

    merged = pd.merge(
        starts, ends, on='machine_id', suffixes=('_start', '_end')
        )

    merged['processing_time'] = (
        merged['timestamp_end'] - merged['timestamp_start']
        )

    result = (
        merged.groupby('machine_id')['processing_time'].mean().round(3).reset_index()
    )

    return result