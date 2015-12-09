import collections
import re


def nested_defaultdict():
    return collections.defaultdict(nested_defaultdict)


class WordSequence(object):

    def __init__(self, word0, word1):
        self.value = (word0, word1)

    def __eq__(self, other):
        return (self is other
                or self.value is other.value
                or self.value == other.value
        )

    def __hash__(self):
        return hash(self.value)


class FlyweightWordSequence(object):

    cache = nested_defaultdict()

    def __new__(cls, word0, word1):
        if not word1 in cls.cache[word0]:
            cls.cache[word0][word1] = word_sequence = super().__new__(cls)
            word_sequence.value = (word0, word1)
        return cls.cache[word0][word1]

    def __eq__(self, other):
        return (self is other
                or self.value is other.value
                or self.value == other.value
        )

    def __hash__(self):
        return hash(self.value)


def count_word_sequences(path, class_):
    counter = collections.Counter()
    word_pattern = re.compile(r"[\w']+")
    with open(path) as f:
        line = f.readline()
        words = []
        while line != '':
            words += word_pattern.findall(line)
            while len(words) >= 2:
                word_sequence = class_(words[0], words[1])
                counter[word_sequence] += 1
                words.pop(0)
            line = f.readline()
    output = {'len': len(counter), 'top_3': {
        word_sequence.value: count
        for word_sequence, count in counter.most_common(3)
    }}
    print(output)
    return output


def main():
    import timeit
    print('WordSequence: ' + str(timeit.timeit(
        stmt="count_word_sequences('./war_and_peace.txt', WordSequence)",
        setup='from __main__ import count_word_sequences, WordSequence',
        number=1
    )))
    print('FlyweightWordSequence: ' + str(timeit.timeit(
        stmt="count_word_sequences('./war_and_peace.txt', FlyweightWordSequence)",
        setup='from __main__ import count_word_sequences, FlyweightWordSequence',
        number=1
    )))

if __name__ == '__main__':
    main()
