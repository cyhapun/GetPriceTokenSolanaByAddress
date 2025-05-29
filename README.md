# Kiểm Tra Giá Token Đa Chuỗi (getPriceToken.py)

## Tổng Quan
Công cụ này giúp bạn kiểm tra giá token trên nhiều mạng blockchain khác nhau thông qua API Moralis. Hỗ trợ cả Solana và các chuỗi tương thích EVM.

## Tính Năng
- Hỗ trợ đa chuỗi (Solana, Ethereum, BSC, Polygon, v.v.)
- Kiểm tra giá theo thời gian thực
- Danh sách token phổ biến
- Giao diện thân thiện với người dùng

## Yêu Cầu Hệ Thống
- Python 3.6 trở lên
- Kết nối Internet
- API key của Moralis

## Hướng Dẫn Cài Đặt

### 1. Cài Đặt Thư Viện
Chạy lệnh sau trong terminal:
```bash
pip install moralis requests
```

### 2. Thiết Lập API Moralis
1. Truy cập [Moralis Admin Panel](https://admin.moralis.com/login)
2. Tạo tài khoản miễn phí
3. Vào mục "Web3 APIs"
4. Sao chép API key
5. Cập nhật trong file `getPriceToken.py`:
```python
API_KEY = "YOUR_API_KEY"  # Thay bằng API key của bạn
```

## Cách Sử Dụng

### 1. Khởi Động
```bash
python getPriceToken.py
```

### 2. Các Bước Thực Hiện
1. Chọn mạng blockchain (chain):
   - Nhấn Enter để mặc định chọn Solana
   - Hoặc nhập tên chain (eth, bsc, polygon,...)
2. Nhập địa chỉ token:
   - Copy từ danh sách có sẵn
   - Hoặc nhập địa chỉ token bất kỳ
3. Xem kết quả:
   - Giá USD hiện tại
   - Phần trăm thay đổi (đối với chain EVM)
   - Thời gian cập nhật

## Danh Sách Chain Hỗ Trợ
- Solana
- Ethereum (ETH)
- Binance Smart Chain (BSC)
- Polygon
- Avalanche
- Fantom
- Cronos
- Arbitrum
- Optimism
- Base
- Linea
- Moonbeam
- Ronin
- PulseChain

## Xử Lý Lỗi
- **API Key không hợp lệ**: Kiểm tra lại API key trong file
- **Địa chỉ token không tồn tại**: Xác nhận lại địa chỉ token
- **Lỗi kết nối**: Kiểm tra internet hoặc thử lại sau
- **Chain không hỗ trợ**: Chọn chain từ danh sách hỗ trợ

## Liên Hệ & Hỗ Trợ
Nếu cần hỗ trợ thêm:
- Tạo issue trên GitHub
- Theo dõi các cập nhật mới
