# Write your solution here
def get_station_data(filename: str):
    stations = {}
    with open(filename) as file:
        for row in file:
            row = row.strip().split(';')
            if row[0] == 'Longitude':
                continue
            stations[row[3]] = (float(row[0]), float(row[1]))
    return stations

def distance(stations: dict, station1: str, station2:str):
    if station1 in stations and station2 in stations:
        x = (stations[station1][0] - stations[station2][0]) * 55.26
        y = (stations[station1][1] - stations[station2][1]) * 111.2
        return (x**2 + y**2)**0.5

def greatest_distance(stations: dict):
    info = list(stations.items())
    result = ('', '', 0)
    for i in range(0, len(info)):
        for j in range(i, len(info)):
            dist = distance(stations, info[i][0], info[j][0])
            if dist > result[2]:
                result = (info[i][0], info[j][0], dist)
    return result
