def boats(people, limit):
    people.sort()
    if people[-1] > limit:
        return -1

    num_boats = 0
    first, last = 0, len(people) - 1

    while first <= last:
        if people[first] + people[last] <= limit:
            first += 1; last -= 1; num_boats += 1
        else:
            last -= 1; num_boats += 1

    return num_boats
