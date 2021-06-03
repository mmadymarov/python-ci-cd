import requests
"""
In this example we applying dependency injection for requests
python build in function, we ourself writing requests instance
that replicate as requests and out test will not depend on the requests
instance in the future, by doing this we will not be independent on python
requests instance
"""
def most_common_word(words, text):
    """
    finds the most common word from a list of words
    in a piece of text
    """
    word_frequency = {w:text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]


def most_common_word_in_web_page(words, url, user_agent=requests):
    """
    Developer can put her/his user_agent
    """
    response = user_agent.get(url)
    return most_common_word(words, response.text)


def test_with_double_test():
    """We write class to insert injection"""

    class TestResponse():
        text = 'aa bbb cc'
    
    class TestUserAgent():
        def get(self, url):
            self.url = url
            return TestResponse()

    test_ua = TestUserAgent()
    result = most_common_word_in_web_page(
        ['a', 'b', 'c'],
        'https://python.org/',
        user_agent=test_ua
    )
    assert result == 'b',\
        'most_common_word_in_page tested with test double'
    
    assert test_ua.url == 'https://python.org/'


"""
The technique demonstrated in this section is a simple form of
dependency injection. 2 The caller has the option to inject an object or class
on which a function depends.
Dependency injection is useful not just for testing but also for making
software more pluggable. For example, you might want your software to be
able to use different storage engines in different contexts, or different XML


parsers, or any number of other pieces of software infrastructure for which
multiple implementations exist.
"""


