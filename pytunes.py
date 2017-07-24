import requests
import logging as log
import json
import pprint
import urllib


class PyTunes:
    def __init__(self):
        self.search_url = 'https://itunes.apple.com/search?'
        self.__set_defaults()
        self.last_term = 0

    def __set_defaults(self):
        self.query_vals = {
            'term': None,
            'country': 'US',
            'media': 'all',
            'entity': None,
            'attribute': None,
            'limit': '25',
            'lang': 'en_us',
            'version': '2',
            'explicit': 'Yes'
        }

    def self_wrapper(func):
        def wrap_and_return(self, *args, **kwargs):
            func(self, *args, **kwargs)
            return self 
        return wrap_and_return

    @self_wrapper
    def term(self, term):
        self.query_vals['term'] = term
        self.last_term = 0

    @self_wrapper
    def country(self, country):
        self.query_vals['country'] = country
        self.last_term = 1

    @self_wrapper
    def media(self, media):
        self.query_vals['media'] = media
        self.last_term = 2

    @self_wrapper
    def entity(self, entity):
        self.query_vals['entity'] = entity
        self.last_term = 3

    @self_wrapper
    def attribute(self, attribute):
        self.query_vals['attribute'] = attribute
        self.last_term = 4

    @self_wrapper
    def limit(self, limit):
        if int(limit) > 200 or int(limit) < 1:
            print 'limit must be between 1 to 200'
        self.query_vals['limit'] = limit
        self.last_term = 5

    @self_wrapper
    def lang(self, lang):
        self.query_vals['lang'] = lang
        self.last_term = 6

    @self_wrapper
    def version(self, version):
        self.query_vals['version'] = version
        self.last_term = 7

    @self_wrapper
    def explicit(self, explicit):
        if int(explicit) is 1:
            explicit = 'Yes'
        elif int(explicit) is 0:
            explicit = 'No'
        self.query_vals['explicit'] = explicit
        self.last_term = 8

    @self_wrapper
    def help(self):
        key = self.query_vals['media']
        with open('opthelp.txt') as helpfile:
            hf = json.load(helpfile)
        if key not in hf[self.last_term]:
            pprint.pprint(hf[self.last_term])
        else:
            print key
            pprint.pprint(hf[self.last_term][key])

    def search(self):
        query_result = self.__request(self.search_url, self.query_vals)
        # print query_result.json()

    def __request(self, url, query_vals):
        query = self.__create_query(url, query_vals)
        # print query
        return requests.get(query)

    @staticmethod
    def __create_query(url, query_vals):
        if query_vals['term'] is None:
            raise ValueError('term is required to search')
        query_vals = dict((key, val) for key, val in query_vals.iteritems() if val)
        query = url + urllib.urlencode(query_vals)
        return query

    
pt = PyTunes()
pt.term('fjdlak fdjksafld fdsa').media('all').entity('movie').search()


