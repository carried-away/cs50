from cs50 import get_string
import re


def main():
    user_input = get_string("Text: ")
    num_sentences = 0
    num_words = 0
    num_chars = 0

    num_chars = len(user_input)
    num_words = len(user_input.split())

    # Find all non-alphabetic characters (excluding spaces)
    non_alpha_chars = re.findall(r'[^a-zA-Z\s]', user_input)
    num_chars -= len(non_alpha_chars)
    num_chars -= user_input.count(" ")

    for i in user_input:
        if i in '!.?':
            num_sentences += 1

    # OG sanity check
    # print(f"Chars: {num_chars}")
    # print(f"Words: {num_words}")
    # print(f"Sentences: {num_sentences}")

    index = calculate_coleman_liau_index(num_chars, num_words, num_sentences)

    if index >= 16:
        grade = 'Grade 16+'
    elif index < 1:
        grade = 'Before Grade 1'
    else:
        grade = 'Grade ' + str(index)

    print()
    print(f'{grade}')


def calculate_coleman_liau_index(chars, words, sentences):

    # Coleman-Liau index
    # where L is the average number of letters per 100 words in the text
    # S is the average number of sentences per 100 words in the text

    L = (chars / words) * 100
    S = (sentences / words) * 100

    # Compute the Coleman-Liau index
    # 0.0588 * L - 0.296 * S - 15.8
    coleman_liau_index = 0.0588 * L - 0.296 * S - 15.8

    result = round(coleman_liau_index)
    return result


main()
