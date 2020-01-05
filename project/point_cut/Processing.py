import pandas as pd
import numpy as np

class DataProcessing():
    def processing(OAI,TFI,CTI):
        CTI["clnt_age"][CTI["clnt_age"]=="10"] = "10-20"
        CTI["clnt_age"][CTI["clnt_age"]=="20"] = "10-20"
        CTI["clnt_age"][CTI["clnt_age"]=="50"] = "50-60"
        CTI["clnt_age"][CTI["clnt_age"]=="60"] = "50-60"

        TFI = TFI[TFI["pd_c"].notnull()]
        TFI = TFI[(TFI["buy_am"]<100000000)&(TFI["buy_am"]!=0)&(TFI["buy_ct"]!=0)]
        TFI = TFI[TFI["pd_c"]!="unknown"]

        oai7 = OAI[OAI["action_type"]==7].reset_index(drop=True)
        oai6 = OAI[OAI["action_type"]==6]
            # 환불 내역 제거
        for i in range(oai7.shape[0]):
            oai6 = oai6.drop(oai6[((oai6["clnt_id"]==oai7["clnt_id"][i])&(oai6["trans_id"]==oai7["trans_id"][i]))].index)
            TFI = TFI.drop(TFI[((TFI["clnt_id"]==oai7["clnt_id"][i])&(TFI["trans_id"]==oai7["trans_id"][i]))].index)
        oai0 = OAI[(OAI["action_type"]!=7)&(OAI["action_type"]!=6)]
        OAI = pd.concat([oai0,oai6],axis=0)
        return OAI, TFI, CTI
