import requests

p = [[221113,'Yogya',150],[691233,'Milli Johnson',12],[814333,'Alia',32],[900993,'Dave P',78],[472243,'Miki Rosh',45],[177903,'Brandy',190]]


def register_users():
    for i in p:
        a = requests.post("https://yogya.pythonanywhere.com/register_user",data={'id':i[0],'name':i[1]})
        print(a.content)
        
def update_list():
    for i in p:
        a = requests.post("https://yogya.pythonanywhere.com/update_score",data={'id':i[0],'score':i[2]})
        print(a.content)
        
register_users()
update_list()