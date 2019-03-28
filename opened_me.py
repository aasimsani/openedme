import flask
from forms import opened_me_form
from encryption import generate_hash, decrypt_hash

from flask import Flask,request, render_template,url_for,redirect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")


@app.route("/gotlink",methods=['GET','POST'])
def got_link():

    form = opened_me_form()
    # TODO Implement error handling from form

    hash = generate_hash(form.email.data,form.link.data)

    domain = "localhost:5000"
    link = domain + url_for('redirect_to') + "?he="+hash['email']+"&hl="+hash['link']

    return render_template("gotlink.html",form=form, link=link)


@app.route("/redirect",methods=['GET','POST'])
def redirect_to():

    #Get data from the link
    link = request.args['hl']
    email = request.args['he']

    #Send email
    

    decrypted = decrypt_hash(email,link)

    return redirect(decrypted['link'])

if __name__ == "__main__":
    app.run(debug=True)