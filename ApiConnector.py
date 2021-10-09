import requests
import Key

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': Key.ApiKEY
}


def get_data(country, mode):
    if mode in 'total':
        url = "https://covid-19-data.p.rapidapi.com/country/code"
        querystring = {"code": country}
        print('mama')
    elif mode in 'daily':
        url = "https://covid-19-data.p.rapidapi.com/report/country/code"
        querystring = {"date": "2020-04-01", "code": country}
    else:
        return 'message'

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()
