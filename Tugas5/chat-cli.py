import socket
import os
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 2331


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP, TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid = ""

    def proses(self, cmdline):
        j = cmdline.split(" ")
        try:
            command = j[0].strip()
            if (command == 'auth'):
                username = j[1].strip()
                password = j[2].strip()
                return self.login(username, password)
            elif (command == 'send'):
                usernameto = j[1].strip()
                message = ""
                for w in j[2:]:
                    message = "{} {}".format(message, w)
                return self.sendmessage(usernameto, message)
            elif (command == 'inbox'):
                return self.inbox()
            elif (command == 'online'):
                return self.list()
            elif (command == 'logout'):
                return self.logout()
            else:
                return "Sorry, wrong command"
        except IndexError:
            return "Sorry, wrong command [Index Error]"

    def sendstring(self, string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                #print("Receiving from server", data)
                if (data):
                    receivemsg = "{}{}".format(receivemsg,
                                               data.decode())
                    if receivemsg[-4:] == '\r\n\r\n':
                        #print("end of string")
                        return json.loads(receivemsg)
        except:
            self.sock.close()
            return {'status': 'ERROR', 'message': 'Failed'}

    def login(self, username, password):
        string = "auth {} {} \r\n".format(username, password)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = result['tokenid']
            return "Username: {} logged in, token: {} ".format(username, self.tokenid)
        else:
            return "Error, {}".format(result['message'])

    def sendmessage(self, usernameto="xxx", message="xxx"):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "send {} {} {} \r\n".format(self.tokenid, usernameto, message)
        print(string)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "message sent to {}".format(usernameto)
        else:
            return "Error, {}".format(result['message'])

    def inbox(self):
        if (self.tokenid == ""):
            return "Error, user not authorized"
        string = "inbox {} \r\n".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "{}".format(json.dumps(result['messages']))
        else:
            return "Error, {}".format(result['message'])



    def list(self):
        if (self.tokenid == ""):
            return "Error, not authorized"
        string = "online {} \r\n".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            return "Online User List: {}".format(json.dumps(result['message']))
        else:
            return "Error, {}".format(result['message'])

    def logout(self):
        if (self.tokenid == ""):
            return "Error, user not authorized"
        string = "logout {} \r\n".format(self.tokenid)
        result = self.sendstring(string)
        if result['status'] == 'OK':
            self.tokenid = ""
            return "You've been logged out!"
        else:
            return "Error, {}".format(result['message'])


if __name__ == "__main__":
    cc = ChatClient()
    while True:
        cmdline = input("Command {}:".format(cc.tokenid))
        print(cc.proses(cmdline))

