import requests
import random

# p = [[221113,'Yogya',150],[691233,'Milli Johnson',12],[814333,'Alia',32],[900993,'Dave P',78],[472243,'Miki Rosh',45],[177903,'Brandy',190]]
# p = ['W ']
p = ['Graham','Willow','Tristan','Rhys','Saoirse','Peregrine','Xylia','Orion','Orpheus','Ragnar','Viggo','Elara','Bronwen','Niamh','Sorcha','Eoghan']

# done = []
# for a in p:
#     while a[0] in done:
#         a[0] = random.randint(100000,100000000)
#     done.append(a[0])
#     print('ho5')
        

def register_users():
    k = 1
    for i in p:
        a = requests.post("https://yogya.pythonanywhere.com/register_user",data={'id':i[0],'name':i[1]})
        print(str(k) + " " + str(a.content))
        k+=1
        
def update_list():
    k = 1
    for i in p:
        a = requests.post("https://yogya.pythonanywhere.com/update_score",data={'id':i[0],'score':i[2]})
        print(str(k) + " " + str(a.content))
        k+=1
        
def all_players():
    a = requests.get("https://yogya.pythonanywhere.com/get_all_players")
    print(a.content)
    for i in eval(a.content):
        print(i)
        
def remove_player():
    k = 1
    for i in p:
        a = requests.post("https://yogya.pythonanywhere.com/remove_player_perm",data={"name": i})
        print(str(k) + " " + str(a.content))
        k+=1
        
# register_users()
# update_list()
# remove_player()
all_players()