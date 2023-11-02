import pytest
from word_frequency import WordFrequency, WordFrequencyAnalyzer


word_frequency_analyzer = WordFrequencyAnalyzer()

TEXT1 = 'This is a test string check for the highest frequency of a word in a string'
TEXT2 = 'The sun shines over the lake'
TEXT3 = None


@pytest.mark.parametrize('text, expected', [(TEXT1, 3), (TEXT2, 2), (TEXT3, None)])
def test_word_frequency_analyzer(text, expected):
    try:
        result = word_frequency_analyzer.calculate_highest_frequency(text)
        assert result == expected
    except TypeError:
        assert True


def test_calculate_frequency_for_word():
    word = 'a'
    expected = 3
    result = word_frequency_analyzer.calculate_frequency_for_word(TEXT1, word)
    assert result == expected


@pytest.mark.parametrize('text, expected', [
    (TEXT1, [('a', 3), ('string', 2), ('check', 1)]),
    (TEXT2, [('the', 2), ('lake', 1), ('over', 1)]),
    (TEXT3, None)
])
def test_calculate_most_frequent_n_words(text, expected):
    n = 3
    try:
        result = word_frequency_analyzer.calculate_most_frequent_n_words(text, n)
        assert len(result) == n
        assert result == expected
    except TypeError:
        assert True


def test_word_frequency():
    word = 'test'
    frequency = 1
    word_frequency = WordFrequency(word, frequency)
    assert word_frequency.word == word
    assert word_frequency.frequency == frequency
