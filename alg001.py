
print(" ... takes a moment to start ...")

from sample_texts import *

################################################################
# reference N3K

from newspaper import Article, Config

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0'
config = Config()
config.browser_user_agent = user_agent

# split out helper function for interactive use
def test00a(h_file, url='https://Example.Com/SomeArticle.html'):
    a = Article(url, config=config)
    with open(h_file) as f:
        h = f.read()
    a.download(input_html=h)
    a.parse()
    a.nlp()
    return a

def test00(h_file=HTML_1, url='https://Example.Com/SomeArticle.html'):
    a = test00a(h_file, url)
    return a.summary
    

################################################################
#
# This is the "basic upgrade" version
#
# XLNET
# see also:
#  https://medium.com/analytics-vidhya/text-summarization-using-bert-gpt2-xlnet-5ee80608e961

from summarizer import TransformerSummarizer

XLNet_model = None

def test01(body=TEXT_1):
    global XLNet_model
    if not XLNet_model:
        XLNet_model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
    full = ''.join(XLNet_model(body, min_length=60))
    return(full)


