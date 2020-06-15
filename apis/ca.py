#!/usr/bin/env python
"""
a script for getting materials from the Chronicling America website
"""

# Make these modules available
import requests
import json

__author__ = "your-name"

# Create a variable called 'api_search_url' and give it a value
api_search_url = 'https://chroniclingamerica.loc.gov/search/pages/results/'

# This creates a dictionary called 'params' and sets values for the API's mandatory parameters
params = {
    'proxtext': 'archeology' # Search for this keyword
}

# This adds a value for 'encoding' to our dictionary
params['format'] = 'json'

# This sends our request to the API and stores the result in a variable called 'response'
response = requests.get(api_search_url, params=params)

# This shows us the url that's sent to the API
print('Here\'s the formatted url that gets sent to the ChronAmerca API:\n{}\n'.format(response.url))

# This checks the status code of the response to make sure there were no errors
if response.status_code == requests.codes.ok:
    print('All ok')
elif response.status_code == 403:
    print('There was an authentication error. Did you paste your API above?')
else:
    print('There was a problem. Error code: {}'.format(response.status_code))

# Get the API's JSON results and make them available as a Python variable called 'data'
data = response.json()

# Let's prettify the raw JSON data and then display it.
# We're using the Pygments library to add some colour to the output, so we need to import it

from pygments import highlight, lexers, formatters

# This uses Python's JSON module to output the results as nicely indented text
formatted_data = json.dumps(data, indent=2)

# This colours the text
highlighted_data = highlight(formatted_data, lexers.JsonLexer(), formatters.TerminalFormatter())

# And now display the results
print(highlighted_data)

# dump json to file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
    