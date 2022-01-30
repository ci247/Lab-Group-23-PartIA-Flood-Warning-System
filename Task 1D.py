# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Build list of rivers with stations
    rivers = rivers_with_station(stations)

    # Display number of rivers and data from first 10
    print("{} rivers with monitoring stations. First 10 are: \n{}".format(len(rivers),rivers[:10]))

    # Build list of rivers with stations
    stations_by_river_dict = stations_by_river(stations)

    # Display data from 3 rivers 'River Aire', 'River Cam', 'River Thames'
    for river, river_stations in stations_by_river_dict:
        if river in [
                'River Aire', 'River Cam', 'River Thames'
        ]:
            print(river,river_stations.sort())


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
