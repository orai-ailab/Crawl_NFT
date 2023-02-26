from dotenv import load_dotenv
import os
load_dotenv()
import time
import requests
import json
import logging
logging.basicConfig(filename='info.log',filemode='w',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

API_KEY_ETHERSCAN = os.getenv('API_KEY_ETHERSCAN')

def call_requests_api_etherscan(start_block,end_block):

    urlAPI = 'https://api.etherscan.io/api'
    params = {
                    "module" : "logs",
                    "action" : "getLogs",
                    "fromBlock" : start_block,
                    "toBlock" :end_block,
                    "topic0" : "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                    "topic0_1_opr" : "and",
                    "topic1" : "0x0000000000000000000000000000000000000000000000000000000000000000",
                    "page" : 1,
                    "offset" : 10000,
                    "apikey" : API_KEY_ETHERSCAN
            }
    result = requests.get(url=urlAPI,params=params).json()
    
    
    if result['status'] == '0':
        transaction_number = []
        transaction_ERC_721 = []
    else:
        # Total transaction
        transaction_number = result['result']
        # Filter transaction ERC 721
        transaction_ERC_721 = []
        for obj in result['result']:
            if len(obj['topics']) != 4:
                continue
            transaction_ERC_721.append(obj)
    
    logging.info('Block: '+str(start_block)+' To '+str(end_block) + ', Step block: '+str(end_block-start_block)+ ', Total transaction: '+str(len(transaction_number))+', Transaction ERC-721: '+str(len(transaction_ERC_721)))
    
    
    
    
    
    
    
    
    return result

def main():
    start_block = 1
    step_block = 1

    result = call_requests_api_etherscan(start_block=start_block,end_block=start_block+step_block)
    for i in range(50):
        if result['status'] == '0':
            transaction_number = []
            transaction_ERC_721 = []
            start_block += step_block
            step_block *=2
            result = call_requests_api_etherscan(start_block=start_block,end_block=start_block+step_block)
            continue
        else:
            # Total transaction
            transaction_number = len(result['result'])
            
            
            # Filter transaction ERC 721
            transaction_ERC_721 = []
            for obj in result['result']:
                if len(obj['topics']) != 4:
                    continue
                transaction_ERC_721.append(obj)
                
            
            if transaction_number <= 4000:
                
                start_block = start_block + step_block
                step_block *= 2
                result = call_requests_api_etherscan(start_block=start_block,end_block=start_block+step_block)
                continue

            if transaction_number == 10000:

                step_block = int(step_block/2)
                result = call_requests_api_etherscan(start_block=start_block,end_block=start_block+step_block)
                continue
                
            else:

                start_block += step_block
                result = call_requests_api_etherscan(start_block=start_block,end_block=start_block+step_block)
                continue
                
            

            

main()

    