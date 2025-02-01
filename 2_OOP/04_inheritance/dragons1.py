class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if self.pos_x >= x_1 and self.pos_x <= y_2:
            if self.pos_y <= x_2 and self.pos_y <= y_2:
                return True
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        target_area = (x - self.__fire_range, y - self.__fire_range), (
            x + self.__fire_range,
            y + self.__fire_range,
        )
        print(target_area)
        blast = []
        for unit in units:
            if unit.in_area(
                target_area[0][0],
                target_area[0][1],
                target_area[1][0],
                target_area[1][1],
            ):
                blast.append(unit)
        return blast


class UnitSolution:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class DragonSolution(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        hit_by_blast = []
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                hit_by_blast.append(unit)
        return hit_by_blast
