# from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from pyngrok import ngrok
from time import sleep
import pyautogui
import threading
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from shortLink import ShortLink
import qrcode
from PIL import Image

print("-----------------------DarkRoom Server ----------------------")

gmail = 'rudra8732@gmail.com'
port = '8080'
protocol = 'http'

http_tunnel = ngrok.connect(port, protocol)
longLink = str(http_tunnel).split('"')[1]

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
#         print(nope)
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

freshLink = longLink #Temporary 

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
hostName = "localhost"
serverPort = 8080
print("-----------------Server Started-----------------")






# class MyServer(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         file_ = open('index.html')
#         htmlCode = file_.read()
#         self.wfile.write(bytes(f"{htmlCode}", "utf-8"))
        

# if __name__ == "__main__":        
#     webServer = HTTPServer((hostName, serverPort), MyServer)
#     print("Server started http://%s:%s" % (hostName, serverPort))

#     try:
#         webServer.serve_forever()
#     except KeyboardInterrupt:
#         pass

#     webServer.server_close()
#     print("Server stopped.")

# --------Server Code Section Complete --------


# import socket

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8080  # Arbitrary non-privileged port

User = {}
AuthenticUser= []
AuthenticSocket = []
UnAuthenticUser = []
client_sockets = []
# AuthenticHtmlCode = open('authentication.html','r').read()
# index = open('index.html','r').read()


MessageContainer = {}
    
def Authentication(clientData):
    passward = "87328732"
    return clientData==passward

def checkUserAuthenticity(UserAgent):
    return UserAgent in AuthenticUser



 # --------------------trial --------------------
    
def PostResponseMaker(response):
    # Process the request and prepare a response
    response_body = response
    response_headers = {
        'Content-Type': 'text/plain',
        'Content-Length': str(len(response_body))
    }
    status = '200 OK'
    response = 'HTTP/1.1 {status}\r\n'.format(status=status)
    for header in response_headers:
        response += '{0}: {1}\r\n'.format(header, response_headers[header])
    response += '\r\n' + response_body

    return response
 # --------------------trial Complete--------------------

def handle_reque(request):
   
    userAgent = request.split('\n')[2].split(":")[-1]
    lst = request.split('\n')
    httpMethod = lst[0][:lst[0].index('/')]
    query = lst[0][lst[0].index('/'):]
    
    htmlCode = index
    if not checkUserAuthenticity(userAgent): htmlCode = AuthenticHtmlCode
   
    if 'GET' in httpMethod and 'Authentication' in query:
        
        clientData = query[query.index("=")+1:query.index(" ")]
        htmlCode = htmlCode + "<h2>Wrong Passward</h2>"
        if  Authentication(clientData):
            AuthenticUser.append(userAgent)
            # AuthenticSocket.append(client_socket)
            htmlCode = index

        
    
    if 'POST' in httpMethod and 'Message' in query:
        Message = lst[-1]
        MessageContainer[len(MessageContainer)] = [Message.replace("+"," "),userAgent]
        print(f"Message is: {Message}")
        print(User)
        print("\n")
        for user in AuthenticUser :
            client = User[user]
            print(client)
            response = PostResponseMaker(Message)
            client.send(response.encode())

      
    # if 'GET' in httpMethod and 'MessageRequest' in query:

    #     msg = ''
    #     for i in MessageContainer:
    #         raw =f"{MessageContainer[i][-1]}-->{MessageContainer[i][0]}"
    #         msg = msg + raw + '\n'
    #     users = "\n".join(AuthenticUser)

    #     data = msg + '///' + users

    #     response = PostResponseMaker(data, request)
    #     response = bytes(response ,'utf-8')
    #     client_socket.sendall(response)




    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
    response = bytes(response ,'utf-8')
    client_socket.sendall(response)

    # client_socket.close()




# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#             server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#             server_socket.bind((HOST, PORT))
#             server_socket.listen(5)

#             print(f'Starting server on port {PORT}')

#             while True:
#                 client_socket, client_address = server_socket.accept()
#                 handle_request(client_socket)
   


#   list of connected client sockets

MessageContainer = []


def handle_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    requestDict = dict() 
    for i in request.split('\n'):
        key , value = i.split(':')[0].strip(),i.split(':')[-1].strip()
        requestDict[key] = value 
    

    
    # User[requestDict['userAgent']] = client_socket
        
    lst = request.split('\n')
    httpMethod = lst[0][:lst[0].index('/')].strip()
    query = lst[0]
    
    # print(lst)
    # print("-----"+httpMethod+"--------")
    # print("----"+query+"--------")
    # print(request)
    # print("\n")

    if httpMethod == 'GET' and 'MessageQuery' in query:
            ClientAvaialbleMessage = int(requestDict["Client-Avaialble-Message"])
            ServerAvaialbleMessage = len(MessageContainer)
           
            NeedMessage = int(ServerAvaialbleMessage) - int(ClientAvaialbleMessage)
            msg = ''
            # print("\n")
            # print(ClientAvaialbleMessage)
            # print(ServerAvaialbleMessage)
            if NeedMessage>0:
                msg_ = MessageContainer[ClientAvaialbleMessage-1:]
                i = msg_[-1]
                msg =f"{i['userAgent']}-->{i['msg']}"

            

            response = PostResponseMaker(msg)
            client_socket.sendall(response.encode())
            # client_socket.close()
            # return 'MessageQuery'

            
    # print(httpMethod)
    if httpMethod == 'POST' and 'MessageResponse' in query:
            msg = lst[-1].replace("+", " ")
            tempDict = dict()
            tempDict['userAgent'] = requestDict["User-Agent"]
            tempDict['msg'] = msg.strip()
            MessageContainer.append(tempDict)
            # client_socket.close()
            # return 'MessageResponse'

            
    else:
        try:
            htmlCode = open('chat.html','r').read()
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
            client_socket.sendall(response.encode())
        except:pass

    client_socket.close()
    
            

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    while True:
       
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_request, args=(client_socket,))
        client_thread.start()


        # handle_request(request)

        
        # if not checkUserAuthenticity(userAgent): 
        #     htmlCode = AuthenticHtmlCode
        #     response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
        #     response = bytes(response ,'utf-8')
        #     client_socket.sendall(response)

        # if 'GET' in httpMethod and 'Authentication' in query:
        #     clientData = query[query.index("=")+1:query.index(" ")]
        #     htmlCode = htmlCode + "<h2>Wrong Passward</h2>"
        #     if  Authentication(clientData):
        #         AuthenticUser.append(userAgent)
        #         # AuthenticSocket.append(client_socket)
        #         htmlCode = index
        #         response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{htmlCode}"
        #         response = bytes(response ,'utf-8')
        #         client_socket.sendall(response)

        # if 'POST' in httpMethod and 'Message' in query:
        #     Message = lst[-1]
        #     MessageContainer[len(MessageContainer)] = [Message.replace("+"," "),userAgent]
        #     print(f"Message is: {Message}")
        #     print(User)
        #     for user in AuthenticUser :
        #         client = User[user]
        #         print(client)
        #         response = PostResponseMaker(Message)
        #         client.send(response.encode())





#         handle_request(request)
        # client_sockets.append(client_socket)
        # client = client_sockets[-1]
        # print("---------------------")
        # for c in  client_sockets:
        #     print(c)
        # print("---------------------")
        # print(client)
        # print("\n\n")
        # response = PostResponseMaker('reply')
        # client.send(response.encode())
        # print(client)



        # message = 'Hello, world!'
        # for client in client_sockets:
        #     response = PostResponseMaker(message, client)
        #     client.send(message.encode())
