'''

def convert_row_to_dict(headers, row):
    d = {}
    for i, f in enumerate(headers):
        d[f] = row[i]
    return d

s = convert_row_to_dict(
    ['id', 'email', 'q1'],
    ['33', 'bot@mail.com', '1']
    )
#print(s)


for i, k in enumerate(s):
    print(i)
    print(k)
    

r = criteria_matches(
    {},
    {'id':'33', 'country': 'Scotland', 'q2': '1'},
    )

print(r)


sys.exit(0)

'''

import sys

from pprint import pprint
from datetime import datetime 


def strip_row_spaces(row):
    return [i.strip() for i in row]


def extract_csv_data(filename):
    """Returns list of rows"""
    rows = []
    with open(filename) as f:
        for l in f.readlines():
            row = l.split(',')
            rows.append(strip_row_spaces(row))
    return rows[0], rows[1:]


def convert_to_dicts(headers, rows):
    rows_as_dicts = []
    for row in rows:
        d = convert_row_to_dict(headers, row)
        rows_as_dicts.append(d)
    return rows_as_dicts


def convert_row_to_dict(headers, row):
    d = {}
    for i, f in enumerate(headers):
        d[f] = row[i]
    return d


def criteria_matches_AND(criteria, row):
    '''
    Criteria: {'country': 'scotland', 'q2': '1'}
    row: {'id': '3', 'country': 'scotland', 'q2': '1'}

    If criteria is empty, return True
    '''
    for k in criteria:
        if criteria[k] != row[k]:
            return False
    return True


def criteria_matches_OR(criteria, row):
    '''
    Criteria: {'country': 'scotland', 'q2': '1'}
    row: {'id': '3', 'country': 'scotland', 'q2': '1'}

    If criteria is empty, return True
    '''
    for k in criteria:
        if criteria[k] != row[k]:
            return True
    return False


def filter_list(data, criteria):
    filtered_list = []
    for row in data:
        if criteria_matches_AND(criteria, row):
            filtered_list.append(row)
    return filtered_list


def main_old():
    filename = 'data.csv'
    headers, rows = extract_csv_data(filename)
    data = convert_to_dicts(headers, rows)
    results = filter_list(data, {'country': 'england', 'q1': '1'})
    #pprint(data)
    print(len(results))

def main():
    filename = 'data2.csv'
    headers, rows = extract_csv_data(filename)
    data = convert_to_dicts(headers, rows)
    results = filter_list(data, {'country': 'england', 'q4': 'No'})
    #pprint(data)
    print(len(results))

main()







