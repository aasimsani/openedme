


def generate_hash(email,link):

    # TODO: Implement stronger scrambling
    scrambled_link = ""
    scrambled_email = ""

    for letter in link:

        scrambled_link += chr(ord(letter)+3)
    
    for letter in email:
        scrambled_email += chr(ord(letter)+3)

        
    
    return {"email":scrambled_email,"link":scrambled_link}


def decrypt_hash(email_hash,link_hash):

    email = ""
    link = ""

    for letter in link_hash:
        link += chr(ord(letter)-3)

    for letter in email_hash:
        email += chr(ord(letter)-3)
    
    return {"email":email,"link":link} 