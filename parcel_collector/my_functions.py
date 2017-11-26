

def get_dimensions():
    width = int(input("width:"))
    height = int(input("height:"))
    length = int(input("length:"))
    return width, height, length


def get_volume(parcel):
    return parcel[1] * parcel[2] * parcel[3]


def build_parcel(destination, width, height, length):
    return (destination, width, height, length)


def collect_parcels_from_user():
    '''
    Collect parcels from user
    Decide when to stop
    Return list of parcels
    '''
    parcels = []
    while True:
        # Get destination
        destination = input("Where is it going:")
        # Determine whether to stop
        if destination == "":
            break
        width, height, length = get_dimensions()
        parcel = build_parcel(destination, width, height, length)
        parcels.append(parcel)
    return parcels


def find_largest_parcel(parcels):
    largest_parcel = None
    largest_volume = 0
    for parcel in parcels:
        volume = get_volume(parcel)
        print(volume)
        if volume > largest_volume:
            largest_parcel = parcel
            largest_volume = volume
    return largest_parcel
    
def find_smallest_parcel(parcels):
    largest_parcel = None
    largest_volume = 0
    for parcel in parcels:
        volume = get_volume(parcel)
        print(volume)
        if volume > largest_volume:
            largest_parcel = parcel
            largest_volume = volume
    return largest_parcel
    
