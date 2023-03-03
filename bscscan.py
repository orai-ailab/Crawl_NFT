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

# Xử lý dữ liệu JSON trả về từ BscScan để lấy thông tin về các giao dịch
if response.status_code == 200:
    data = response.json()
    result = data["result"]
    transactions = result["transactions"]
    for tx in transactions:
        print(tx)
else:
    print("Lỗi khi lấy dữ liệu từ BscScan")