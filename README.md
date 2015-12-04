# BitcoinPiggyBank
Kid friendly bitcoin piggy bank, made with Python(Flask + PyQt QWebView + pybitcointools)


Customize name and color of a simple bitcoin piggy bank for kids.


**Use Case:**
Set up a recurring weekly payment (allowance) at Coinbase, to help young children learn about saving and spending. They can buy toys from Amazon with Purse.io, or use at stores with Gyft. No more counting and rolling coins! Supports spending to another address, and can save a default parent's address.


![Screenshot](https://raw.githubusercontent.com/SteveV916/BitcoinPiggyBank/master/screen.png "Screenshot")

Requirements:
- sudo pip install flask
- sudo pip install bitcoin # https://github.com/vbuterin/pybitcointools/
- sudo apt-get install python-PyQt4

Instructions:
- Edit and rename richie.json, to your child's name.json.
- Be sure to add your own bitcoin address and private key(wif)!
- Run with your child's name: $python run.py richie


P.S. - Yes, the private key is in a config file, but this is for kids not your life savings.
