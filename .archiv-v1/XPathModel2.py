from dataclasses import dataclass


@dataclass
class XPathModel2:
    data_wplywu: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]"          #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[1]
    inwestor: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]"             #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[2]
    nazwa_zamieszkania: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]"   #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[3]
    stan_prawny: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/span[2]"  #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[4]
    data_wydania_decyzji: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]" #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[5]
    url: str = "/html/body/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/a"                #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[6]/a

    def __init__(self, row_index):
        self.data_wplywu: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[1]"          #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[1]
        self.inwestor: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[2]"             #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[2]
        self.nazwa_zamieszkania: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[3]"   #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[3]
        self.stan_prawny: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[4]/span[2]"  #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[4]
        self.data_wydania_decyzji: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[5]" #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[5]
        self.url: str = f"/html/body/div/div[2]/div/div[3]/table/tbody/tr[{row_index}]/td[6]/a"                #/html/body/div/div[2]/div/div[3]/table/tbody/tr[10]/td[6]/a