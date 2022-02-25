from flask import Flask, jsonify, request

app = Flask(__name__)

from servers import servers

#import csv
 
#with open('challenge/players.csv', newline='') as File:  
#    players = csv.reader(File)
#    for row in players:
#        print(row)

@app.route('challenge/<string:name>')
def banPlayerServer(server_name):
    serverFound = [server for server in servers if server['name'] == server_name]
    if len(productsFound) > 0:
        

if __name__ == '__main__':
    app.run(debug=True, port=4000)