from dotenv import load_dotenv
import os
load_dotenv()
import time
import requests
import json

# Replace with your own API key
API_KEY_ETHERSCAN = os.getenv('API_KEY_ETHERSCAN')


step_block = 1
start_block = 1
urlAPI = 'https://api.etherscan.io/api'

for i in range(50):

    params = {
                    "module" : "logs",
                    "action" : "getLogs",
                    "fromBlock" : start_block,
                    "toBlock" :start_block + step_block,
                    "topic0" : "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "topic0_1_opr" : "and",
                    "topic1" : "0x0000000000000000000000000000000000000000000000000000000000000000",
                    "page" : 1,
                    "offset" : 10000,
                    "apikey" : API_KEY_ETHERSCAN
            }

    result = requests.get(url=urlAPI,params=params).json()
    if result['status'] == '0':
        start_block += step_block
        step_block *= 2
        transaction_number = 0
        transaction_ERC_721 = []
    else:
        transaction_number = len(result['result'])
        if transaction_number < 10000 and transaction_number > 4000:
            start_block += step_block

            
        if transaction_number <= 4000:
            start_block += step_block
            step_block *= 2

        if transaction_number == 10000:
            step_block = int(step_block/2)

        

        transaction_ERC_721 = []
        for obj in result['result']:
            if len(obj['topics']) != 4:
                continue
            transaction_ERC_721.append(obj)

    print('-------------------------------------')
    print('Block: '+str(start_block)+' to '+str(start_block+step_block)+'\nSố lượng transaction: '+str(transaction_number))
    print('Step block: '+str(step_block))
    print('Số lượng transaction ERC-721: '+str(len(transaction_ERC_721)))
    print('-------------------------------------\n')