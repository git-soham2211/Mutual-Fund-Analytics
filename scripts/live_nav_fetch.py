import requests
import pandas as pd

funds = {
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_LargeCap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for name, code in funds.items():

    try:

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"../data/raw/{name}_live_nav.csv",
            index=False
        )

        print(f"{name} downloaded successfully")

    except Exception as e:

        print(f"Error in {name}")
        print(e)