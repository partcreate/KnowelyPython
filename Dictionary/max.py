from typing import Any
from collections import Counter


dictionary = {'a': 3, 'b': 2, 'c': 1}
dictionary_keys = dictionary.keys()
dictionary_values = dictionary.values()

print(max(dictionary, key=dictionary.get))

def majority_element(nums: list) -> int:
    cache = {}

    for num in nums:
        if cache.get(num):
            cache[num] += 1
        else:
            cache[num] = 1

    max_key = max(cache, key=cache.get)

    return max_key


def simple_majority_element(nums: list) -> int:

    counts: dict[Any, int] = {item: nums.count(item) for item in set(nums)}

    return max(counts, key=counts.get)

def best_majority_with_counter(nums: list) -> Any | None:

    counts = Counter(nums)

    most_common_element: Any = max(counts, key=counts.get)

    return most_common_element



nums1 = [1, 2, 2, 3, 2, 1]

print(best_majority_with_counter(nums1))