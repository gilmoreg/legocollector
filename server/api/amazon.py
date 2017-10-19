""" /api/amazon.py """
from os import environ
import time
import bottlenose
from bs4 import BeautifulSoup
# noinspection PyCompatibility
from urllib.error import HTTPError


class Amazon(object):
    """ Class for wrapping Bottlenose, the Amazon API library """

    def __init__(self):
        self.amazon = bottlenose.Amazon(
            environ['AWS_ACCESS_KEY_ID'],
            environ['AWS_SECRET_ACCESS_KEY'],
            environ['AWS_ASSOCIATE_TAG'],
            Parser=lambda text: BeautifulSoup(text, 'lxml'),
            MaxQPS=0.5)
        # ErrorHandler=self.error_handler)

    def search(self, set_id):
        """ Wrapper for bottlenose ItemSearch method """
        return self.amazon.ItemSearch(Keywords="Lego {}".format(set_id),
                                      Title=set_id,
                                      SearchIndex="Toys",
                                      # MerchantId="Amazon",
                                      ResponseGroup="Images,OfferSummary,Small")

    def error_handler(self, err):
        """
        Error handler for bottlenose
        Retry after wait on 503 errors
        """
        ex = err['exception']
        if isinstance(ex, HTTPError) and ex.code == 503:
            print('503 error')
            time.sleep(0.1)
            return True
        # Do not retry on other types of errors
        return False
