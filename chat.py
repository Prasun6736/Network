##client side####
import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket() #create client side socket

s.connect((server_ip,server_port))

data_to_server = input('Operation number1 number2: ')  #enter client's message to server


while data_to_server != 'exit': #keep on sending data to server until 'exit' is entered
    s.send(data_to_server.encode()) #send byte data to server

    data_from_server = s.recv(1024) #receive data from server
    print(data_to_server.split()[0]+' is ' + str(data_from_server.decode())) #display server's message in string format

    data_to_server = input('Operation number1 number2: ') #enter data to be sent to server

s.close() #close connection
    


#------------------------server side##

import socket

def addition(a,b):
    return str(a+b)

def subtraction(a,b):
    return str(a-b)

def multiplication(a,b):
    return str(a*b)

def division(a,b):
    return str(a/b)

host = '127.0.0.1'
port = 8002

s = socket.socket() #create server side socket

s.bind((host,port)) #binding the socket to host and port

s.listen(1) # max num of connections allowed

c, addr = s.accept() #wait till a client connects

print('A client connected')

#server runs continuously until all data is received from client
while True:
    data_received = c.recv(1024) #receive byte data from client

    if not data_received: #if client sends empty string, stop
        break
    
    print('Data from client: ' + str(data_received.decode())) #display clients raw/byte message as string
    data = data_received.decode().split()
    n1, n2 = map(int, data[1:])
    data_to_send = ''
    if data[0] == 'addition':
        data_to_send = addition(n1,n2) #server's message to client
    elif data[0] == 'subtraction':
        data_to_send = subtraction(n1,n2)
    elif data[0] == 'multiplication':
        data_to_send = multiplication(n1,n2)
    elif data[0] == 'division':
        data_to_send = division(n1,n2)

    c.send(data_to_send.encode()) #send the data to client in byte format
c.close() #close connection


##udp_client---------------------##
import socket

server_name = 'localhost'
server_port = 6889

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_name, server_port))

msg, addr = s.recvfrom(1024)
#s.settimeout(5)

while msg:
    
    print("Received: "+ msg.decode())
    msg, addr = s.recvfrom(1024)


s.close()


###udp_server_________--------##

import socket
import time

own_name = 'localhost'
own_port = 6889

#creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#waiting time of the server
time.sleep(5)

s.sendto(b"Hello class!! Welcome to your lab class", (own_name, own_port))
msg = "Goodbye!!"
s.sendto(msg.encode(), (own_name, own_port))
s.close()


##file client----######

import socket

server_name = 'localhost'
server_port = 8000

s = socket.socket() #create TCP socket

s.connect((server_name,server_port)) #connect to server

filename = input('Enter filename: ') #provide the filename

#filename = 'test_md.txt'

s.send(filename.encode()) #send the filename to the server

content = s.recv(1024) #receive file content from server

print(content.decode()) #print the content in string format

s.close() #close the connection


##file server----##

import socket

host = 'localhost'
port = 8000

s = socket.socket() #create a TCP socket

s.bind((host,port)) #bind socket to host and port num

s.listen(1) #max 1 connection will be accepted

c, addr = s.accept() #wait till client connects
print('A client requested a connection')

fname = c.recv(1024) #accept file name from client

fname = str(fname.decode()) #decode filename to string format

print('Filename received from client: '+fname) 

try:
    f = open(fname, 'rb') #open the file at server side
    content = f.read() #read content of the file
    c.send(content) #send the content of the file, no need to use encode() as by default the content is read as byte
    f.close() #close the file
except FileNotFoundError:
    c.send(b'File does not exist')

c.close() #disconnect the server


###-------------demo udp client###

#UDP client that receives messages from server

import socket

server_name = 'localhost'
server_port = 8001

#create a client side UDP socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#s.bind((server_name,server_port)) #connect to server with server_name and server port

serverAddrPort = ("127.0.0.1", 8001)

data_to_send = input("Data to server:")
while data_to_send!='exit':
    s.sendto(data_to_send.encode(), serverAddrPort)

    data_from_server = s.recvfrom(1024)
    msg = "Message from Server {}".format(data_from_server[0].decode())  
    print(msg)
    #print('server says: '+str(data_from_server.decode()))
    data_to_send = input("Data to server:")

s.close() #close the connection


##-------------demo_udp server###

import socket
import time

client_name = 'localhost'
client_port = 8001


#create a UDP socket at server side 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((client_name, client_port))
#time.sleep(2) #let the server wait for 2 seconds 

#data_receive, addr = s.recvfrom(msg,(client_name,client_port))  #specifying client address as UDP is connectionless protocol, server does not know where to send the packet

while True:
    name, addr1 = s.recvfrom(1024)
    print('Message from client: ' +str(name.decode()))
    data_send = input("Message to client:")
    s.sendto(data_send.encode(), addr1)

s.close() #close the connection


