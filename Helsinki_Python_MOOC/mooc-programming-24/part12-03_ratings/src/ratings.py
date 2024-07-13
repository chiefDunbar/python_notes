# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def key(item: dict):
        return item['rating']
    return sorted(items, key = key, reverse = True)