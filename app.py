from flask import Flask, jsonify
import requests
app = Flask(__name__)
URL = "https://api.github.com"

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/user/<username>')
def retrieve_user_info(username):
    user = get_followers(username, 5)
    user['user'] = username
    if len(user['followers']) > 0:
        for follower in user['followers']:
            follower['followers'] = get_followers(follower['user'], 5)
    return jsonify(user)

@app.route('/test/user/<username>')
def test_user_info(username):
    user = get_followers(username, 5)
    user['user'] = username
    if len(user['followers']) > 0:
        for follower in user['followers']:
            follower['followers'] = get_followers(follower['user'], 5)
    return jsonify(user)

def get_followers(username, limit):
    user = {}
    followers_url = '/users/' + username + '/followers'
    r = requests.get(url = URL + followers_url)
    data = r.json()
    if len(data) > 0:
        user['followers'] = []
        for index, follower in enumerate(data):
            new_follower = {}
            new_follower['user'] = follower['login']
            user['followers'].append(new_follower)
            if index == (limit - 1):
                break
    else:
        user['followers'] = 'User has 0 followers'
    return user
