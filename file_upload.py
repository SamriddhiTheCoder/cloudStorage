import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BEf5oeLL4PKJD93lfAYN72-iLdmfXBgVVzwpGcI4RORCz5jIQ5Ziyuqyjeze559TItWg95Uig112uqBw2-aZP-jzJO8CNVy85k-efSBiXithc78-OJ8n5sigSBAyj3mq3hZs3Ey1"
    data = TransferData(access_token)
    file_from = input("Enter file path to be uploaded: ")
    file_to = input("Enter file to upload: ")
    data.uploadFile(file_from, file_to)

main()
