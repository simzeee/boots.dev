# I just quickly copied over all the work I did in the boots.dev loops course. This will not run.


def print_numbers():
    for i in range(0, 100):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()


def print_numbers():
    for i in range(0, 200):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()


def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()


def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()


def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total


def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total


def regenerate(current_health, max_health, enemy_distance):
    while enemy_distance > 3:
        if current_health < max_health:
            current_health += 1
        enemy_distance -= 2
    return current_health


def countdown_to_start():
    for i in range(10, 0, -1):
        if i == 1:
            print("1...Fight!")
        else:
            print(f"{i}...")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()


def calculate_flurry_crit(num_attacks, base_damage):
    critical_damage = 0
    for i in range(1, num_attacks):
        print(i)
        if i == num_attacks - 1:
            critical_damage += 4 * base_damage
        critical_damage += 2 * base_damage
        print(critical_damage)
    return critical_damage


def calculate_experience_points(level):
    total_xp = 0
    for i in range(1, level):
        total_xp += i * 5
    return total_xp


def is_prime(number):
    is_prime = True
    if number <= 0:
        return False
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    return is_prime


def meditate(mana, max_mana, energy, energy_drinks):
    while mana < max_mana or energy == 0 and energy_drinks == 0:
        if energy == 0:
            if energy_drinks > 0:
                energy_drinks -= 1
                energy += 50
            else:
                break
        energy -= 1
        mana += 1
    return mana, energy, energy_drinks
