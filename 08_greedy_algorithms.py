# Вы передаете массив, и он преобразуется в set.
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed: # пока сет нe пуст
    best_station = None
    states_covered = set()

    for station, states in stations.items():
        covered = states_needed & states #  Находит пересечение множеств

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered # вычитаем из необработанного сета то что уже обработали
    final_stations.add(best_station)

print(final_stations)
