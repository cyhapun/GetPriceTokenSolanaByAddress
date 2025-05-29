import requests
import json
import datetime

API_KEY = "YOUR_API_KEY"

def display_popular_solana_tokens():
    popular_tokens = [
        {
            "name": "Solana",
            "symbol": "SOL",
            "address": "So11111111111111111111111111111111111111112"
        },
        {
            "name": "USD Coin",
            "symbol": "USDC",
            "address": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
        },
        {
            "name": "Tether",
            "symbol": "USDT",
            "address": "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
        },
        {
            "name": "Bonk",
            "symbol": "BONK",
            "address": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263"
        },
        {
            "name": "Jito",
            "symbol": "JTO",
            "address": "jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL"
        },
        {
            "name": "Pyth Network",
            "symbol": "PYTH",
            "address": "HZ1JovNiVvGrGNiiYvEozEVgZ58xaU3RKwX8eACQBCt3"
        },
        {
            "name": "Raydium",
            "symbol": "RAY",
            "address": "4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R"
        },
        {
            "name": "Popcat",
            "symbol": "POPCAT",
            "address": "7GCihgDB8fe6KNjn2MYtkzZcRjQy3t9GHdC8uHYmW2hr"
        },
        {
            "name": "dogwifhat",
            "symbol": "WIF",
            "address": "EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm"
        },
        {
            "name": "Fartcoin",
            "symbol": "FARTCOIN",
            "address": "9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump"
        }
    ]

    print("---------------------------- Danh sách Token Solana Phổ Biến ----------------------------")
    print("{:<5} {:<25} {:<15} {:<100}".format("STT", "Tên", "Ký hiệu", "Địa chỉ Token"))
    print("-" * 90)

    for i, token in enumerate(popular_tokens):
        print("{:<5} {:<25} {:<15} {:100}".format(
            i + 1,
            token["name"],
            token["symbol"],
            token["address"]
        ))
    
    print("-" * 90)

def get_price_token(token_address):
    url = f"https://solana-gateway.moralis.io/token/mainnet/{token_address}/price"
    headers = {"Accept": "application/json", "X-API-Key": API_KEY}

    if API_KEY == "YOUR_API_KEY":
        print(f"Vui lòng đăng kí API key tại 'https://admin.moralis.com/login'")
        return None
        
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy giá token: {e}")
        return None
    except json.JSONDecodeError:
        print("Lỗi giải mã JSON khi lấy giá token.")
        return None
    
if __name__ == "__main__":
    display_popular_solana_tokens()

    try:
        while True:
            token_address = input("Hãy nhập địa chỉ token trong mạng Solana mà bạn muốn lấy thông tin (Tổ hợp phím Ctrl+C hoặc 'exit' để thoát): ")
            if token_address.strip().lower() == "exit":
                print("Đã thoát chương trình.")
                break

            token_price = get_price_token(token_address)
            
            if token_price:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Giá USD: {token_price.get('usdPrice'):.12f}")
                print(f"Thời gian: {now}")
            else:
                print("Không thể lấy thông tin token. Vui lòng thử lại sau!")
    except KeyboardInterrupt:
        print("\nĐã thoát chương trình.")