from mailjet_rest import Client
from config import MJ_APIKEY_PUBLIC,MJ_APIKEY_PRIVATE 

api_key = MJ_APIKEY_PUBLIC
api_secret = MJ_APIKEY_PRIVATE



def send_email_mj(email,link):

    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
    'Messages': [
                    {
                            "From": {
                                    "Email": "openedme@gmail.com",
                                    "Name": "Opened Me"
                            },
                            "To": [
                                    {
                                            "Email": email,
                                            "Name": ""
                                    }
                            ],
                            "Subject": "Your link was opened.",
                            "TextPart": """
                                        Your link %s was opened.
                                        Please support Opened Me via Patreon: https://patreon.com/openedme
                                        """ % link,
                            "HTMLPart": ""
                    }
            ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())

    return True
