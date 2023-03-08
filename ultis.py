import requests
import pymongo
import certifi
client = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
database = client['nft']
collection = database['etherscan']
from fake_useragent import UserAgent

# Tạo đối tượng UserAgent
ua = UserAgent()

def getMetadata(transaction):
    url = 'https://api.opensea.io/asset/'+transaction['address']+'/'+str(int(transaction['topics'][3],16))+'?format=json'
    res = requests.get(url,headers={'User-Agent': ua.random})
    if res.status_code == 200:
        result = res.json()
        asset = {
            'contract': transaction['address'],
            'blockNumber': str(int(transaction['blockNumber'],16)),
            'transactionHash': transaction['transactionHash'],
            'tokenId': str(int(transaction['topics'][3],16)),
            'authorAddress': result['creator']['address'],
            'uri': result['token_metadata'],
            'name': result['name'],
            'description': result['description'],
            'image': result['image_original_url'],
            'tags': [doc.get("value") for doc in result['traits'] if doc.get("trait_type") == "tag"],
            'market': "https://opensea.io/assets/"+transaction['address']+"/"+str(int(transaction['topics'][3],16)),
            'network': 'ethereum'
        }
        collection.insert_one(asset)
    

    