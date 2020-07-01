import requests

class RequestsApi:

    url = "http://localhost:3000"
    headers = {}

    @staticmethod
    def get_all():
        try:
            res = requests.get(RequestsApi.url+"/estates/get/all")
            return res.json()
        except:
            return "False"

    @staticmethod
    def get_save(estate):
        try:
            data = {"title":estate.get_title(),"type":estate.get_type(),"address":estate.get_address(),"rooms":estate.get_rooms(),"price":estate.get_price(),"area":estate.get_area()}
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
