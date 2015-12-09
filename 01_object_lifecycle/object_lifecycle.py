import collections
import datetime


class WordSequence(object):

    def __init__(self, word0, word1, word2):
        self._value = (word0, word1, word2)


class FlyweightWordSequence(object):

    cache = {}

    def __new__(cls, word0, word1, word2):
        word_cache = cls.cache
        if not word0 in word_cache:
            word_cache[word0] = {}
        word_cache = word_cache[word0]
        if not word1 in word_cache:
            word_cache[word1] = {}
        word_cache = word_cache[word1]
        if not word2 in word_cache:
            word_cache[word2] = (word0, word1, word2)
        return word_cache[word2]

    @property
    def value(self):
        return self


def count_word_sequences(path, class_):
    counter = collections.Counter()
    with open(path) as f:
        line = f.readline()
        words = []
        while line != '':
            words += line.split(' ')
            while len(words) >= 3:
                word_sequence = class_(words[0], words[1], words[2])
                counter[word_sequence] += 1
                words = words[1:]
            line = f.readline()
    return len(counter)

def main():
    print('WordSequence:')
    before_time = datetime.datetime.now()
    print('    return: ' + str(count_word_sequences('./war_and_peace.txt', WordSequence)))
    after_time = datetime.datetime.now()
    print('    time:   ' + str((after_time - before_time).microseconds))

    print('FlyweightWordSequence:')
    before_time = datetime.datetime.now()
    print('    return: ' + str(count_word_sequences('./war_and_peace.txt', FlyweightWordSequence)))
    after_time = datetime.datetime.now()
    print('    time:   ' + str((after_time - before_time).microseconds))

if __name__ == '__main__':
    main()
