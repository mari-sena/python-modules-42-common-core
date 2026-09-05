import sys


def store_items() -> dict[str, int]:
    items_dict: dict[str, int] = dict()

    for item in sys.argv[1:]:
        if item.find(":") != -1:
            try:
                result = item.split(":")

                if len(result) != 2:
                    print(f"Error - invalid parameter '{item}'")
                    continue

                if result[0] in items_dict:
                    print(f"Redundant item '{result[0]}' - discarding")
                else:
                    items_dict.update({result[0]: int(result[1])})

            except ValueError:
                print(
                    f"Quantity error for '{result[0]}': "
                    f"invalid literal for int() with base 10: '{result[1]}'"
                )
        else:
            print(f"Error - invalid parameter '{item}'")
    return items_dict


def main() -> None:
    print("=== Inventory System Analysis ===")
    items = store_items()
    print(f"Got inventory: {items}")

    items_list = list(items)
    print(f"Item list: {items_list}")

    # Total quantity
    items_total_qty = sum(list(items.values()))
    print(
        f"Total quantity of the {len(items_list)} "
        f"items: {items_total_qty}"
    )

    if len(items) == 0:
        return

    # Percentage
    for item_name, quantity in items.items():
        x: float = quantity / items_total_qty
        print(f"Item {item_name[0]} represents {round(x * 100, 1)}%")

    # Most abundant
    most_abundant = max(items.values())
    for item_name in items:
        if most_abundant == items[item_name]:
            print(
                f"Item most abundant: {item_name} "
                f"with quantity {most_abundant}"
            )
            break
    # Least abundant
    least_abundant = min(items.values())
    for item_name in items:
        if least_abundant == items[item_name]:
            print(
                f"Item least abundant: {item_name} "
                f"with quantity {least_abundant}"
            )
            break

    # Update
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
