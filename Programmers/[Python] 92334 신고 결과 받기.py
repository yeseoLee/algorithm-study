def solution(id_list, report, k):
    result = [0]*len(id_list)
    cheaters = [[] for _ in range(len(id_list))]
    id_to_idx = {}
    for idx, id in enumerate(id_list):
        id_to_idx[id] = idx

    for i in report:
        reporter, cheater = i.split()
        cheater_idx = id_to_idx[cheater]
        reporter_idx = id_to_idx[reporter]
        if reporter_idx not in cheaters[cheater_idx]:
            cheaters[cheater_idx].append(reporter_idx)
    for i in cheaters:
        if len(i) < k:
            continue
        for j in i:
            result[j] += 1
    return result
