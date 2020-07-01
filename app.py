import requests
from flask import Flask, render_template, request, redirect, url_for, flash, session
from api.requests_api import RequestsApi
from models.Estates import Estate

app = Flask(__name__)
app.secret_key = "asdf123456"

def session_validate():
    if 'login' in session:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('/layouts/session.html')

@app.route('/register')
def register():
    return render_template('/layouts/register.html')

@app.route('/save', methods=['POST'])
def save():

    if request.method == 'POST':
        try:

            titleInput = request.form['titleInput']
            typeInput = request.form['typeInput']
            addressInput = request.form['addressInput']
            roomInput = request.form['roomInput']
            priceInput = request.form['priceInput']
            areaInput = request.form['areaInput']
            estate = Estate(title=titleInput,type_=typeInput,
                     address=addressInput,rooms=int(roomInput),
                     price=int(priceInput),area=areaInput)

            res = RequestsApi.get_save(estate)
            print(res)

            return redirect(url_for('listed'))

        except:

            return "Not Saved"

@app.route('/create')
def create():
    return render_template('/layouts/create.html')

@app.route('/edit', methods=['PUT'])
def edit():
    if request.method == 'PUT':
        try:

            titleInput = request.form['titleInput']
            typeInput = request.form['typeInput']
            addressInput = request.form['addressInput']
            roomInput = request.form['roomInput']
            priceInput = request.form['priceInput']
            areaInput = request.form['areaInput']
            estate = Estate(title=titleInput,type_=typeInput,
                     address=addressInput,rooms=int(roomInput),
                     price=int(priceInput),area=areaInput)

            res = RequestsApi.update_api(estate)
            print(res)

            return redirect(url_for('listed'))

        except:

            return "Update Not complete"

@app.route('/update/<id>')
def update(id):
    res = RequestsApi.single_update(id)
    return render_template('/layouts/edit.html', data = res['res']['data'])

@app.route('/view/<id>')
def view(id):
    res = RequestsApi.get_single(id)
    return render_template('/layouts/view.html', data = res['res']['data'])

@app.route('/listed')
def listed():
    res = RequestsApi.get_all()
    return render_template('/index.html', _data = res['res']['data'])


@app.route('/delete/<id>')
def delete(id):
    res = RequestsApi.delete_api(id)
    return redirect(url_for('listed'))



if __name__ == '__main__':
    app.run(port=8081, debug=True)



