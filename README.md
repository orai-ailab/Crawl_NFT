# Crawl_NFT on BSCSCAN
Get "Internal Transactions" by Block Range
Returns the list of internal transactions performed within a block range, with optional pagination.
Note : This API endpoint returns a maximum of 10000 records only.
```
https://api.bscscan.com/api
   ?module=account
   &action=txlistinternal
   &startblock=0
   &endblock=2702578
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken```