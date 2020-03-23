import shelve
import uuid
import socket
import os
import base64


class FolderFile:
    def __init__(self):
        if not os.path.exists('folderfile'):
            os.makedirs('folderfile')

    def upload_data(self, nama=None, file=None):
        unggah = file
        f = open('folderfile/' + nama, 'wb')
        f.write(base64.decodestring(unggah))
        return True

    def download_data(self, nama=None):
        array = []
        print('masuk fungsi download')
        f = open('folderfile/'+nama,'rb')
        l = f.read()
        print(l)
        f.close()
        hasil = base64.encodebytes(l)
        print(hasil)
        array.append(hasil.decode())
        return array

    def  list_data(self):
        lists = os.listdir('folderfile')
        f = []
        for filename in lists:
            f.append(filename)
        return f

if __name__=='__main__':
    cb = FolderFile()
    input = 'input.txt'
    print(cb.list_data())