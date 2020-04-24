import sys
import os.path
import uuid
from glob import glob
from datetime import datetime


class HttpServer:
    def __init__(self):
        self.sessions = {}
        self.types = {}
        self.types['.pdf'] = 'application/pdf'
        self.types['.jpg'] = 'image/jpeg'
        self.types['.txt'] = 'text/plain'
        self.types['.html'] = 'text/html'

    def response(self, kode=404, message='Not Found', messagebody='', headers={}):
        tanggal = datetime.now().strftime('%c')
        resp = []
        resp.append("HTTP/1.0 {} {}\r\n".format(kode, message))
        resp.append("Date: {}\r\n".format(tanggal))
        resp.append("Connection: close\r\n")
        resp.append("Server: myserver/1.0\r\n")
        resp.append("Content-Length: {}\r\n".format(len(messagebody)))
        for kk in headers:
            resp.append("{}:{}\r\n".format(kk, headers[kk]))
        resp.append("\r\n")
        resp.append("{}".format(messagebody))
        response_str = ''
        for i in resp:
            response_str = "{}{}".format(response_str, i)
        return response_str

    def proses(self, data):
        requests = data.split("\r\n")
        # print(requests)
        baris = requests[0]
        all_headers = [n for n in requests[1:] if n != '']
        j = baris.split(" ")
        try:
            method = j[0].upper().strip()
            # print(method)
            if (method == 'GET'):
                object_address = j[1].strip()
                object_address = object_address.replace('/', '')
                print(object_address)
                return self.http_get(object_address, all_headers)
            if (method == 'POST'):
                temp = requests[18].rsplit("=")
                # print(temp)
                content = temp[1]
                print(content)
                object_address = j[1].strip()
                return self.http_post(object_address, all_headers, content)
            else:
                return self.response(400, 'Bad Request', '', {})
        except IndexError:
            return self.response(400, 'Bad Request', '', {})

    def http_get(self, object_address, headers):
        files = glob('./*')
        thedir = '.\\'
        if thedir + object_address not in files:
            return self.response(404, 'Not Found', '', {})
        fp = open(thedir + object_address, 'r')
        isi = fp.read()
        headers = {}
        headers['Content-type'] = "text/html"
        return self.response(200, 'OK', isi, headers)

    def http_post(self, object_address, headers, content):
        head = headers
        headers = {}
        temp = ""
        for h in head:
            temp = temp + h + "\n"
        isi = content + "\n\n" + temp
        return self.response(200, 'OK', isi, headers)


# >>> import os.path
# >>> ext = os.path.splitext('/ak/52.png')

if __name__ == "__main__":
    httpserver = HttpServer()
    d = httpserver.proses('GET testing.txt HTTP/1.0')
    print(d)















