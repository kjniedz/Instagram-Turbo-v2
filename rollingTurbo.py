import requests
import json
import threading
import uuid
import getpass
import sys
import time
import random
import string
import re
from bs4 import BeautifulSoup
import subprocess as subprocess
from colorama import Fore, init
init()

def clear():
    sp.call('clear', shell=True)
 
def login():
    global myUUID, myCSRF, mySessionID, myMID, myDS_USER_ID, nUsername, mEmail, mBio, mFirstName, nNumber
    clear()
    print(Fore.CYAN+'*'*47)
    print('+'+Fore.WHITE+'Supa Fast Turbo'+Fore.CYAN+'+')
    print('+'+Fore.WHITE+'Stealing Your Handles and Girls'+Fore.CYAN+'+')
    print('*'*47+Fore.WHITE)
 
    nUsername = input(Fore.RED+'Enter Username: '+Fore.GREEN)
    nPassword = getpass.getpass(Fore.RED+'Enter Password: ')
    mBio = input('Enter Custom Bio: '+Fore.GREEN)
    nNumber = getpass.getpass(Fore.RED+'Enter Number: '+Fore.GREEN)
    myUUID = str(uuid.uuid4())
 
    try:
        paramsPost = {"ig_sig_key_version":"5","signed_body":"fa61f4be32e827c7152e38a075e36142d8313ba582d6437f07539b00a03f454e.{\"reg_login\":\"0\",\"password\":\""+nPassword+"\",\"device_id\":\""+myUUID+"\",\"username\":\""+nUsername+"\",\"adid\":\"FE4FD084-9DCB-481A-A248-57E0E32E25ED\",\"login_attempt_count\":\"0\",\"phone_id\":\""+myUUID+"\"}"}
        headers = {"Accept":"*/*","X-IG-Capabilities":"36r/Vw==","User-Agent":"Instagram 44.0.0.17.95 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+","Connection":"close","X-IG-ABR-Connection-Speed-KBPS":"0","X-IG-Connection-Speed":"-1kbps","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US;q=1","X-IG-Connection-Type":"WiFi","X-IG-App-ID":"124024574287414","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        r = requests.post("https://i.instagram.com/api/v1/accounts/login/", data=paramsPost, headers=headers)
        decoded = r.content.decode('utf-8')
        if "logged_in_user" in decoded:
            print(Fore.WHITE+'['+Fore.GREEN+'+'+Fore.WHITE+']'+' Successfully Logged In!')
            myCSRF = r.cookies['csrftoken']
            myDS_USER = r.cookies['ds_user']
            myDS_USER_ID = r.cookies['ds_user_id']
            mySessionID = r.cookies['sessionid']
            myMID = r.cookies['mid']
            try:
                paramsGet = {"ig_sig_key_version":"5","edit":"true","ig_sig":"0418319e74cfd759b390f6985f3913f27dd40e3cc36ca4e39d9c4e8f4566ff61"}
                headers = {"Accept":"*/*","X-IG-Capabilities":"AQ==","Connection":"close","User-Agent":"Instagram 6.5.1 (iPhone2,1; iPhone OS 6_1_6; en_US; en) AppleWebKit/420+","Accept-Encoding":"gzip, deflate","Accept-Language":"en;q=1, fr;q=0.9, de;q=0.8, ja;q=0.7, nl;q=0.6, it;q=0.5","X-IG-Connection-Type":"WiFi"}
                cookies = {"urlgen":"\"{\\\"1.3.3.7\\\": 7922}:1hNgEb:9CKXMjDWqUyNeomPGlYZ3gj8nao\"","igfl":myDS_USER,"ds_user":myDS_USER,"ds_user_id":myDS_USER_ID,"mid":myMID,"sessionid":mySessionID,"csrftoken":myCSRF,"rur":"VLL","is_starred_enabled":"yes"}
                response = requests.get("https://i.instagram.com/api/v1/accounts/current_user/", params=paramsGet, headers=headers, cookies=cookies)
                if nUsername in response.content.decode('utf-8'):
                    #print('['+Fore.GREEN+'+'+Fore.WHITE+']'+' Successfully Setup Account')
                    mEmail = str(response.json()['user']['email'])
                    mFirstName = str(response.json()['user']['full_name'])
                    #print(response.content)
                    try:
                        paramsPost = {"ig_sig_key_version":"5","signed_body":"66ab4c58537eead820f066daecac18eb319af61529d3da92845e9ed7d811bcd5.{\"gender\":\"3\",\"_csrftoken\":\""+myCSRF+"\",\"_uuid\":\""+myUUID+"\",\"_uid\":\""+myDS_USER_ID+"\",\"external_url\":\"\",\"username\":\""+nUsername+"\",\"email\":\""+mEmail+"\",\"phone_number\":\"\",\"biography\":\""+mBio+"\",\"first_name\":\""+mFirstName+"\"}"}
                        headers = {"Accept":"*/*","X-IG-Capabilities":"36r/Bw==","User-Agent":"Instagram 39.0.0.12.95 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+","Connection":"close","X-IG-ABR-Connection-Speed-KBPS":"0","X-IG-Connection-Speed":"319kbps","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US;q=1","X-IG-Connection-Type":"WiFi","X-IG-App-ID":"124024574287414","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
                        cookies = {"urlgen":"\"{\\\"107.99.45.23\\\": 7922\\054 \\\"2601:2c3:877f:db78:835:4e84:b991:95f6\\\": 7922}:1h4px5:GmcZFuickg3NXINWN7E4OhGsdLc\"","igfl":myDS_USER,"ds_user":myDS_USER,"ds_user_id":myDS_USER_ID,"mid":myMID,"shbts":"1552658440.473448","sessionid":mySessionID,"csrftoken":myCSRF,"shbid":"18080","rur":"ATN","is_starred_enabled":"yes"}
                        response = requests.post("https://i.instagram.com/api/v1/accounts/edit_profile/", data=paramsPost, headers=headers, cookies=cookies)
                        if nUsername in response.content.decode('utf-8'):
                            print('['+Fore.GREEN+'+'+Fore.WHITE+']'+' Successfully Setup: '+nUsername)
                            time.sleep(1)
                            target()
                        elif "Try Again Later" in response.content.decode('utf-8'):
                            print('['+Fore.YELLOW+'!'+Fore.WHITE+']'+' Try Again...')
                            login()
                        else:
                            print(Fore.WHITE+response.content)
                            print('['+Fore.RED+'-'+Fore.WHITE+']'+' Check Your Account')
                            sys.exit()
                    except Exception as a:
                        print(str(a))
                        pass
                else:
                    print('['+Fore.RED+'!'+Fore.WHITE+']'+' Unable To Successfully Setup Account')
            except Exception as p:
                print(p)
                pass
        elif "invalid_credentials" in decoded:
            print('['+Fore.RED+'-'+Fore.WHITE+']'+' Incorrect Login Information, Try Again.')
            time.sleep(1)
            login()
        elif "challenge_required" in r.decoded:
            print('['+Fore.RED+'-'+Fore.WHITE+']'+' Suspicious Login / Login Issue')
            sys.exit()
        else:
            print(Fore.WHITE+'Couldnt Login! Read Log.')
            print(r.content)
            sys.exit()
    except Exception as e:
        print(str(e))
        pass
 
threads = []
def target():
    clear()
    nUser = input(Fore.RED+'Enter Username To Target: '+Fore.GREEN)
    randString()
 
    try:
        eUparamsPost = {"ig_sig_key_version":"5","signed_body":"cf05ca7fc174d94fddaef03a4891990aa35f1b0ffbdee891d4302103e9349114.{\"_uuid\":\""+myUUID+"\",\"_uid\":\""+myDS_USER_ID+"\",\"device_id\":\""+myUUID+"\",\"day\":\"1\",\"month\":\"4\",\"year\":\"1999\",\"current_screen_key\":\"dob\",\"_csrftoken\":\""+myCSRF+"\"}"}
        eUheaders = {"Accept":"*/*","X-IG-Capabilities":"36r/dw==","User-Agent":"Instagram 49.0.0.14.178 (iPhone9,3; iOS 12_0; en_US; en-US; scale=2.00; gamut=wide; 750x1334) AppleWebKit/420+","Connection":"close","X-IG-ABR-Connection-Speed-KBPS":"0","X-IG-Connection-Speed":"268kbps","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US;q=1","X-IG-Connection-Type":"WiFi","X-IG-App-ID":"124024574287414","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        eUcookies = {"ds_user":nUsername,"ds_user_id":myDS_USER_ID,"mid":myMID,"sessionid":mySessionID,"csrftoken":myCSRF,"rur":"FRC"}
        eUresponse = requests.post("https://i.instagram.com/api/v1/consent/existing_user_flow/", data=eUparamsPost, headers=eUheaders, cookies=eUcookies)
        if '"status": "ok"' in eUresponse.content.decode('utf-8'):
            print(Fore.WHITE+'['+Fore.YELLOW+'!'+Fore.WHITE+']'+' Bypassing EU Regulations')
        else:
            print(Fore.WHITE+'['+Fore.YELLOW+'!'+Fore.WHITE+']'+' No EU Forms To Bypass')
    except Exception as eu:
        print(str(eu))
        pass
 
    nWorkers = input(Fore.RED+'Enter Number Of Threads: '+Fore.GREEN)
    for x in range(int(nWorkers)):
        t = threading.Thread(target=swapUser, args=(nUser,))
        threads.append(t)
        t.start()
    for process in threads:
        process.join()
 
def randString():
    global newDS_ID
    newDS_ID = None
    newDS_ID = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
 
myCounter = 0
spamBlockFix = 0
def swapUser(nUser):
    global myCounter, spamBlockFix
    swapStart = True
    while swapStart:
        myCounter += 1
        try:
            paramsPost = {"external_url":"","gender":"3","chaining_enabled":"on","phone_number":"","biography":mBio,"first_name":mFirstName,"email":mEmail,"username":nUser}
            headers = {"Origin":"https://www.instagram.com","Accept":"*/*","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Referer":"https://www.instagram.com/accounts/edit/","Connection":"close","Accept-Encoding":"gzip, deflate","X-CSRFToken":myCSRF,"X-Instagram-AJAX":"b3fa4c74085d","Accept-Language":"en-us","X-IG-App-ID":"1217981644879628","Content-Type":"application/x-www-form-urlencoded"}
            cookies = {"urlgen":"\"{\\\"2607:fb90:b2b:fd01:4d1a:8692:22b:3720\\\": 21928}:1hHFLp:PGeqsPqCCKxeGUzlh5LxiafM6cY\"","ds_user_id":"1"+newDS_ID,"mid":myMID,"sessionid":mySessionID,"csrftoken":myCSRF,"rur":"FRC"}
            response = requests.post("https://www.instagram.com/accounts/edit/", data=paramsPost, headers=headers, cookies=cookies)
            if "Please wait a few minutes before you try again" in response.content.decode('utf-8'):
                randString()
                spamBlockFix += 1
                Msg = '['+Fore.YELLOW+'!'+Fore.WHITE+']'+' Spam Block Hit'
            elif "feedback_required" in response.content.decode('utf-8'):
                sys.exit('['+Fore.RED+'!'+Fore.WHITE+']'+' Bad Freshie! Make A New Account!')
            elif "Oops, an error occurred." in response.content.decode('utf-8'):
                Msg = '['+Fore.YELLOW+'!'+Fore.WHITE+']'+' Yoink\'d That Error'
            elif "This username isn't available. Please try another." in response.content.decode('utf-8'):
                Msg = '['+Fore.RED+'-'+Fore.WHITE+']'+' Username Not Available'
            elif '{"status": "ok"}' in response.content.decode('utf-8'):
                output = open('successfullySwapped.txt', 'a')
                output.writelines(nUser)
                output.close()
                print('\nClaimed: '+nUser+'\n'+'Email: '+mEmail+'\n\n')
                try:
                    headers = {"x-install-id":"aa9fc98d31b47a8c9124cf1ae9c687b3","Accept":"*/*","User-Agent":"TextfreeVoice/2191 CFNetwork/974.2.1 Darwin/18.0.0","Connection":"close","x-udid":"C533DDBE-B55D-41C9-9E93-1786047BFD95,FE4FD084-9DCB-481A-A248-57E0E32E25ED","x-uid":"1105042925","Accept-Encoding":"gzip, deflate","X-Rest-Method":"POST","x-bg":"0","x-os":"ios,12.0","Authorization":"OAuth realm=\"https://api.pinger.com\",oauth_consumer_key=\"1105042925%3Btextfree-voice-iphone-free-8D722AD4-B45D-49E0-89DA-23ED09288004\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1557564906\",oauth_nonce=\"FC1C3CAE-CFC2-435F-9EFB-24A0B4BEF3D1\", oauth_signature=\"3Lr1wwsjRFQZ612UkSfaQmDVmuU%3D\"","x-client":"textfree-voice-iphone-free,11.39.1,2191","Accept-Language":"en-us","x-gid":"73","Content-Type":"application/json"}
                    rawBody = "{\"to\":[{\"TN\":\"1"+nNumber+"\"}],\"text\":\""+"Successfully Claimed: "+nUser+"\"}"
                    r  = requests.post("https://api.pinger.com/2.0/message", data=rawBody, headers=headers)
                except Exception as t:
                    #print(str(t))
                    pass
                sys.exit()
                swapStart = False
            else:
                Msg = 'Something Else'
                #print(response.content)
            print(Fore.WHITE+">> Attempts: "+str(myCounter)+" | "+Msg+" | Response Time: "+str(response.elapsed.total_seconds()), end="\r", flush=True)
        except Exception as e:
            #print(str(e))
            pass
 
if __name__ == '__main__':
    login()