import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Search wikipedia for name"""

    my_wiki = wikipedia.search(name)
    return my_wiki


def phrase(name):
    """This is a phrase analyzer for wikipedia page"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
