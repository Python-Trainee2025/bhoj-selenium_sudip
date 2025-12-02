import random
import string


class SearchStressRandomProperties:

    @staticmethod
    def generate_random_words(count=120):
        words = []
        for _ in range(count):
            length = random.randint(2, 10)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.append(word)
        return words
