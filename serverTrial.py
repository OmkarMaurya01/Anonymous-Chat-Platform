            
# from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from pyngrok import ngrok
from time import sleep
import pyautogui
import threading
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from shortLink import ShortLink
import qrcode
from PIL import Image


print("-----------------------DarkRoom Server ----------------------")

# gmail = 'rudra8732@gmail.com'
gmail = 'study8732@gmail.com'
port = '8080'
protocol = 'http'
hostName = "localhost"
serverPort = 8080
HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8080 


http_tunnel = ngrok.connect(port, protocol)
# print(http_tunnel)
longLink = str(http_tunnel).split('"')[1]

# subDomain = input("Create Domain [https://www.<youdomain>.com]: ")

# Shorting of link here

# while True:
#     subDomain = str(input('Enter the SubDomain [min 6 letter]:'))
#     if len(subDomain)<6:
#         print('Your SubDomain should contain 6 or more characters ')
#         continue
#     break

# while True:
#     try: 
#         repeat,status,freshLink = ShortLink(subDomain ,longLink, gmail)
#     except Exception as e: 
#         freshLink = longLink
#         status = "Error in ShortLink"
#         print(f"Status: {status}")
#         print('nope')
#         print(e)
#         break
#     print(f"Status: {status}")

#     if not repeat: 
#         print('Link Compression process...Done')    
#         break
#     while True:
#         subDomain = str(input('Enter the New SubDomain [min 6 letter]:'))
#         if len(subDomain)<6:
#             print('Your SubDomain should contain 6 or more characters ')
#             continue
#         break
# longLink = "http://localhost:8080/"
import re
while True:
    Key = input("Create Authorized Key:  ")
    pattern = re.compile('^[0-9]+$')
    # pattern.search(string)
    pattern = pattern.search(Key)
    if pattern is not None : break
    print("Key should be Numerical")
# print(pattern.search('794abc'))

freshLink = longLink #Temporary 
subDomain = 'Metting'

print(f'WebInterface [url]: {freshLink}')
print(f'Port: {port}')
print(f"protocol: {protocol}")

# --------QR Code Section --------
data = freshLink
img = qrcode.make(data)
img.save('EncryptedQR.png')
img.show()

# print('Encrypting URL....Done')
# --------QR Code Section Complete--------

# --------Server Code Section --------

print("-----------------Server Started-----------------")




MessageContainer = []



    
def PostResponseMaker(response):
    # Process the request and prepare a response
    response_body = response
    response_headers = {
        'Content-Type':"application/json" ,
        'Content-Length': str(len(response_body))
    }
    status = '200 OK'
    response = 'HTTP/1.1 {status}\r\n'.format(status=status)
    for header in response_headers:
        response += '{0}: {1}\r\n'.format(header, response_headers[header])
    response += '\r\n' + response_body

    return response

def fetchResponse(message ,header = False):
    import json
    response_data = message
    
    response_headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    }
    if  header:
        for h in header.split(","):response_headers[h.split(":")[0]] = h.split(":")[-1]

    response = 'HTTP/1.1 200 OK\r\n'
    response += ''.join(f'{k}: {v}\r\n' for k, v in response_headers.items())
    response += '\r\n'
    response += json.dumps(response_data)

    return response

# --------------------------------------------------------------------------------------
#                                    start
# --------------------------------------------------------------------------------------

AuthorizedUserAgent = []
MessageEnquiry = []
Msg = []
TMsg = []

htmlCode = open('chat.html','r').read()
# htmlCode = htmlCode.replace("replace_Link_Here", freshLink.replace("http",'https'))
htmlCode = htmlCode.replace("replace_Link_Here", longLink.replace("http",'https'))
htmlCode = htmlCode.replace("replace_Key_here", Key)
htmlCode = htmlCode.replace("replace_Host_here", subDomain)
# print(htmlCode)
# print(htmlCode)
# quit()

