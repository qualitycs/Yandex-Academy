items = []
receipt_number = [1]


def add_item(item_name, item_cost):
    items.append((item_name, item_cost))


def print_receipt():
    if not items:
        return

    print(f"Чек {receipt_number[0]}. Всего предметов: {len(items)}")

    for item in items:
        print(f"{item[0]} - {item[1]}")

    total_cost = sum([item[1] for item in items])
    print(f"Итого: {total_cost}")

    print("-" * 5)

    receipt_number[0] += 1
    items.clear()
