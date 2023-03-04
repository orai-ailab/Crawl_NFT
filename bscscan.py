from dotenv import load_dotenv
import os
load_dotenv()
import time
import requests
import json
import logging
import certifi
import threading
import pymongo

# Cấu hình logging cho ứng dụng của bạn
logging.basicConfig(filename='info_bscscan.log', level=logging.INFO,format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')



API_KEY_BSCSCAN = os.getenv('API_KEY_BSCSCAN')









def main():
    start_block = 1
    step_block = 1
    total_transaction = 0
    total_transaction_erc_721 = 0
    while True:
        urlAPI = 'https://api.bscscan.com/api'
        params = {
                        "module" : "logs",
                        "action" : "getLogs",
                        "fromBlock" : start_block,
                        "toBlock" :start_block+step_block,
                        "topic0" : "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
                        "topic0_1_opr" : "and",
                        "topic1" : "0x0000000000000000000000000000000000000000000000000000000000000000",
                        "page" : 1,
                        "offset" : 10000,
                        "apikey" : API_KEY_BSCSCAN
                }
        result = requests.get(url=urlAPI,params=params).json()


        if result['status'] == '0':
            transaction_number = []
            transaction_ERC_721 = []
            logging.info('Block: '+str(start_block)+' To '+str(start_block+step_block) + ', Step block: '+str(step_block)+ ', Total transaction: '+str(len(transaction_number))+', Transaction ERC-721: '+str(len(transaction_ERC_721)))
            start_block += step_block
            step_block *=2
            
        else:
            # Total transaction
            transaction_number = result['result']
            # Filter transaction ERC 721
            if len(transaction_number) <= 4000:
                transaction_ERC_721 = []
                for obj in result['result']:
                    if len(obj['topics']) != 4:
                        continue
                    transaction_ERC_721.append(obj)
                   
                total_transaction += len(transaction_number)
                total_transaction_erc_721 += len(transaction_ERC_721)
                logging.info('Block: '+str(start_block)+' To '+str(start_block+step_block) + ', Step block: '+str(step_block)+ ', Total transaction: '+str(len(transaction_number))+', Transaction ERC-721: '+str(len(transaction_ERC_721))+', Crawled Transaction: '+str(total_transaction)+', Crawled Transaction ERC 721: '+str(total_transaction_erc_721))
                start_block = start_block + step_block
                step_block *= 2
                
                

            if len(transaction_number) == 10000:
                step_block = int(step_block/2)
                
            else:
                transaction_ERC_721 = []
                for obj in result['result']:
                    if len(obj['topics']) != 4:
                        continue
                    transaction_ERC_721.append(obj)
                  
                total_transaction += len(transaction_number)
                total_transaction_erc_721 += len(transaction_ERC_721)
                logging.info('Block: '+str(start_block)+' To '+str(start_block+step_block) + ', Step block: '+str(step_block)+ ', Total transaction: '+str(len(transaction_number))+', Transaction ERC-721: '+str(len(transaction_ERC_721))+', Crawled Transaction: '+str(total_transaction)+', Crawled Transaction ERC 721: '+str(total_transaction_erc_721))
                start_block += step_block
                
                
                
            

            

main()

    