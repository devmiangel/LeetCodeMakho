# Last updated: 21/9/2026, 23:46:31
1import pandas as pd
2
3def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
4    return employees.head(3)