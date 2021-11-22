import os
import csv
from guide_p.models import Stations


def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    with open(file_obj, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for csv_line in reader:
            try:
                station = csv_line['Station'].capitalize()
                line = csv_line['Line'].capitalize()
                admarea = csv_line['AdmArea'].capitalize()
                district = csv_line['District']
                status = csv_line['Status'].capitalize()
                station = Stations(station=station, line=line, admarea=admarea, district=district, status=status)
                station.save()
            except BaseException as exc:
                pass

def run():
    cur = os.path.abspath(os.path.curdir)
    csv_path = '/Users/semyagureevyh/PycharmProjects/Kaliningrad/guide/helpers/' + "data.csv"
    print(cur)
    # with open(csv_path, "r") as f_obj:
    #     csv_dict_reader(f_obj)


