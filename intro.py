#!/usr/bin/env python3

"""Retrieve and print words from URL

Usage:

    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


# creating global varables requires "global" keyword within function
count = 0
def show_count():
    print(count)


def set_count(c):
    global count # reference global variable c
    count = c

def fetch_words(url):
    """Fetch a list of words from a URL.

     Args:
        url: The Url of a UTF-8 text document.

     Returns:
        A list of strings containing the words from the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()


def print_items(items):
    """Print items one per line.

     Args:
        An iterable series of printable items
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from the URL.

     Args:
        url: The Url of a UTF-8 text document.
    """
    print('sup')
    words = fetch_words(url)
    print_items(words)


def default_arg_prac(message, border='='):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

# using immutable None object as a sentinel
def mutable_default_values_addSpam(menu=None): # [] causes mutable object
    # avoid output "[spam, spam, spam]" by using immutable (ie int string)
    # objects for default values.
    if menu is None:
        menu = []
        print("true")
    menu.append("spam")
    print(menu)
    return menu

if __name__ == '__main__':
    

    """""
    show_count()
    set_count(5)
    show_count()
    """

    """
    breakfast = ["bacon", "eggs"]
    mutable_default_values_addSpam(breakfast)
    mutable_default_values_addSpam()
    mutable_default_values_addSpam()
    """
    #default_arg_prac("hey", border="/")
    # main(sys.argv[1]) # The 0th arg is the module filename