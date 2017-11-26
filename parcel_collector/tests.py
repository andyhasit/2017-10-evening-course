from my_functions import *


parcel = ('NL', 10, 10, 10)
volume = get_volume(parcel)
if volume == 1000:
    print('get_volume works!!!')
else:
    print('get_volume fails!!!')
    print(volume)


parcels = [('NL', 10, 10, 10), ('JPN', 30, 30, 30), ('FR', 20, 20, 20)]
largest_parcel = find_largest_parcel(parcels)

if largest_parcel == ('JPN', 30, 30, 30):
    print('find_largest_parcel works!!!')
else:
    print('find_largest_parcel fails :-(')
    print(largest_parcel)


smallest_parcel = find_smallest_parcel(parcels)
if smallest_parcel == ('NL', 10, 10, 10):
    print('find_smallest_parcel works!!!')
else:
    print('find_smallest_parcel fails :-(')
    print(smallest_parcel)



