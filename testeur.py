from access import Access
from data_process import DataProcess


def test_access():
    new_access = Access()
    token = new_access.get_token()
    assert isinstance(token, str) == True


def test_generer_liste_dates():
    data_process = DataProcess()
    liste_date = data_process.generer_liste_dates(date_debut="2022-08-12", date_fin="2022-10-5")
    liste_date_expected = [['2022-08-12', '2022-08-18'], ['2022-08-19', '2022-08-25'],
                          ['2022-08-26', '2022-09-01'], ['2022-09-02', '2022-09-08'],
                          ['2022-09-09', '2022-09-15'], ['2022-09-16', '2022-09-22'],
                          ['2022-09-23', '2022-09-29'], ['2022-09-30', '2022-10-05']]
    assert liste_date == liste_date_expected


def test_get_data():
    data_process = DataProcess()
    list_data = data_process.get_data(endpoint='/actual_generations_per_unit',
                                      start_date='2022-12-01T00:00:00%2B02:00',
                                      end_date='2022-12-10T23:00:00%2B02:00')
    assert len(list_data) != 0


def test_transform_data():
    data_process = DataProcess()
    data = data_process.transform_data(endpoint='/actual_generations_per_unit',
                                       start_date='2022-12-01T00:00:00%2B02:00',
                                       end_date='2022-12-10T23:00:00%2B02:00')
    assert (not data.isnull().any().any()) == True
