# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        max_item = None
        max_count = 0
        counts = {}
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1
            if counts[item] > max_count:
                max_item = item
                max_count = counts[item]
        return max_item

    @classmethod
    def doubles(cls, my_list: list):
        counts = {}
        counter = 0
        for item in my_list:
            counts[item] = counts.get(item, 0) + 1
        for values in counts.values():
            if values >= 2:
                counter += 1
        return counter