''' /api/amazon.py '''
from os import environ
import bottlenose
from bs4 import BeautifulSoup


class Amazon:
    ''' Class for wrapping Bottlenose, the Amazon API library '''
    def __init__(self, *args, **kwargs):
        self.amazon = bottlenose.Amazon(
                environ['AWS_ACCESS_KEY_ID'],
                environ['AWS_SECRET_ACCESS_KEY'],
                environ['AWS_ASSOCIATE_TAG'],
                Parser=lambda text: BeautifulSoup(text, 'lxml'))
    
    
    def search(self, set_id):
        ''' Wrapper for bottlenose ItemSearch method '''
        return self.amazon.ItemSearch(Keywords="Lego {}".format(set_id),
                                        Title=set_id,
                                        SearchIndex="Toys",
                                        # MerchantId="Amazon",
                                        ResponseGroup="Images,OfferSummary,Small")
