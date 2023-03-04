import requests
from dotenv import load_dotenv
load_dotenv()
import os
# Thay đổi API key của bạn ở đây
API_KEY_BSCSCAN = os.getenv('API_KEY_BSCSCAN')

# Số block cần lấy thông tin
block_number = 1890000

# Gửi request để lấy thông tin về tất cả các giao dịch từ block cụ thể
url = f"https://api.bscscan.com/api?module=proxy&action=eth_getBlockByNumber&tag={block_number}&boolean=true&apikey={API_KEY_BSCSCAN}"
response = requests.get(url)

# hex nft 
HEX_NFT = ['0xa9059cbb','0x23b872dd','0x42966c68','0xd73dd623']
# Xử lý dữ liệu JSON trả về từ BscScan để lấy thông tin về các giao dịch

for i in range(block_number,block_number+1000000):
    if response.status_code == 200:
        data = response.json()
        result = data["result"]
        transactions = result["transactions"]
        for tx in transactions:
            print(tx['input'])
            if tx['input'] in HEX_NFT:
                print(tx)

    else:
        print("Lỗi khi lấy dữ liệu từ BscScan")