import sys


def store_items() -> dict[str, int]:
    items_dict: dict[str, int] = {}

    for item in sys.argv[1:]:
        if item.find(":") != -1:
            try:
                result = item.split(":")

                if len(result) != 2 or result[0] == "" or result[1] == "":
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
    if items_total_qty == 0:
        return

    # Percentage
    for item_name in items:
        quantity = items[item_name]
        x: float = quantity / items_total_qty
        print(f"Item {item_name} represents {round(x * 100, 1)}%")

    # Most abundant
    most_name = items_list[0]
    for item_name in items:
        if items[item_name] > items[most_name]:
            most_name = item_name

    print(
		f"Item most abundant: {most_name} "
		f"with quantity {items[most_name]}"
	)

    # Least abundant
    least_name = items_list[0]
    for item_name in items:
        if items[item_name] < items[least_name]:
            least_name = item_name

    print(
		f"Item least abundant: {least_name} "
		f"with quantity {items[least_name]}"
	)

    # Update
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()
