#!/usr/bin/env python3
"""
Author : Krishna Sandeep Dharga (krishnasandeep.d17@gmail.com)
Date   : 05/19/2021
Purpose: Crowsnest exercise from Tiny Python Projects book
         Get a word as a command line argument,
         get an appropriate article based on the first letter
         concatenate article and word to a string and print!
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='crows nest -- choose the correct article!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', help='A word')

    return parser.parse_args()


def with_article(word):
    """Get appropriate consonant for the word entered"""

    if word[0].upper() in 'AEIOU':
        article_word = 'an ' + word
    else:
        article_word = 'a ' + word

    return article_word


def main():
    """Main function"""

    args = get_args()
    word = args.word

    print('Ahoy, Captain, {} off the larboard bow!'.format(
        with_article(word)))


if __name__ == '__main__':
    main()
