def solution(cacheSize, cities):
    
    cache = []
    time = 0
    for i in range(len(cities)):
        cities[i] = cities[i].upper()
    
    for i in cities:
        if i in cache:
            cache.remove(i)
            cache.append(i)
            time += 1
        else:
            if cacheSize == 0:
                time += 5
                continue
            elif len(cache) == cacheSize:
                cache.pop(0)
                cache.append(i)
            else:
                cache.append(i)
            time += 5
    return time