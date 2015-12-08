import collections
import datetime


class WordSequence(object):

    def __init__(self, *words):
        self._value = tuple(words)

    @property
    def value(self):
        return self._value


class FlyweightWordSequence(object):

    cache = {}

    def __new__(cls, *words):
        word_cache = cls.cache
        word_index = 0
        while word_index < len(words):
            print(type(words[word_index]))
            word_cache = word_cache.get(words[word_index])
            if not word_cache:
                value = tuple(words)
                word_new_index = word_index
                while word_new_index < len(words) - 1:
                    next_word_cache = {}
                    word_cache[words[word_new_index]] = next_word_cache
                    word_cache = next_word_cache
                word_cache[words[word_new_index]] = value
                return value
            word_index += 1

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
                word_sequence = class_(*words[:3])
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
