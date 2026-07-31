class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # shorten= replace non adj substrings with lengths
        # sbstrings are not adjacent, use numbers to rep their lengths
        # Case: whole string replace with num
        # Note: no leading zeros
        # Note; no numbers "0" for empty substring
        # input: word, abbr
        # recursion:
        # check first part of string matches
        # jump based on number
        # recurse, try to match smaller strings
        # dont need recursion, just need pointers
        word_index = 0
        abbr_index = 0
        while word_index < len(word) and abbr_index < len(abbr):
            if abbr[abbr_index].isdigit():
                length_word = ""
                while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                    if not length_word and abbr[abbr_index] == "0":
                        return False
                    length_word += abbr[abbr_index]
                    abbr_index += 1     # abbr_index now points to after the numbers
                length = int(length_word)
                word_index += length
            else:
                if word[word_index] != abbr[abbr_index]:
                    return False
                else:
                    word_index += 1
                    abbr_index += 1
        if word_index == len(word) and abbr_index == len(abbr):
            return True
        return False