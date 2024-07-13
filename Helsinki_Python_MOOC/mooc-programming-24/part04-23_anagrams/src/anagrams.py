# Write your solution here
def anagrams(one, two):
    if sorted(one) == sorted(two):
        return True
    else:
        return False