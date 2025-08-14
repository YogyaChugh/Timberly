import requests

a = requests.get("https://yogya.pythonanywhere.com//get_leaderboard")
print(eval(a.content))