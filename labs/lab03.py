
import string


# 1
def unique_in_order(values):
    seen = set()
    result = []
    for v in values:
        if v not in seen:
            seen.add(v)
            result.append(v)
    return result


# 2
def word_frequencies(text):
    freq = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq


# 3
def top_k(frequencies, k):
    ordered = sorted(frequencies.items(), key=lambda kv: (-kv[1], kv[0]))
    return ordered[:k]


# 4
def transpose(matrix):
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# 5
def invert(mapping):
    result = {}
    for key, value in mapping.items():
        result.setdefault(value, []).append(key)
    for value in result:
        result[value].sort()
    return result


# 6
def common_elements(first, second):
    return sorted(set(first) & set(second))


# 7
def group_by_length(words):
    groups = {}
    for w in words:
        groups.setdefault(len(w), []).append(w)
    return groups


# 8
class Bag:
    def __init__(self):
        self._counts = {}

    def add(self, item, times=1):
        self._counts[item] = self._counts.get(item, 0) + times

    def remove(self, item, times=1):
        if self._counts.get(item, 0) < times:
            raise KeyError(item)
        self._counts[item] -= times
        if self._counts[item] == 0:
            del self._counts[item]

    def count(self, item):
        return self._counts.get(item, 0)

    def total(self):
        return sum(self._counts.values())

    def unique(self):
        return len(self._counts)

    def items(self):
        return sorted(self._counts.items())

    def __contains__(self, item):
        return item in self._counts

    def __len__(self):
        return self.total()


# 9
def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 10
def chunks(values, size):
    if size <= 0:
        raise ValueError("size must be positive")
    for i in range(0, len(values), size):
        yield values[i:i + size]
