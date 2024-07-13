# Write your solution here:
def sort_by_seasons(items: list):
    def key(item: dict):
        return item['seasons']
    return sorted(items, key = key)