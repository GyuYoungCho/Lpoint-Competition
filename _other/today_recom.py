import pandas as pd
from datetime import datetime

class TodayRecommend():
    def __init__(self):
        now = datetime.now()
        self.hour = now.hour
        self.weekday = now.weekday()
    def today_recommend(self, TFI):
        tfi1 = TFI[['de_tm','de_dt','pd_c']]
        tfi1['de_dt'] = pd.to_datetime(tfi1['de_dt'], format='%Y%m%d')
        tfi1['hour'] = (pd.to_datetime(tfi1['de_tm'])).dt.strftime("%H")
        tfi1['day_of_week'] = tfi1["de_dt"].dt.weekday
        tfi1['count'] = 1

        tfi_group = tfi1.groupby(["day_of_week","pd_c"]).sum()["count"]
        weekday_population = tfi_group[self.weekday]
        weekday_population.sort_values(ascending=False,inplace=True)

        tfi_group2 = tfi1.groupby(["hour","pd_c"]).sum()["count"]
        hour_population = tfi_group2[str(self.hour)]
        hour_population.sort_values(ascending=False,inplace=True)
        return pd.Series(weekday_population[:7].index), pd.Series(hour_population[:7].index)
