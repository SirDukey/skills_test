class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency


class WordFrequencyAnalyzer:
    """This class is an interface which contains 3 tools for analyzing a string.

    1. calculate_highest_frequency
    2. calculate_frequency_for_word
    3. calculate_most_frequent_n_words

    Examples:
        >>> word_frequency_analyzer = WordFrequencyAnalyzer()
        >>> word_frequency_analyzer.calculate_highest_frequency('The sun shines over the lake')
        >>> 2 # expected output
    """

    @staticmethod
    def calculate_highest_frequency(text: str) -> int:
        """
        should return the highest frequency in the text (several words might actually have this frequency)
        Returns (int):  highest frequency of any word in a text
        """
        if not isinstance(text, str):
            raise TypeError('text can only be of type "str"')
        text = text.lower()
        text_data = text.split()
        result_store = []
        for word in text_data:
            frequency = text_data.count(word)
            result_store.append(WordFrequency(word, frequency))

        return max([result.frequency for result in result_store])

    @staticmethod
    def calculate_frequency_for_word(text: str, word: str) -> int:
        """
        should return the frequency of the specified word
        Returns (int):  the frequency of a word in a text
        """
        if not any([isinstance(text, str), isinstance(word, str)]):
            raise TypeError('input arguments must be of type "str"')
        word = word.lower()
        text = text.lower()
        text_data = text.split()
        check = word
        result_store = {}
        for word in text_data:
            frequency = text_data.count(word)
            result_store[word] = WordFrequency(word, frequency)
        return result_store[check].frequency

    @staticmethod
    def calculate_most_frequent_n_words(text: str, n: int) -> list:
        """
        should return a list of the most frequent ‘n’ words in the input text, all the words returned in lower case.
        If several words have the same frequency, this method should return them in ascendant alphabetical order
        (for input text “The sun shines over the lake” and n = 3, it should return the list [ (“the”, 2), (“lake”, 1),
        (“over”, 1) ]

        Returns (list):  a list of n tuples, where n is an amount.
        """

        def __sort_by_frequency(value: tuple) -> list:
            """Used to sort a two value tuple by the second value"""
            return value[1]

        if not isinstance(text, str) or not isinstance(n, int):
            raise TypeError

        n = int(n)
        result_list = []
        text = text.lower()
        text_data = sorted(text.split())
        for word in text_data:
            frequency = text_data.count(word)
            wf = WordFrequency(word, frequency)
            if word not in [w[0] for w in result_list]:
                result_list.append((wf.word, wf.frequency))

        return sorted(result_list, reverse=True, key=__sort_by_frequency)[:n]
