# 🎟️ TicketPlus 自動搶票程式

這是一個基於 **Python + Selenium** 的自動化搶票腳本，可以同時開啟多個瀏覽器分身，自動登入並嘗試購買指定票券。  

---

## 📌 功能
- 自動開啟多個瀏覽器分身搶票
- 自動登入帳號密碼
- 自動點擊票數 + 下一步
- 自動檢測「更新票數」按鈕並刷新
- 瀏覽器最大化，並關閉圖片載入以提升速度

---

## 🛠 環境需求
- Python 3.8+
- Google Chrome
- ChromeDriver（自動由 `webdriver_manager` 安裝）

---

## 📦 安裝
1. 下載專案程式碼
2. 安裝必要套件：
   ```bash
   pip install selenium webdriver-manager
