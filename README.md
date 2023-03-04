# Crawl_NFT on BSCSCAN
Get "Internal Transactions" by Block Range
Returns the list of internal transactions performed within a block range, with optional pagination.
Note : This API endpoint returns a maximum of 10000 records only.
````
https://api.bscscan.com/api
   ?module=account
   &action=txlistinternal
   &startblock=0
   &endblock=2702578
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
````


# Crawl_NFT on ETHERSCAN
# Get "Internal Transactions" by Block Range
# Returns the list of internal transactions performed within a block range, with optional pagination.
​​  Note : This API endpoint returns a maximum of 10000 records only.
````
https://api.etherscan.io/api
   ?module=account
   &action=txlistinternal
   &startblock=13481773
   &endblock=13491773
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken
````




#Get Event Logs by Topics
#Returns the events log in a block range, filtered by topics. 
````
https://api.etherscan.io/api
   ?module=logs
   &action=getLogs
   &fromBlock=12878196
   &toBlock=12879196
   &topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef
   &topic0_1_opr=and
   &topic1=0x0000000000000000000000000000000000000000000000000000000000000000
   &page=1
   &offset=1000
   &apikey=YourApiKeyToken
````
Usage:
For a single topic, specify the topic number such as topic0, topic1, topic2, topic3
For multiple topics, specify the topic numbers and topic operator either and or or such as below

topic0_1_opr (and|or between topic0 & topic1), topic1_2_opr (and|or between topic1 & topic2) topic2_3_opr (and|or between topic2 & topic3), topic0_2_opr (and|or between topic0 & topic2) topic0_3_opr (and|or between topic0 & topic3), topic1_3_opr (and|or between topic1 & topic3)