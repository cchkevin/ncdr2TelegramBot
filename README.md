# ncdr2TelegramBot 民生示警公開資料轉送 Telegram
由民生示警公開資料平台(https://alerts.ncdr.nat.gov.tw/indexHome.aspx)取得推送的災害示警資訊
在 Raspberry Pi上搭建一個 nginx + flask 進行接收, 經由Telegram Bot API 進行訊息轉發

建置說明: 
1.環境需安裝 Flask 及 xmltodict 套件
2.災害推送訊息需上民生示警公開資料平台冊會員後進行線上申請
3.申請Telegram Bot及查到Chat Id
4.APP.PY的程式碼內請自行修改Telegram Bot 的Token 及 Chat id
5.Happy Coding ~
