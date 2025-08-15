import flask
import os
from cryptography.fernet import Fernet
import requests

class User:
    id: int
    name: str
    score: int
    def __init__(self,id,name,score=0):
        self.id = id
        self.name = name
        self.score = score
    def __repr__(self):
        return str([self.name, self.score])
    def __str__(self):
        return str([self.name, self.score])
    def __eq__(self, other) -> bool:
        try:
            if other.id==self.id and other.name==self.name and other.score==self.score:
                return True
        except:
            return False
        return False

users = []

KEY_FILE = "secret.env"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as sec:
        MAIN_KEY = sec.read()
else:
    MAIN_KEY = Fernet.generate_key()
    with open(KEY_FILE, "wb") as sec:
        sec.write(MAIN_KEY)
key = Fernet(MAIN_KEY)

if not os.path.exists("user_data.log"):
    with open("user_data.log",'w') as file:
        temp_data = "{'Users': {}}".encode()
        encrypted_msg = key.encrypt(temp_data)
        file.write(encrypted_msg.decode())
else:
    with open("user_data.log",'r') as file:
        data = file.read()
        data = key.decrypt(data).decode()
        a_data = eval(data)
    tdata = a_data['Users']
    for p in tdata:
        users.append(User(p,eval(tdata[p])[0],int(eval(tdata[p])[1])))
app = flask.Flask(__name__)

@app.get("/")
def root():
    return "There is no information on this page!"

@app.post("/register_user")
def register():
    id = int(flask.request.form["id"])
    name = flask.request.form["name"]
    user = User(id,name)
    users.append(user)
    with open("user_data.log",'r') as file:
        data = file.read()
        data = key.decrypt(data).decode()
        a_data = eval(data)
    with open("user_data.log",'w') as file:
        a_data['Users'][id] = str(user)
        file.write(key.encrypt(str(a_data).encode()).decode())
    return "success"

@app.get("/get_leaderboard")
def get_leaderboard():
    id = int(flask.request.form["id"])
    name = flask.request.form["name"]
    user_found = None
    user_index = 0
    i = 1
    final = []
    for user in users:
        if i<=4:
            final.append([i,user.name,user.score])
        if user.id == id:
            user_found = user
            user_index = i
        i+=1
    if user_index>4:
        if user_found:
            us = [user_index, user_found.name, user_found.score]
            final.append(us)
            return final
        else:
            requests.post("https://yogya.pythonanywhere.com/register_user",data={'id': id,'name': name})
            return ""
    else:
        return final

@app.get("/get_username")
def username():
    id = int(flask.request.form["id"])
    for user in users:
        if id == user.id:
            return user.name
    return ""

@app.get("/get_score")
def score():
    id = int(flask.request.form["id"])
    for user in users:
        if id == user.id:
            return str(user.score)
    return ""


@app.post("/update_score")
def update_score():
    id = int(flask.request.form["id"])
    score = int(flask.request.form["score"])
    found_user = None
    for user in users:
        if user.id == id:
            found_user = user
            if user.score<score:
                user.score = score
                for k in users:
                    found_the_user = False
                    completed = False
                    temp = None
                    i = users.index(k)
                    if user == k:
                        break
                    if user.score>k.score:
                        print(f"{user} is greater than {k}")
                        found_the_user = True
                        temp = k
                        users[i] = user
                    while found_the_user and temp!=None:
                        if i==len(users)-1:
                            users.append(temp)
                            completed = True
                            break
                        bro = users[i+1]
                        i+=1
                        print(f"Check for {bro} and {temp}")
                        if bro!=user:
                            print(f"Swapped {bro} with {temp}")
                            temp2 = bro
                            users[i] = temp
                            temp = temp2
                        else:
                            print(f"Swapped {bro} with {temp}")
                            users[i] = temp
                            completed = True
                            break
                    if completed:
                        print(f"List: {users}")
                        break
                                
            break
    if not found_user:
        return ""
    a_list = {}
    for user in users:
        a_list[user.id] = str(user)
    a_list = str({'Users': a_list})
    with open("user_data.log",'w') as file:
        file.write(key.encrypt(str(a_list).encode()).decode())
    return "Success"