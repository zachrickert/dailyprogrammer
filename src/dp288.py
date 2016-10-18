"""Code for dailyprogramer challenge #288."""
from inputs import SAMPLE_288, CHALLENGE_288

punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

def alliteration(input):
    STOP_WORDS = '''I a about an and are as at be by com for from how in
    is it of on or that the this to was what when where who will with the'''

    stop_words = STOP_WORDS.split()
    is_alliteration = False
    for line in input.splitlines():
        alliteration_list = []
        if line.isdigit():
            # Ignore the first line with just the number.
            continue
        alliteration_list.append(' ')
        for word in line.split():
            word = word.rstrip(punctuation)
            if word not in stop_words:
                if word[0] == alliteration_list[-1][0]:
                    is_alliteration = True
                elif is_alliteration:
                    is_alliteration = False
                else:
                    alliteration_list.pop()
                alliteration_list.append(word)
        if not is_alliteration:
            alliteration_list.pop()
        is_alliteration = False
        print(' '.join(alliteration_list))


if __name__ == '__main__':
    alliteration(SAMPLE_288)
    alliteration(CHALLENGE_288)
