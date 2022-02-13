from typing import List, Tuple


def arrange_applications(applications: List[Tuple[int, int]]):
    applications.sort(key=lambda x: x[0])
    rooms = []

    for application in applications:
        found = False

        for i, room in enumerate(rooms):
            if application[0] >= room:
                rooms[i] = application[1]
                found = True
                break

        if not found:
            rooms.append(application[1])

    return len(rooms)

