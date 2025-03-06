"""Set Covering"""
import json
def findStations(stations: set):
    """____"""
    selected = set()
    stationDict = {}
    for _ in range(int(input())):
        l = json.loads(input())
        stationDict[l["Name"]] = l["Cities"]
    
    while stations:
        best_station = None
        covered_by_best = set()
        
        for station, covered_cities in stationDict.items():
            covered = set(covered_cities) & stations
            if len(covered) > len(covered_by_best):
                best_station = station
                covered_by_best = covered
        
        if best_station is None:
            break
        
        selected.add(best_station)
        stations -= covered_by_best
    
    print(sorted(list(selected)))
        

findStations(set(json.loads(input())))