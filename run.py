#!/usr/bin/env python

#sudo pip install flask
#sudo pip install bitcoin # https://github.com/vbuterin/pybitcointools/
#sudo apt-get install python-PyQt4
#sudo apt-get install python-gevent
 
import time
from flask import Flask, send_from_directory, jsonify, request, render_template
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from bitcoin import *  
import os, sys, threading, socket, platform
import json

# --- flask web app responses
app = Flask(__name__, template_folder='./lib', static_url_path='/lib', static_folder='lib')

@app.route("/")
def index():
    return render_template('view.html')

@app.route("/pyggy.svg")
def pyggysvg(): #returns pyggy.svg with main color replaced
    svgfile = openfile("lib/pyggy.svg")
    svg = svgfile.read().replace('PYGGYCOLOR', settings["color"])
    return svg
      
@app.route("/settings")
def returnsettings(): #return settings
    return jsonify(settings)
    
@app.route("/spend")
def callspendcoin(): #call spendcoin
    toaddress = request.args.get('toaddress')
    amtbtc = request.args.get('amtbtc')
    return spendcoin(toaddress, amtbtc)


# --- Use PyQt QWebView to display flask web app
class Application(QApplication):
    def __init__(self):
        if platform.system() == 'Linux':
            self.setAttribute(Qt.AA_X11InitThreads, True)
        QApplication.__init__(self, sys.argv)
        
def launch_window(port):
    app = Application()
    web = QWebView()
    web.load(QUrl("http://127.0.0.1:{0}".format(port)))
    web.setWindowTitle('Bitcoin Pyggy Bank')
    web.resize(375, 430)
    web.show()
    sys.exit(app.exec_())


# --- bitcoin transaction
def spendcoin(toaddress, amtbtc):
    #arrange transaction
    fee = int(settings["fee_satoshi"])
    amtsatoshi = int(float(amtbtc)*100000000) #btc to satoshi
    ins = select(unspent(settings["address"]), amtsatoshi+fee)
    outs = [{'value': amtsatoshi, 'address': toaddress}]
    #sign transaction
    tx = mksend(ins, outs, settings["address"], fee)
    print(tx)
    txsgn = sign(tx, 0, settings["wif"])
    print("TX: ", settings["address"], amtsatoshi, fee, toaddress)
    print(txsgn)
    pushtx(txsgn) # << post transaction
    return jsonify(txn=txsgn)

# --- files,settings
def openfile(relpath): #open file
    file_url = os.path.join(os.path.realpath(os.path.dirname(__file__)), relpath)
    return open(file_url)

def loadsettings(name): #load settings
    global settings
    settings = json.load(openfile(name + ".json"))
    settings["name"] = name

# --- main
def main():
    # start the web app in a background thread
    t = threading.Thread(target=app.run, kwargs={'port':settings['port']})
    t.daemon = True
    t.start()
    time.sleep(0.5)
    
    # launch the window
    launch_window(settings['port'])

settings = []

if __name__ == '__main__':
    loadsettings(sys.argv[1]) # $python pyggy.py <name>
    main()

