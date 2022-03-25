import dropbox
import os
from dropbox.files import WriteMode

local_path = input("Enter the path of the file/folder to be uploaded: ")

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        db = dropbox.Dropbox(self.access_token)

        for root, files, dirs in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                print(relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                print(dropbox_path)
        
                with open(local_path, 'rb') as f:
                    db.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

        print("success")

def main():
    access_token = "sl.BEchoZzpzmA4YmI_p8T4lqqqvFZzZKa_grMhgy6gyh8k2GhPekr7JC-iTc7vhG-52k_Y0uo6XGL8quJlcf4laqQI9k63QE9BwkQ_qo9kdzriyNs5VNU1yMwDOc0-qM6fwE6EKCiL"
    data = TransferData(access_token)
    print(data)
    file_from = local_path
    print(file_from)
    file_to = input("Enter the full path to upload the file: ")
    data.upload_file(file_from, file_to)

main()
