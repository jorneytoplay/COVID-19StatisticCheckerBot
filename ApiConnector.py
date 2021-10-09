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
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()
    elif mode in 'world':
        url = "https://covid-19-data.p.rapidapi.com/totals"
        response = requests.request("GET", url, headers=headers)
        return response.json()
    else:
        return 'message'


