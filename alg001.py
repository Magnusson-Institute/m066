
from summarizer import TransformerSummarizer

from sample_texts import *

# see also:
# https://medium.com/analytics-vidhya/text-summarization-using-bert-gpt2-xlnet-5ee80608e961

XLNet_model = None
def test01(body=TEXT_1):
    global XLNet_model
    if not XLNet_model:
        XLNet_model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
    full = ''.join(XLNet_model(body, min_length=60))
    return(full)
