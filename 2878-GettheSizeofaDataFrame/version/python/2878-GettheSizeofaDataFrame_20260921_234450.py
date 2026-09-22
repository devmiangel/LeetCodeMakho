# Last updated: 21/9/2026, 23:44:50
1import pandas as pd
2
3def getDataframeSize(players: pd.DataFrame) -> List[int]:
4    data = [len(players.index), len(players.columns)]
5    return data
6    