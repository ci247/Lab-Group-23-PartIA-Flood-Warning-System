# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Number of stations wanted
    N = 5

    # Store list of station objects to plot: stations_highest_rel_level(stations, 10)
    stations_highest_list = stations_highest_rel_level(stations, N)

    for station in stations_highest_list:
        # Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        # Plot level history
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
