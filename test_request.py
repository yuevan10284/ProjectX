import requests

# URL and headers as specified
url = "https://sbapi.ma.sportsbook.fanduel.com/api/content-managed-page?page=CUSTOM&customPageId=mlb&pbHorizontal=false&_ak=FhMFpcPWXMeyZxOx&timezone=America%2FNew_York"

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://sportsbook.fanduel.com",
    "Priority": "u=1, i",
    "Referer": "https://sportsbook.fanduel.com/",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"macOS"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}

# Make the GET request
response = requests.get(url, headers=headers)

# Print the status code and pipe response text to a file
with open("response.txt", "w") as file:
    file.write(f"Status Code: {response.status_code}\n")
    file.write("Response Text:\n")
    file.write(response.text)
