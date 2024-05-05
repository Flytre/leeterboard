import requests
import json

BASE_URL = "https://leetcode-stats-api.herokuapp.com/"
USERLIST = "../bin/users.json"

with open(USERLIST, 'r') as u:
    global users
    users = json.load(u)

rankings = []

for user, username in users.items():
    res = requests.get(BASE_URL + username).json()
    cal = res['submissionCalendar']
    submits = sum(cal.values())
    rankings.append((submits, user))

rankings.sort()
rankings.reverse()

# make table
with open("../readme.md", 'w') as f:
    f.write("| Name | Submissions |\n")
    for submits, user in rankings:
        f.write(f"| {user} | {submits} |\n")
