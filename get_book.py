"""
This is to get "Book Links" for libgenesis. API requested from any 
kind of python server is possible.
@author prashantxc
@licence MIT License
"""

from libgen_api import LibgenSearch

book = LibgenSearch()

title = "A brief History of Time"

def get_by_title():
    """Returns Book on the basis of title"""
    
    response_on_title = book.search_title(title)

    return response_on_title
