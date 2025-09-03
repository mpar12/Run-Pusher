import re

def estimate_target_words(duration_mins: int, wpm: int) -> int:
    return int(duration_mins * wpm ) 



def clamp_words(words: str, target_words: int) -> str:
    """ Clamp the number of words spit out by the model to the target words """
    word_list = words.split()
    if len(word_list) > target_words:
        return " ".join(word_list[:target_words]) + "."
    return words

