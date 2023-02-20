people = {}


def add_friends(name_of_person, list_of_friends):
    people[name_of_person] = people.get(name_of_person, []) + list_of_friends


def are_friends(name_of_person_1, name_of_person_2):
    return name_of_person_2 in people.get(name_of_person_1, [])


def print_friends(name_of_person):
    friends = sorted(people.get(name_of_person, []))
    print(*friends)
