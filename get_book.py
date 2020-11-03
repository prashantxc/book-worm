"""
This is to get "Book Links" from libgenesis. API requested from any 
kind of python server is possible.
@author prashantxc
@licence MIT License
"""

from libgen_api import LibgenSearch

book = LibgenSearch()

title = "Astronomy"
author = "Albert Einstein"

def get_by_title():
    """Returns Book on the basis of title"""
    response_on_title = book.search_title(title)

    return response_on_title


def get_by_author():
    """Returns Book on the basis of author"""
    response_on_author = book.search_author(author)

    return response_on_author

def get_title_filter():
    """Returns Book on the basis of title and corresponding filter"""
    title_filter = {
        "Author": "Robert",
        "Extension": "pdf"
    }
    
    response_title_filter = book.search_title_filtered(title, title_filter)

    return response_title_filter