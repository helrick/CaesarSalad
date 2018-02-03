from bs4 import BeautifulSoup

import requests

def makeSoupFromUrl(url='https://en.wikiversity.org/wiki/Wikidebate'):
    #url = "https://en.wikiversity.org/wiki/Wikidebate"

    # get the html from the url
    r = requests.get(url)
    data = r.text

    # Make the soup
    # The soup is a tree constructed from the html
    soup = BeautifulSoup(data, "html.parser")
    #print soup
    #print soup.contents
    return soup


def findCategories(soup):
    wikiContents = soup.find('h2', id="Debates")
    categoryTags = wikiContents.find_all('h3') # Should be an array
    categories = []
    for category in categoryTags:
        categories.append(category.get_text())
    return [categories, categoryTags]


def findCategoryTopics(category, categoryTags):
    # returns a list of the debate topics for the category
    topicTags = categoryTags.find_all('h2', id=category)
    topics = []
    for topic in topicTags:
        topics.append(topic.get_text())
    return [topics, topicTags]


def getTopicURL(topicTag):
    # param: a single topic tag. extract the href link
    topicURL = topicTag['href']
    return topicURL

def getTopicAgainstPoints(url):
    # follow a url to a topic,
    # get all the against arguments,
    # put into an array
    soup = makeSoupFromUrl(url)
    print soup.get_text()
    argumentfor = soup.find(id="Arguments_for")
    argumentforhtml = argumentfor.parent
    print argumentforhtml

    #print arguments

def main():
    getTopicAgainstPoints('https://en.wikiversity.org/wiki/Should_we_colonize_Mars%3F')

main()




