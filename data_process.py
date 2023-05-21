from access import Access
import requests
import pandas as pd
from datetime import datetime, timedelta


class DataProcess:

    def __init__(self, api='https://digital.iservices.rte-france.com/open_api/actual_generation/v1/'):
        self.api = api

    def get_data(self, endpoint='/actual_generations_per_unit',
                 start_date='2022-12-01T00:00:00%2B02:00', end_date='2022-12-10T23:00:00%2B02:00'):

        new_access = Access()
        token = new_access.get_token()
        header_get = {'Authorization': 'Bearer ' + token}
        list_dates = self.generer_liste_dates(start_date, end_date)
        list_data = []
        for i in range(len(list_dates)):
            start_date = list_dates[i][0] + 'T00:00:00%2B02:00'
            end_date = list_dates[i][1] + 'T23:00:00%2B02:00'
            result = requests.get(self.api + endpoint + '?start_date=' + start_date
                                  + '&end_date=' + end_date,
                                  headers=header_get)
            list_data.append(result.json())

        return list_data

    def transform_data(self, endpoint='/actual_generations_per_unit',
                       start_date='2022-12-01T00:00:00%2B02:00',
                       end_date='2022-12-10T23:00:00%2B02:00'):
        list_data = self.get_data(endpoint=endpoint, start_date=start_date, end_date=end_date)
        df = pd.DataFrame({'start_date': pd.Series(dtype='str'),
                           'end_date': pd.Series(dtype='str'),
                           'updated_date': pd.Series(dtype='str'),
                           'value': pd.Series(dtype='float')})
        for k in range(len(list_data)):
            data = list_data[k]
            for i in range(len(data['actual_generations_per_unit'])):
                df1 = pd.DataFrame(data['actual_generations_per_unit'][i]['values'], columns=df.columns)
                df = pd.concat([df, df1])
        mean = df.groupby(['start_date', 'end_date'])['value'].sum()
        return mean

    def generer_liste_dates(self, date_debut, date_fin):
        format_date = '%Y-%m-%d'
        liste_dates = []

        # Conversion des dates en objets datetime
        debut = datetime.strptime(date_debut.split('T')[0], format_date)
        fin = datetime.strptime(date_fin.split('T')[0], format_date)

        # Calcul des dates intermédiaires
        while debut + timedelta(days=7) <= fin:
            liste_dates.append([debut.strftime(format_date), (debut + timedelta(days=6)).strftime(format_date)])
            debut += timedelta(days=7)

        liste_dates.append([debut.strftime(format_date), fin.strftime(format_date)])

        return liste_dates