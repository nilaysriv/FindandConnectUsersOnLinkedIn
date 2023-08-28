import requests
import json

def bioinformatics():
 url = "https://api.linkedin.com/v2/search/people?q=bioinformatics&location=New+Delhi"
  headers = {
    "Authorization": "Client-ID ENTER-YOUR-CLIENT-ID ENTER-YOUR-CLIENT-SECRET",
  }

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    people = json.loads(response.content)["people"]

    for person in people:
      print(person["name"])
      print(person["headline"])
      print(person["url"])

      # Connect with the person automatically
      requests.post(person["url"] + "/connect")

  else:
    print("Error: {} {}".format(response.status_code, response.content))


if __name__ == "__main__":
  bioinformatics()
