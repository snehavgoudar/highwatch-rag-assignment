# simple mock version for assignment demo
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import io
import os

DOWNLOAD_DIR = "temp_pdfs"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_file(file_id, file_name):
    os.makedirs("temp_pdfs", exist_ok=True)

    request = service.files().get_media(fileId=file_id)

    file_path = f"temp_pdfs/{file_name}"

    fh = io.FileIO(file_path, "wb")

    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()

    return file_path

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

service = build("drive", "v3", credentials=creds)

def list_files():
    results = service.files().list(
        pageSize=10,
        fields="files(id,name)"
    ).execute()

    return results.get("files", [])
# def download_file(file_id):
#     return "temp.pdfs"