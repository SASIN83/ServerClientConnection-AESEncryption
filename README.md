# ServerClientConnection-AESEncryption

Part A (TCP Client-Server)
1) Check if the first part of the received string is present in the server collection. -Passed
2) If yes, then retrieve the subset for the corresponding string and check if the second part of the received string is present in the retrieved subset. If yes, then the final VALUE retrieved, will be number of times the server has to send the response to client. The server will then send current time of the system at 1 second interval 'n' number of times. (Where 'n' is the VALUE retrieved) - Passed
3) If not, then sever will send "EMPTY" message to client. - Passed
4) The client will display the received string. - Passed

Part B(Encryption)
The second part the assignment is to Encrypt and Decrypt every message transferred between Client and the Server i.e., the client should encrypt the message before sending to the server and decrypt the messages received from the server. Likewise, the server should be able to do the same. - Passed

Notes
1. It is preferred that the server should be able to handle multiple client connections without breaking any current connection. - Passed
2. Use any type of Encryption/Decryption method. - Passed
3. All the inputs should be user configurable. - Done
