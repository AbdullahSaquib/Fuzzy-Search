"""The fuzzy_compare_word takes two inputs as arguments.
The convention is that, the second argument is the correct
word against which the word in the first argument is compared.
It return a real number between 0 and 1, which is a measure
of how well the two words matches. The fuzzy_compare_words
allow one missing word, it can be improved further by adding
another layer of try except statements.
"""


def fuzzy_compare_words(search_word, db_word):
    db_wd = db_word.lower()
    s_wd = search_word.lower()
    db_wd_len = len(db_word)
    s_wd_len = len(s_wd)
    mc = 1  # marks center
    ml = 0.5  # marks left
    mr = 0.5  # marks right
    marks = 0.0
    for i in range(0, s_wd_len):
        try:
            if s_wd[i] == db_wd[i]:
                marks += mc
                continue
            else:
                raise IndexError
        except IndexError:
            try:
                if s_wd[i] == db_wd[i+1]:
                    marks += mr
                    continue
                else:
                    raise IndexError
            except IndexError:
                try:
                    if s_wd[i] == db_wd[i-1]:
                        marks += ml
                except IndexError:
                    pass

    if db_wd_len > s_wd_len:
        return marks/db_wd_len
    else:
        return marks/s_wd_len


"""campare_strings compare two strings to return a number
between 0 and 1, measuring how well the two strings matches.
The convention is that the first argument is the searched
string, and the second argument is the title in database,
that is the correct string.
"""


def compare_strings(search_string, db_string):
    search_words_list = search_string.split()
    db_string_words_list = db_string.split()
    marks = 0
    score = 0
    for wd1 in search_words_list:
        for wd2 in db_string_words_list:
            temp = fuzzy_compare_words(wd1, wd2)  # change compare words here
            if temp > marks:
                marks = temp
            if marks == 1:
                break
        score += marks*len(wd1)
        marks = 0
    len1 = len(search_string)-(len(search_words_list)-1)
    return score/len1


# search_string = 'The adventures of Rocky and Bullwinkle'
# db_string = 'Harry Potter and the chamber of secrets'
# print(compare_strings(search_string, db_string))
