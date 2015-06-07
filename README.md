# BitcoinPiggyBank
Kid friendly bitcoin piggy bank, made with Python(Flask + PyQt QWebView + pybitcointools)

Micro-pay your kids in bitcoin.
They can save, view, and spend their balance with this simple app.

![Screenshot](https://raw.githubusercontent.com/SteveV916/BitcoinPiggyBank/master/screen.png "Screenshot")

Requirements:
- sudo pip install flask
- sudo pip install bitcoin # https://github.com/vbuterin/pybitcointools/
- sudo apt-get install python-PyQt4
- sudo apt-get install python-gevent

Instructions:
- Edit and rename richie.json, to your child's <name>.json.
- Be sure to change to a new bitcoin address and private key (WIF)!
- Run with your child's name: $python run.py richie
