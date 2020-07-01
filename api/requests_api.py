import requests

class RequestsApi:

    url = "http://localhost:3000"
    headers = {}

    @staticmethod
    def get_login(user):
        try:
            res = requests.post(RequestsApi.url+"/users/login", data={"email":user.get_email(),"password":user.get_password()})
            return res.json()
        except:
            return "False"

    @staticmethod
    def get_register(user):
        try:
            res = requests.post(RequestsApi.url+"/users/register", data={"email":user.get_email(),"password":user.get_password()})
            return res.json()
        except:
            return "False"

    @staticmethod
    def get_all(var=''): # 'asc' || 'desc'
        try:
            res = requests.get(RequestsApi.url+"/estates/get/all?sort="+var)
            return res.json()
        except:
            return "False"

    @staticmethod
    def get_by_user(user):
        try:
            res = requests.get(RequestsApi.url+"/estates/get/all/"+user)
            return res.json()
        except:
            return "False"

    @staticmethod
    def get_save(estate):
        try:
            data = {"title":estate.get_title(),"type":estate.get_type(),"address":estate.get_address(),"rooms":estate.get_rooms(),"price":estate.get_price(),"area":estate.get_area(),"owner":estate.get_owner()}
            res = requests.request("POST", RequestsApi.url + "/estates/add", data=data)
            return res.json()
        except:
            return False

    @staticmethod
    def get_single(id):
        try:
            res = requests.get(RequestsApi.url+"/estates/get/" + id)
            return res.json()
        except:
            return False

    @staticmethod
    def single_update(id):
        try:
            res = requests.get(RequestsApi.url+"/estates/get/" + id)
            return res.json()
        except:
            return False

    @staticmethod
    def delete_api(id):
        try:
            res = requests.delete(RequestsApi.url+"/estates/delete/" + id)
            return res.json()
        except:
            return False

    @staticmethod
    def update_api(id):
        try:
            data = {"title":estate.get_title(),"type":estate.get_type(),"address":estate.get_address(),"rooms":estate.get_rooms(),"price":estate.get_price(),"area":estate.get_area()}
            res = requests.request("PUT", RequestsApi.url + "/estates/update/" + id, data=data)
            return res.json()
        except:
            return False
