# Hướng dẫn sử dụng getPriceToken.py

## Mục đích

Chương trình này giúp bạn tra cứu giá token trên mạng Solana một cách nhanh chóng bằng API Moralis.

---

## Cách sử dụng

### 1. Cài đặt thư viện cần thiết

Chạy lệnh sau trong terminal/cmd:

```bash
pip install requests
```
> **Lưu ý:** Không cần cài đặt `json` vì đây là module chuẩn của Python.

---

### 2. Lấy Moralis API Key

- Truy cập [https://admin.moralis.com/login](https://admin.moralis.com/login)
- Đăng ký tài khoản (miễn phí)
- Sau khi đăng nhập, vào mục **Web3 APIs** để lấy **API Key**
- Thay thế dòng sau trong file `getPriceToken.py`:
  ```python
  API_KEY = "YOUR_API_KEY"
  ```
  bằng API Key bạn vừa lấy được, ví dụ:
  ```python
  API_KEY = "abc123xyz..."
  ```

---

### 3. Chạy chương trình

Mở terminal/cmd tại thư mục chứa file và chạy:

```bash
python getPriceToken.py
```

---

### 4. Sử dụng chương trình

- Chương trình sẽ hiển thị danh sách các token Solana phổ biến cùng địa chỉ contract.
- Bạn nhập địa chỉ token muốn tra cứu (có thể copy từ danh sách hoặc nhập địa chỉ khác).
- Để thoát chương trình, nhấn `Ctrl+C` hoặc nhập `exit`.
- Kết quả sẽ hiển thị giá USD của token đó cùng ngày giờ hiện tại.

---

## Ví dụ sử dụng

```
---------------------------- Danh sách Token Solana Phổ Biến ----------------------------
STT   Tên                      Ký hiệu         Địa chỉ Token
------------------------------------------------------------------------------------------
1     Solana                   SOL             So11111111111111111111111111111111111111112
2     USD Coin                 USDC            EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
...
------------------------------------------------------------------------------------------
Hãy nhập địa chỉ token trong mạng Solana mà bạn muốn lấy thông tin (Ctrl+C để thoát): EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
Giá USD: 1.000000000000 | Thời gian: 2024-06-28 15:30:45
```

---

## Lưu ý

- Nếu chưa nhập API Key, chương trình sẽ nhắc bạn đăng ký.
- Nếu nhập sai địa chỉ token hoặc token không tồn tại, sẽ báo lỗi.
- Nếu gặp lỗi kết nối, hãy kiểm tra lại Internet hoặc thử lại sau.
- Có thể nhấn `Ctrl+C` bất cứ lúc nào để thoát chương trình.

---

## Liên hệ

Nếu có thắc mắc, vui lòng liên hệ hoặc để lại issue trên GitHub cá nhân của bạn.