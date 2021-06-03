"""
Writing test double classes can become tedious pretty quickly, because
you often require one class per method called in the test, and all of
these classes must be set up to correctly chain their responses. If you
write multiple test scenarios, you either have to make the test doubles
generic enough to cover several scenarios or repeat nearly the same
code all over again.
Mock objects offer a more convenient solution. These are objects that
you can easily configure to respond in predefined ways.
"""

from unittest import mock
import requests

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


def test_with_test_mock():
    from unittest.mock import Mock
    mock_requests = Mock()
    mock_requests.get.return_value.text = 'aa bbb c'
    result = most_common_word_in_web_page(
        ['a', 'b', 'c'],
        'https://python.org/',
        user_agent=mock_requests
    )

    assert result=='b',\
        'most_common_word_in_web_page tested with test mock'
    assert mock_requests.get.call_count == 1
    assert mock_requests.get.call_args[0][0]\
        == 'https://python.org/', 'called with right URL'


"""
The first two lines of this test function import the class Mock and create
an instance from it. Then the real magic happens.

mock_requests.get.return_value.text = 'aa bbb c'

This installs an attribute, get, in object mock_requests, which, when it
is called, returns another mock object. The attribute text on that second
mock object has an attribute text, which holds the string 'aa bb c'.

Let’s start with some simpler examples. If you have a Mock object
m, then m.a = 1 installs an attribute a with value 1. On the other hand,
m.b.return_value = 2 configures m, so that m.b() returns 2.

This installs an attribute, get, in object mock_requests, which, when it
is called, returns another mock object. The attribute text on that second
mock object has an attribute text, which holds the string 'aa bb c'.
Let’s start with some simpler examples. If you have a Mock object
m, then m.a = 1 installs an attribute a with value 1. On the other hand,
m.b.return_value = 2 configures m, so that m.b() returns 2.
You can continue to chain, so m.c.return_value.d.e.return_value = 3
makes m.c().d.e() return 3. In essence, each return_value in the
assignment corresponds to a pair of parentheses in the call chain.
In addition to setting up these prepared return values, mock objects also
record calls. The previous example checked the call_count of a mock object,
which simply records how often that mock has been called as a function.
The call_args property contains a tuple of arguments passed to its
last call. The first element of this tuple is a list of positional arguments, the
second a dict of named arguments.
If you want to check multiple invocations of a mock object, call_args_
list contains a list of such tuples.

"""