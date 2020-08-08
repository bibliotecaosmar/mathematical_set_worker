from complementary_variables import ALPHA
from subpattern import sample_sequence, sc_forbegins, sc_forend, sc_separator_easy, sc_around, common_number4
from protocols import combine, wrap, cartesian_product, axis_Z, intersection 

#
# Words Only
#============================================

def double_word(wordlist):
    return cartesian_product(wordlist, wordlist)

def triple_word(wordlist):
    return axis_Z(wordlist, wordlist, wordlist)

#
# Word Modificated
#============================================

def word_modificated(wordlist):
    ...

#
# Number and Simbol
#============================================

def sequence():
    return sample_sequence(5)

def sequence_simbols():
    return cartesian_product(sample_sequence(4), sc_forend())

def sequence_alpha_simbols():
    ...

#
# Word and Simbol
#============================================

def word_separator_word(wordlist):#defeito: mostra 2 vezes a msm sequência
    return intersection(wordlist, wordlist, sc_separator_easy())

def simbol_word(wordlist):
    return cartesian_product(sc_forbegins(), wordlist)

def special_word_special(wordlist):
    return wrap(wordlist, sc_around()) 

#
# Word and Number
#============================================

def word_number2(wordlist):
    return combine(wordlist, number(2))

def word_number4(wordlist):
    return combine(wordlist, common_number4())

#
# Word, Simbol and Number
#============================================

def word_simbol_number2(wordlist):
    return combine(combine(wordlist, simbol), number(2))

def word_word_simbol_number2(wordlist):
    return combine(combine(cartesian_product(wordlist, wordlist), sc_separator_easy()), number(2))

def word_simbol_word_number2(wordlist):
    return combine(intersection(wordlist, wordlist, sc_separator_easy()), number(2))

def word_word_simbol_sequence(wordlist):
    return combine(combine(cartesian_product(wordlist, wordlist), sc_separator_easy()), sample_sequence(4))

def word_word_simbol_number(wordlist):
    return combine(combine(cartesian_product(wordlist, wordlist), sc_separator_easy()), common_number4())

   
