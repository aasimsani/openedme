import flask
from forms import opened_me_form
from encryption import generate_hash, decrypt_hash

from flask import Flask,request, render_template,url_for,redirect
from send_email import send_email_mj
from config import DOMAIN_NAME
from make_tiny import make_tiny_link

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")


@app.route("/gotlink",methods=['GET','POST'])
def got_link():

    form = opened_me_form()
    # TODO Implement error handling from form

    hash_data = generate_hash(form.email.data,form.link.data)

    domain = DOMAIN_NAME
    redirect_url = url_for('redirect_to')
    tiny_url = make_tiny_link(hash_data,redirect_url,domain)

    return render_template("gotlink.html",form=form, link=tiny_url)


@app.route("/redirect",methods=['GET','POST'])
def redirect_to():

    #Get data from the link
    link = request.args['hl']
    email = request.args['he']

    decrypted = decrypt_hash(email,link)

    email = decrypted['email']
    link = decrypted['link']

    if "http" not in link:
        link = "http://" + link



    #Send email
    send_email_mj(email,link)




    return redirect(link)

if __name__ == "__main__":
    app.run(debug=True)