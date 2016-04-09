# BitcoinPiggyBank
Kid friendly bitcoin piggy bank, made with Python(Flask + PyQt QWebView + pybitcointools)


Customize name and color of a simple bitcoin piggy bank for kids.


**Use Case:**
Set up a recurring weekly payment (allowance) at Coinbase, to help young children learn about saving and spending. They can buy toys from Amazon with Purse.io, or use at stores with Gyft. No more counting and rolling coins! Supports spending to another address, and can save a default parent's address (e.g. if you bought them something at the store). Add an app like (Android) Bitcoin Balance on your phone, to easily check their address balance).


![Screenshot](https://raw.githubusercontent.com/SteveV916/BitcoinPiggyBank/master/screen.png "Screenshot")

Requirements:
- sudo pip install flask
- sudo pip install bitcoin
- sudo apt-get install python-qt4

Instructions:
- Edit and rename richie.json, to your child's name.json.
- Be sure to add your own bitcoin address and private key(wif)!
- Run with your child's name: $python run.py richie
