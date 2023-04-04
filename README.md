# Crawl_NFT

## Example on BSCSCAN
* Get "Internal Transactions" by Block Range
* Returns the list of internal transactions performed within a block range, with optional pagination.
* Get "Internal Transactions" by Block Range
* Returns the list of internal transactions performed within a block range, with optional pagination.
### Note : This API endpoint returns a maximum of 10000 records only.
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



## Get Event Logs by Topics
### Returns the events log in a block range, filtered by topics. 
````
https://api.bscscan.io/api
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
## Usage:
For a single topic, specify the topic number such as topic0, topic1, topic2, topic3
For multiple topics, specify the topic numbers and topic operator either and or or such as below

topic0_1_opr (and|or between topic0 & topic1), topic1_2_opr (and|or between topic1 & topic2) topic2_3_opr (and|or between topic2 & topic3), topic0_2_opr (and|or between topic0 & topic2) topic0_3_opr (and|or between topic0 & topic3), topic1_3_opr (and|or between topic1 & topic3)


# BSCSCAN ERC 721 Crawler

This is a Python script that crawls the BSC blockchain for ERC-721 transaction events using BSCSCAN API and saves them to a BigQuery table. It filters the transaction events based on an `event signature` and logs the activity.

## Requirements
* Python 3.x
* Required Python packages are listed in `requirements.txt` file.


## Installation

1. Clone the repository and navigate to the project directory:

``` bash
   git clone https://github.com/orai-ailab/Crawl_NFT.git
   cd Crawl_NFT
```

2. Install the required Python packages:

``` bash
   pip install -r requirements.txt
```

3. Create a BSCSCAN API key (https://bscscan.com/myapikey) and add it to `.env` file.

4. Create a BigQuery dataset and a table for the transactions.

5. Fill in the details in the `key_path`, and `table_id` variables in line 14 and 62 respectively.  

6. Run the script using:

``` bash
   python bscscan_erc721.py
```

## Usage

The script is designed to automatically search BSC blockchain for ERC-721 transactions and add them to a BigQuery table. 
