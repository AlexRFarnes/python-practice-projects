from collections import Counter

import pytest
from word_counter import count_words, tokenize, top_n

# Write your own tests here for the functions in word_counter.py.
# A few things worth thinking about testing once you get there:
#   - tokenize: does punctuation get stripped? are words lowercased? what about
#     an empty string, or a string with no words at all?
#   - count_words: are stopwords actually excluded? what if stopwords is empty?
#   - top_n: does it return the right number of items, in the right order, when
#     there are ties?


def test_count_words_basic_counting():
    words_list = ["hello", "hello", "hello"]
    counts = count_words(words_list)
    assert counts == Counter(words_list)


def test_count_words_default_stopwords_exclusion():
    words_list = ["the", "a", "fox"]
    counts = count_words(words_list)
    assert "the" not in counts
    assert "a" not in counts
    assert "fox" in counts


def test_count_words_custom_stopword_exclusion():
    stopwords = {"hello"}
    words_list = ["hello", "world"]
    counts = count_words(words_list, stopwords)
    assert "hello" not in counts


def test_count_words_empty_stopwords():
    words_list = ["the", "a", "fox"]
    counts = count_words(words_list, set())
    assert "the" in counts
    assert "a" in counts
    assert "fox" in counts


def test_count_words_empty_word_list():
    counts = count_words([])
    assert counts.total() == 0


@pytest.mark.parametrize(
    "words, expected, length",
    [
        pytest.param(
            "hello world python", ["hello", "world", "python"], 3, id="basic_case"
        ),
        pytest.param(
            "Hello hello HELLO", ["hello", "hello", "hello"], 3, id="uppercase"
        ),
        pytest.param("world!", ["world"], 1, id="punctuation"),
        pytest.param("", [], 0, id="empyt_string"),
        pytest.param("!!! ...", [], 0, id="string_only_punctuations"),
        pytest.param("don't", ["don't"], 1, id="contractions"),
        pytest.param(
            "'twas dogs'", ["twas", "dogs"], 2, id="leading_trailing_apostrophes"
        ),
        pytest.param("2024 covid19", ["covid"], 1, id="numbers_and_words_with_numbers"),
        pytest.param(
            "hello    world\t python\n\n test",
            ["hello", "world", "python", "test"],
            4,
            id="multiple_spaces_tabs_new_lines",
        ),
    ],
)
def test_tokenize(words, expected, length):
    tokens = tokenize(words)
    assert len(tokens) == length, "the result has the correct amount of tokens"
    assert tokens == expected, "the order of the tokens is the expected"


def test_top_n_single_top():
    counts = Counter(["hello", "hello", "world", "python", "python", "python"])
    n = 1
    top_result = top_n(counts, n)
    assert len(top_result) == 1
    assert ("python", 3) == top_result[0]
    assert "hello" not in [r[0] for r in top_result]


def test_top_n_tied_top():
    counts = Counter(["hello", "hello", "hello", "world", "python", "python", "python"])
    n = 1
    top_result = top_n(counts, n)
    assert len(top_result) == 1
    assert ("hello", 3) == top_result[0], "should return the first insertion"


def test_top_n_top_greater_than_counts():
    counts = Counter(["hello", "hello", "hello", "world", "python", "python", "python"])
    n = 5
    top_result = top_n(counts, n)
    assert len(top_result) == 3


def test_top_n_order_result():
    counts = Counter(["hello", "hello", "world", "python", "python", "python"])
    n = 3
    top_results = top_n(counts, n)
    assert ["python", "hello", "world"] == [r[0] for r in top_results]


def test_top_n_zero():
    counts = Counter(["hello", "hello", "world", "python", "python", "python"])
    n = 0
    top_results = top_n(counts, n)
    assert len(top_results) == 0
