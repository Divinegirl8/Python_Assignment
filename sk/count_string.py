def count_character(words: str) -> dict:
    return {word: words.count(word) for word in words}