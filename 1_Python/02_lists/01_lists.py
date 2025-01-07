# all of boot.dev's learn list material


# list problems go here
def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]


# Don't edit below this line


def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]


def get_last_index(inventory):
    return len(inventory) - 1


def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"

    return inventory


def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids


def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        if items[i] == "Potion":
            potion_count += 1
        elif items[i] == "Bread":
            bread_count += 1
        elif items[i] == "Shortsword":
            shortsword_count += 1

    # don't touch below this line

    return potion_count, bread_count, shortsword_count


def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True

    # don't touch below this line

    return found


def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        if new_character_levels[i] > old_character_levels[i]:
            print(i)


def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers


def get_champion_slices(champions):
    return champions[2:], champions[: len(champions) - 2], champions[::2]


def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items


def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    return weapon in top_weapons


def trim_strongholds(strongholds):
    del strongholds[0:1]
    del strongholds[len(strongholds) - 2 :]


def get_heroes():
    heroes = [
        ("Glorfindel", 2093, True),
        ("Gandalf", 1054, False),
        ("Gimli", 389, False),
        ("Aragorn", 87, False),
    ]

    return heroes


def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
    else:
        return items[0]


def reverse_array(items):
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result
