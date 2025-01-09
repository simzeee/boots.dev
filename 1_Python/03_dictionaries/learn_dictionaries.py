def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": name + "#" + server,
    }


def get_character_record_2(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict


def get_most_common_enemy(enemies_dict):
    max = float("-inf")
    name = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max:
            max = enemies_dict[enemy]
            name = enemy
    return name
