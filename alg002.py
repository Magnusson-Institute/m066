

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

def test04a(article=TEXT_1):
    # example from:
    # https://www.thepythoncode.com/article/text-summarization-using-huggingface-transformers-python

    from transformers import pipeline
    from transformers import T5ForConditionalGeneration, T5Tokenizer

    # initialize the model architecture and weights
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    # model = T5ForConditionalGeneration.from_pretrained("t5-large")

    # initialize the model tokenizer
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    # tokenizer = T5Tokenizer.from_pretrained("t5-large")

    # encode the text into tensor of integers using the appropriate tokenizer
    inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)

    # generate the summarization output

    # (example code settings:)
    # outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    outputs = model.generate(inputs, max_length=500, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)

    # just for debugging
    # print(outputs)

    return(tokenizer.decode(outputs[0]))

def test04b(article=TEXT_1):
    # from:
    # http://datageek.fr/abstractive-summarization-with-huggingface-pre-trained-models/

    from transformers import pipeline
    from transformers import T5ForConditionalGeneration, T5Tokenizer

    # Initialize the HuggingFace summarization pipeline
    # summarizer = pipeline("summarization")
    
    #setting the pipeline
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

    # run the model
    # return(summarizer(article, min_length=25, max_length=50))
    return(summarizer(article, min_length=150, max_length=500))

# this one seems to work the best?
def test04c(article=TEXT_1):
    # from:
    # http://datageek.fr/abstractive-summarization-with-huggingface-pre-trained-models/

    from transformers import pipeline

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")

    # run the model
    return(summarizer(article, min_length=150, max_length=500))


def test04d(article=TEXT_1):
    from transformers import pipeline
    from transformers import GPT2Tokenizer, GPT2Model

    # example from:
    # https://www.thepythoncode.com/article/text-summarization-using-huggingface-transformers-python

    # initialize the model architecture and weights
    model = GPT2Model.from_pretrained("gpt2")

    # initialize the model tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # encode the text into tensor of integers using the appropriate tokenizer
    # inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)
    inputs = tokenizer.encode("summarize: " + article, return_tensors="pt")

    # generate the summarization output

    # (example code settings:)
    # outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    outputs = model.generate(inputs, max_length=500, min_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)

    # just for debugging
    # print(outputs)

    return(tokenizer.decode(outputs[0]))

