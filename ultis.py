import requests
import pymongo
import certifi
client = pymongo.MongoClient("mongodb+srv://hoangks5:YrfvDz4Mt8xrrHxi@cluster0.tcbxc.mongodb.net/",tlsCAFile=certifi.where())
database = client['nft']
collection = database['etherscan']

def getMetadata(contract_address,token_id,transactionHash,blockNumber,netwwork):
    url = 'https://api.opensea.io/asset/'+contract_address+'/'+str(token_id)+'?format=json'
    res = requests.get(url)
    if res.status_code == 200:
        result = res.json()
        asset = {
            'contract': contract_address,
            'blockNumber': blockNumber,
            'transactionHash': transactionHash,
            'tokenId': token_id,
            'authorAddress': result['creator']['address'],
            'uri': result['token_metadata'],
            'name': result['name'],
            'description': result['description'],
            'image': result['image_original_url'],
            'tags': [doc.get("value") for doc in result['traits'] if doc.get("trait_type") == "tag"],
            'market': "https://opensea.io/assets/"+contract_address+"/"+str(token_id),
            'network': netwwork
        }
        collection.insert_one(asset)
    

    