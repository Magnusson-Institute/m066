#
# this requires an account with Forefront.ai
# you will need your model key in the env variable:
# $ export FOREFRONT_MODEL_KEY='... your key... '
#

import requests, json, os
from sample_texts import *

# call with text and range of compression
def test05a(the_text=TEXT_5, c_range=range(1,5)):
    # Models keys are used for Completions requests. Platform keys are used for Resources requests.
    headers = {
        "Authorization": f"Bearer {os.getenv('FOREFRONT_MODEL_KEY')}",  # model (completion) key
        "Content-Type": "application/json"
    }
    # set to one of the ones in the sample texts
    # note: '5' matches the forefront.ai blog post example
    for c in c_range:
        print(f"Running with compression {c} ... ")
        body = {
            "compression_level": c,  # range from 1 (longest) to 5 (shortest)
            "text": the_text
        }
        res = requests.post(
            "https://solutions.forefront.ai/v1/organization/dLzOXuUb3LeI/summarize", # hack, in future use your team ID
            json=body,
            headers=headers
        )
        data = res.json()
        if ('summary' in data):
            summary = data['summary']
            print(f"Compression {c} went from {len(the_text)} characters to {len(summary)}:\n{'='*40}\n{summary}\n{'='*40}\n")
        else:
            print(f"####\n####  Problem: '{data}'\n####")
