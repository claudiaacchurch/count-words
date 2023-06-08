
from lib.read_speed import *

# zero input, returns zero
def test_zero_input_returns_zero():
    result = reading_time(0)
    assert result == 0


# non zero input, returns input/200 formatted as x seconds
def test_non_zero_input_returns_zero():
    result = reading_time(10)
    assert result == '3 seconds'

# non zero input, returns input/200 formatted as y minutes, x seconds 
def test_bigger_than_1_min_input_returns_zero():
    result = reading_time(440)
    assert result == '2 minutes, 12 seconds'

# non zero input, returns input/200 formatted as z hours, y minutes, x seconds
def test_bigger_than_60_min_input_returns_zero():
    result = reading_time(40000)
    assert result == '3 hours, 20 minutes, 0 seconds'

# text input, returns input word number/200 formatted as above
def test_smalltext():
    result = reading_time('Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe. “Beware the Jabberwock, my son! The jaws that bite, the claws that catch! Beware the Jubjub bird, and shun The frumious Bandersnatch!” He took his vorpal sword in hand; Long time the manxome foe he sought— So rested he by the Tumtum tree And stood awhile in thought. And, as in uffish thought he stood, The Jabberwock, with eyes of flame, Came whiffling through the tulgey wood, And burbled as it came! One, two! One, two! And through and through The vorpal blade went snicker-snack! He left it dead, and with its head He went galumphing back. “And hast thou slain the Jabberwock? Come to my arms, my beamish boy! O frabjous day! Callooh! Callay!” He chortled in his joy. ’Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe.')
    assert result == '50 seconds'

def test_bigtext():
    result = reading_time('Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe. “Beware the Jabberwock, my son! The jaws that bite, the claws that catch! Beware the Jubjub bird, and shun The frumious Bandersnatch!” He took his vorpal sword in hand; Long time the manxome foe he sought— So rested he by the Tumtum tree And stood awhile in thought. And, as in uffish thought he stood, The Jabberwock, with eyes of flame, Came whiffling through the tulgey wood, And burbled as it came! One, two! One, two! And through and through The vorpal blade went snicker-snack! He left it dead, and with its head He went galumphing back. “And hast thou slain the Jabberwock? Come to my arms, my beamish boy! O frabjous day! Callooh! Callay!” He chortled in his joy. ’Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe. '*100)
    assert result == '1 hours, 23 minutes, 0 seconds'
