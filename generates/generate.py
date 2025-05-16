import requests

def main():
    url = "https://leetcode.com/api/problems/all/"
    res = requests.get(url)
    print(res.json())

main()