import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        s = input("Enter new coordinates as floats in format 'x,y,z': ")
        coord = []
        tmp = ""

        for c in s:
            if c == ",":
                coord.append(tmp)
                tmp = ""
            else:
                tmp += c
        coord.append(tmp)

        if len(coord) != 3:
            print("Invalid syntax")
            continue

        nums = []
        i = 0
        try:
            while i < len(coord):
                nums.append(float(coord[i]))
                i += 1
        except ValueError:
            print(
                f"Error on parameter '{coord[i]}': "
                f"could not convert string to float: '{coord[i]}'"
            )
            continue

        return (nums[0], nums[1], nums[2])


def calculate_distance(
        a: tuple[float, float, float],
        b: tuple[float, float, float]
        ) -> float:
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    t1 = get_player_pos()

    print(f"Got a first tuple: ({t1[0]}, {t1[1]}, {t1[2]})")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    distance_from_center = calculate_distance((0, 0, 0), t1)
    print(f"Distance to center: {round(distance_from_center, 4)}")

    print("\nGet a second set of coordinates")
    t2 = get_player_pos()

    distance_between = calculate_distance(t1, t2)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(distance_between, 4)}"
    )


if __name__ == "__main__":
    main()
