# importing the requests library
import requests

def send_req(msg):
    """send the prompt to the REST API and return the reply"""
    # api-endpoint
    URL = "https://ollama.usmanazi.site/prompt/" + msg;

    # sending get request and saving the response as response object
    r = requests.get(url = URL)
    if r.status_code != 200:
        print("Error: " + str(r.status_code) + " - " + r.text)
        return "error";
    
    # extracting data in json format
    return r.json()["reply"];


# print(send_req("who is Usman?"))