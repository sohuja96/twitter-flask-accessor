from flask import Flask
import twitterAuth
import requests
app = Flask(__name__)

trackUrl = "https://stream.twitter.com/1.1/statuses/filter.json"

api = twitterAuth.api

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/health")
def health():
    print(api)
    users = api.GetFriends()
    string = ""
    for user in users:
        string += user.name + ", "
    return api.VerifyCredentials().status.text

@app.route("/track/<tag>",
        methods=['GET'])
def track(tag):
    for i in api.GetStreamFilter(track=[tag]):
        print(i.get("text"), "`|`")
