from bs4 import BeautifulSoup
from functools import partial


def get_text(elem):
    """
    get tag
    :param elem:
    :return:
    """
    return elem.text


def get_filter():
    """
    get filtering functions for east/west conference
    :return:
    """
    filter_func = lambda table, element: \
        [] != element.find_all('th', attrs={'aria-label': table})
    east_func = partial(filter_func, 'Eastern Conference')
    west_func = partial(filter_func, 'Western Conference')
    return [east_func, west_func]


def link(tags):
    """
    change teams to their links
    :param tags:
    :return:
    """
    def apply_link(tag):
        tag_link = tag.find_all('a')
        if tag_link != [] and len(tag.text) == 3:
            tag.string.replace_with(tag_link[0]['href'])
        return tag

    return list(map(apply_link, tags))