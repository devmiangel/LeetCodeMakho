# Last updated: 21/9/2026, 23:58:40
1import pandas as pd
2
3def selectData(students: pd.DataFrame) -> pd.DataFrame:
4
5    new_df = students[students['student_id'] == 101][['name', 'age']]
6    
7    return new_df
8    