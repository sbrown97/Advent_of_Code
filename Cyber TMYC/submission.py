import requests

url = r"https://yv9w75zly1.execute-api.us-east-1.amazonaws.com/dev/TMYC_Solution_Checker" # endpoint of the TMYC API

# Feel free to use the test below to be sure it's working for you.  But you'll want to customize the fields nested below "Item" for your problem and your submission (see below for the appropriate key to identify a question or part or subpart).
mysubmission = {
  "operation": "submit",
  "payload": {
    "Item": {
      "id": "rstewart@lmi.org",  # Change me!
      "question": "w4_ch",  # Change me!
      "submission": "hash" # Change me!
    }
  }
}

response = requests.post(url, json = mysubmission)  # doing the work

print(response.text) # because you want to see if your response was correct (or if there was an error!