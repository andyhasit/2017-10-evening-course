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


def times2(x):
    return x * 2

def times3(x):
    return x * 3

x = times3
x = times2

print(x(4))

sys.exit(0)

sys.exit(0)

'''

import sys

from pprint import pprint
from datetime import datetime 


def tidy(row):
    return [i.strip() for i in row]

def extract_csv_data(filename):
    """Returns list of rows"""
    rows = []
    tidy = lambda r: [i.strip() for i in row]
    #def tidy(r): 
    #    return [i.strip() for i in row]
    with open(filename) as f:
        for l in f.readlines():
            row = l.split(',')
            rows.append(tidy(row))
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


def purge_duplicates(data, unique_field, takes_precedence):
    '''
    {
        'bob@gmail.com': ['id': '2', 'email': 'bob@gmail.com'...],
        'jane@gmail.com': ['id': '1', 'email': 'bob@gmail.com'...],
    }
    '''
    unique_values = {}
    for row in data:
        value = row[unique_field]
        if value in unique_values:
            existing = unique_values[value]
            if takes_precedence(row, existing):
                unique_values[value] = row
        else:
            unique_values[value] = row
    return unique_values.values()


d = {'a': 23, 'b': 44}
d.keys()
d.values()


def precedence_func(new, old):
    return new['id'] > old['id']


def exercise_1():
    filename = 'data.csv'
    headers, rows = extract_csv_data(filename)
    data = convert_to_dicts(headers, rows)
    foo = lambda new, old: new['id'] > old['id']
    foo = precedence_func
    rows = purge_duplicates(
        data, 
        'email', 
        foo
    )
    results = filter_list(data, {'country': 'england', 'q1': '1'})
    results = filter(
        lambda row: row['country'] == 'england' and row['q1'] == '0',
        data
        )
    print(len(results))


def exercise_2():
    filename = 'data2.csv'
    headers, rows = extract_csv_data(filename)
    data = convert_to_dicts(headers, rows)
    results = filter_list(data, {'country': 'england', 'q4': 'No'})
    print(len(results))
    

exercise_1()







