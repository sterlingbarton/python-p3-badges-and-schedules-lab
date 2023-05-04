def badge_maker(name):
    return f'Hello, my name is {name}.'


def batch_badge_creator(names):
    name_list = []
    for name in names:
        name_list.append(f'Hello, my name is {name}.')
    return name_list


def assign_rooms(names):
    room_list = []
    index = 1
    for name in range(len(names)):
        room_list.append(
            f"Hello, {names[name]}! You'll be assigned to room {index}!")
        index += 1
    return room_list


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for assignment in assign_rooms(names):
        print(assignment)
