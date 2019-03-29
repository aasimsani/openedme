import flask
from forms import opened_me_form
from encryption import generate_hash, decrypt_hash

from flask import Flask,request, render_template,url_for,redirect
from send_email import send_email_mj
from config import DOMAIN_NAME,IPSTACK_KEY
from make_tiny import make_tiny_link
import requests
import json

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
    
    
    url = "http://api.ipstack.com/"+"{}".format(request.headers.get('X-Forwarded-For'))+"?access_key=%s" % IPSTACK_KEY

    r = requests.get(url)
    j = json.loads(r.text)
    
    
    city = j['city']
    continent = j['continent_name']
    country = j['country_name']
    region = j['region_name']

    if city == None:
        city = ""
    
    if continent == None:
        continent = ""
    
    if country == None:
        country = ""

    if region == None:
        region = ""

    location = continent+"/"+country+" - "+region+"/"+city

    email = decrypted['email']
    link = decrypted['link']

    if "http" not in link:
        link = "http://" + link



    #Send email
    send_email_mj(email,link,location)




    return redirect(link)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
