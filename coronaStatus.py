import requests
from datetime import date, timedelta

def status(data):
    date={"date":data,"q":"Poland","iso":"POL"}
    r = requests.get('https://covid-api.com/api/reports',date)
    data = r.json()
    return data
def main():
    dzis = date.today()
    wczoraj = date.today() - timedelta(days=1)
    wynik = {"data":"","zarazony":"","smierci":"","wyzdrowiali":""}
    data = status(dzis)
    if data['data']:
        for d in data['data']:
            wynik["data"] = dzis
            wynik["zarazony"] = d['confirmed']
            wynik["smierci"] = d['deaths']
            wynik["wyzdrowiali"] = d['recovered']
            
    else:
        data = status(wczoraj)
        if data['data']:
            for d in data['data']:
                wynik["data"] = str(wczoraj)
                wynik["zarazony"] = d['confirmed']
                wynik["smierci"] = d['deaths']
                wynik["wyzdrowiali"] = d['recovered']
                
    for w,i in wynik.items():
        print(w,i)
if __name__ == "__main__":
    main()