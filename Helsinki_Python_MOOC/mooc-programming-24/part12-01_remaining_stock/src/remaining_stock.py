# Write your solution here:
def sort_by_remaining_stock(items: list):
    def key(item: tuple):
        return item[2]
    return sorted(items, key = key)