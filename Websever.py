# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
#Fill in start
serverSocket.bind(('',serverPort)) #bind server sock and server port
#Fill in end

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
	#Fill in start
	connectionSocket, addr = serverSocket.accept() #setup connect from the client...
        #Fill in end

	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client
		message = connectionSocket.recv(1024).decode()
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		#Fill in start
		first_l = message.find(' ') #immediately search for space
		second_l = message.find(' ',first_l+1) #searching for next space
		path = message[first_l+1:second_l] #get message from the first char till before 2nd space
                #Fill in end
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		#Fill in start
		name_of_file = path[1:] #assign name of file from first char to last
                #Fill in end
		# Store the entire contenet of the requested file in a temporary buffer
		#Fill in start
		with open(name_of_file) as req_file:
			tempbuff = req_file.read() #storing entire content of requested file in temp buff
                #Fill in end
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		# Send the content of the requested file to the connection socket
		#Fill in start
		connectionSocket.send(tempbuff.encode()) #sending req file to connection socket 
                #Fill in end
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
			# Send HTTP response message for file not found
			#Fill in start 
			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode()) #send the required 404 Not Found msg for file not found
                        #Fill in end
			# Close the client connection socket
			connectionSocket.close()

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
