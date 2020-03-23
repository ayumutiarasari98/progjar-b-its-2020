import json
import logging
import base64
from file import FolderFile

ts = FolderFile()


class Protocol:
    def process(self, string_to_process):
        s = string_to_process
        cstrings = s.split(' ')
        try:
            command = cstrings[0].strip()
            if command == 'upload':
                logging.warning('upload')
                name = cstrings[1].strip()
                file = cstrings[2].strip()
                ts.upload_data(name, file.encode())
                return 'OK'
            elif command == 'download':
                logging.warning('download')
                name = cstrings[1].strip()
                result = ts.download_data(name)
                return result[0]
            elif command == 'list':
                logging.warning('list')
                result = ts.list_data()
                return json.dumps(result)
            else:
                return 'ERROR CMD'
        except:
            return 'ERROR'


if __name__ == '__main__':
    pm = Protocol()
