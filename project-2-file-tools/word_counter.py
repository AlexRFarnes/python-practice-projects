"""Word-frequency logic: pure functions that turn raw text into word counts.

None of these functions read files directly — that's `wordfreq.py`'s job. Keeping
this module pure (text/tokens in, data out) mirrors Project 1's tasks.py/storage.py
split and makes it easy to test without touching disk.
"""

import re
from collections import Counter

# A minimal starter set — extend this with whatever words you think are too common
# to be interesting (e.g. "the", "a", "and", ...). Keep it lowercase.
STOPWORDS: set[str] = {"the", "a", "an", "and", "is", "are", "but", "to"}  # set literal


def tokenize(text: str) -> list[str]:
    """Split `text` into a list of lowercase word tokens, ignoring punctuation.

    Should not include empty strings or pure-punctuation "words." Think about
    what `re` tool lets you pull out contiguous runs of letters (and maybe digits
    or apostrophes, your call) from a string in one pass.
    """
    return re.findall(r"[a-z]+(?:'[a-z]+)*", text.lower())


def count_words(tokens: list[str], stopwords: set[str] | None = None) -> Counter:
    """Return a `Counter` mapping each token to how many times it appears.

    Tokens present in `stopwords` should be excluded entirely from the result.
    """
    if stopwords is None:
        stopwords = STOPWORDS

    return Counter(filter(lambda token: token not in stopwords, tokens))


def top_n(counts: Counter, n: int) -> list[tuple[str, int]]:
    """Return the `n` most common (word, count) pairs from `counts`, highest first.

    `Counter` already has a method built for exactly this — look it up.
    """
    return counts.most_common(n)
