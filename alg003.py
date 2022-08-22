#
# this requires an account with Forefront.ai
# you will need your model key in the env variable:
# $ export FOREFRONT_MODEL_KEY='... your key... '
#

import requests, json, os
from sample_texts import *

# Models keys are used for Completions requests. Platform keys are used for Resources requests.
headers = {
    "Authorization": f"Bearer {os.getenv('FOREFRONT_MODEL_KEY')}",  # model (completion) key
    "Content-Type": "application/json"
}

the_text = TEXT_1 # set to one of the ones in the sample texts

body = {
    "compression_level": 5,  # range from 1 (longest) to 5 (shortest)
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
    print(summary)
    print(f"\nWent from {len(the_text)} characters to {len(summary)}")
else:
    print(f"####\n####  Problem: '{data}'\n####")
