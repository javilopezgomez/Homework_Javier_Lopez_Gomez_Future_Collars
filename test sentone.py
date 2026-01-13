import re
import requests
from urllib.parse import urlparse
import csv

urls = [
    "https://accounts.google.com/login",
    "https://drive.google.com/file/d/1A2B3C4D5E/view",
    "https://www.dropbox.com/s/abc123xyz/shared_document.pdf",
    "https://example-bank.com/account/login",
    "https://mycompany.internal/upload",
    "https://randomfileshare.xyz/upload.php?file=test.txt",
    "https://api.myservice.com/v1/users?email=john.doe@example.com",
    "https://github.com/user/repo/settings/secrets",
    "https://pastebin.com/raw/AbCdEfGh",
    "https://cdn.example.com/public/assets/logo.png"
]

LOGIN_REGEX = r"/login"
UPLOAD_REGEX = r"/upload"
API_REGEX = r"/api/|/v\d+/"
FILE_REGEX = r"\.(pdf|png|txt)$"
SECRETS_REGEX = r"/secrets"

results = []

for url in urls:
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path.lower()

    classification = "UNKNOWN"
    confidence = "LOW"

    if re.search(SECRETS_REGEX, path):
        classification = "CREDENTIALS"
        confidence = "HIGH"
    elif re.search(LOGIN_REGEX, path):
        classification = "AUTH"
        confidence = "HIGH"
    elif re.search(UPLOAD_REGEX, path):
        classification = "FILE_UPLOAD"
        confidence = "MEDIUM"
    elif re.search(API_REGEX, path):
        classification = "API"
        confidence = "MEDIUM"
    elif re.search(FILE_REGEX, path):
        classification = "PUBLIC_FILE"
        confidence = "LOW"

    try:
        response = requests.head(url, timeout=5)
        status = response.status_code
    except:
        status = "ERROR"

    results.append([
        url,
        domain,
        path,
        classification,
        confidence,
        status
    ])

    print(url, classification, confidence, status)

print(results)

with open('results.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["url", "domain", "path", "classification", "confidence", "status"])
    writer.writerows(results)