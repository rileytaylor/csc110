# HW 11 Hours spent: 2


from geolocation import *

STASH = (34.988889, -106.614444)
STUDIO = (34.989978, -106.614357)
FBI = (35.131281, -106.61263)


def main():
    locations = create_location_objects()
    print_results(locations)


def create_location_objects():
    data = {}
    data['stash'] = GeoLocation(STASH[0], STASH[1])
    data['studio'] = GeoLocation(STUDIO[0], STUDIO[1])
    data['fbi'] = GeoLocation(FBI[0], FBI[1])
    return data


def print_results(locations):
    print('the stash is at ' + str(locations['stash']))
    print('ABQ studio is at ' + str(locations['studio']))
    print('FBI building is at ' + str(locations['fbi']))
    print('distance in miles between:')
    stash_to_studio = locations['stash'].distance_from(locations['studio'])
    print('    stash/studio = ' + str(stash_to_studio))
    stash_to_fbi = locations['stash'].distance_from(locations['fbi'])
    print('    stash/fbi = ' + str(stash_to_fbi))

main()