def Authentication(client_socket, requestDict):
    userAgent = requestDict['User-Agent']
    if userAgent in AuthorizedUserAgent:
        print(f" the user {userAgent} is authorized person ")
        return True

    if "Passward" in list(requestDict.values())[-1]:
        passward = list(requestDict.values())[-1].split('@layer')[-2].strip()
        if passward == Key.strip():
            AuthorizedUserAgent.append(userAgent)
            response = fetchResponse('Key Matched')
            response = bytes(response ,'utf-8')
            client_socket.sendall(response)
            client_socket.close()

            return True
        response = fetchResponse('Wrong Key')
        response = bytes(response ,'utf-8')
        client_socket.sendall(response)
        client_socket.close()
    
    if 'images.jpeg' in list(requestDict.values())[0]:
        print(f" images.jpeg requested")
        with open('images.jpeg', 'rb') as f:
                file_data = f.read()

                # create an HTTP response header
                http_response = b"HTTP/1.1 200 OK\r\n"
                http_response += b"content-type: image/jpeg\r\n"
                # http_response += f"Content-Length: {len(file_data)}\r\n"
                http_response += b"\r\n"

                # send the HTTP response header
                client_socket.sendall(http_response)

                # send the media file data
                client_socket.sendall(file_data)

                # close the connection
                client_socket.close()
                return True
   
    htmlCode = open('authentication.html','r').read()
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
    response = bytes(response ,'utf-8')
    client_socket.sendall(response)
    client_socket.close()
        






def handle_request(client_socket):
     
    
    request = client_socket.recv(1024).decode('utf-8')
    # request = client_socket.recv(1024).decode('iso-8859-1')
    print(request)
    requestDict = dict() 
    for i in request.split('\n'):
        key , value = i.split(':')[0].strip(),i.split(':')[-1].strip()
        requestDict[key] = value 
    
    Authentication(client_socket, requestDict)
    # UserAgent = requestDict['User-Agent']
    # AuthorizedUserAgent[UserAgent] = client_socket 

    if 'MessageEnquiry' in request.split('\n')[-1]:

        query = request.split('\n')[-1]

        clientMsg = int(query.split(' ')[-1])
        serverMsg = int(len(Msg))
        # print(f"clientMsg: {clientMsg}")
        # print(f"serverMsg: {serverMsg}")
        msg = str()
        # if clientMsg<serverMsg:
            # msg = Msg[clientMsg:]
        userclient = requestDict['User-Agent']
        for record in TMsg:
            userAgent = record['userAgent'] 
            msg_ = record['msg']
            fulluseragent = record['fulluserAgent'].strip()
            print(userclient)
            print(fulluseragent)
            if fulluseragent == userclient:userAgent = 'You'
            text = f'{userAgent} --> {msg_}'
            msg = msg + text + ",,,"

        clientNumber = int(requestDict['Clientnumber']) 
        if clientNumber<len(AuthorizedUserAgent):
            authorPer = ',,,'.join(AuthorizedUserAgent)
            msg = msg + f"[[[{authorPer}]]]"

        
        response = fetchResponse(msg , f'client:{len(AuthorizedUserAgent)}')

        # print(response)
        response = bytes(response ,'utf-8')
        client_socket.sendall(response)
        client_socket.close()

       
    if 'POST Message' in request.split('\n')[-1]:
        query = request.split('\n')[-1].split('@layer')[-2].strip()
        userclient = requestDict['User-Agent']
        # print(userclient)
        # print(query)
        tempDict = dict()
        tempDict['fulluserAgent'] = userclient
        pre = userclient.index('(')
        pos = userclient.index(')',pre+1)
        userclient = userclient[pre+1:pos] 
        tempDict['userAgent'] = userclient
        tempDict['msg'] = query
        TMsg.append(tempDict)

        Msg.append(query)

        response = fetchResponse("Done Updating Message")
        response = bytes(response ,'utf-8')
        client_socket.sendall(response)
        client_socket.close()
    
    # print(request.split('\n')[0])
    if 'man.png' in request.split('\n')[0]:
        print("Man Got")
        with open('man.png', 'rb') as f:
                file_data = f.read()

                # create an HTTP response header
                http_response = b"HTTP/1.1 200 OK\r\n"
                http_response += b"content-type: image/png\r\n"
                # http_response += f"Content-Length: {len(file_data)}\r\n"
                http_response += b"\r\n"

                # send the HTTP response header
                client_socket.sendall(http_response)

                # send the media file data
                client_socket.sendall(file_data)

                # close the connection
                client_socket.close()
                

    
    try:
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
        response = bytes(response ,'utf-8')
        client_socket.sendall(response)
        client_socket.close()
    except:pass
       
    

    



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while True:
       
        client_socket, address = server_socket.accept()
        
        client_thread = threading.Thread(target= handle_request , args=(client_socket,))
        client_thread.start()
        
        
       
        # print(MessageContainer)
         
      
