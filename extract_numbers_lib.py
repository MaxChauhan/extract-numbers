#! /usr/bin/env python
"""
Library

"""
import re

from bs4 import BeautifulSoup


def strip_seven(text):
    return text[5:]


def remove_years(text):
    year_pattern = r'[1-3][0-9]{3}'
    return re.sub(year_pattern, '', text)


def remove_notes(text):
    note_pattern = r'[Nn]ote [0-9]+'
    return re.sub(note_pattern, '', text)


def remove_dates(text):
    date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]+'
    return re.sub(date_pattern, '', text)


def remove_commas(text):
    return text.replace(',', '')


def parse_file(file) -> [int]:
    """
    :param file:
    :return:
    """
    # First strip out page numbers
    pagenum_pattern = r'<P STYLE="margin-top:0px;margin-bottom:0px" ALIGN="center"><FONT STYLE="font-family:Times New Roman" SIZE="2">[0-9 ]+</FONT></P>'
    pageless = re.sub(pagenum_pattern, '', file.read())

    # BeautifulSoup is a library that parses out the text from a HTML file
    soup = BeautifulSoup(pageless, 'html.parser')

    # Gets the raw text from the article
    text = soup.get_text()

    # Strip out known patterns
    text = strip_seven(text)
    text = remove_years(text)
    text = remove_notes(text)
    text = remove_dates(text)
    # Strip out commas so numbers like 13,500 turn into 13500
    text = remove_commas(text)

    digits = [float(x) for x in re.findall(r'\d+\.*\d?', text)]
    print(digits)
    rounded = [str(x)[0] for x in digits]
    print(rounded)
    return rounded
