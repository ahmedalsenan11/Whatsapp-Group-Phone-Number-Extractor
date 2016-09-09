#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import BeautiufulSoup class from bs4 package
from bs4 import BeautifulSoup


# paste complete div element having class infinite-list
html = '''
# paste your  div element
'''


# which concatenate phone number string
#  [ +91 99956 96485 ] to [ +919995696845 ]
def concatenate(contact):
    contact = contact.split()
    return "".join(contact)


def main():
    # Number of Contact in your group
    number_of_contact = 0

    # BeautifulSoup object html content as argument
    soup = BeautifulSoup(html, "lxml")

    # for loop goes through every span in html content
    for i in soup.find_all('span'):
        # if we found span element with class attribute "emojitext ellipsify" and its title attribute on None
        if i.get('class') == ['emojitext', 'ellipsify'] and i.get("title") is not None:
            print (concatenate(i.get_text()))
            number_of_contact += 1

    print "The Total Number of Contacts are %s" % (number_of_contact,)


if __name__ == "__main__":
    main()
