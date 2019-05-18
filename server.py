from flask import Flask, request
from flask_cors import CORS
from time import gmtime, strftime
import eth_utils
import json

def get_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def resultPage(query):
	return """
<div>
<p>Query: {}</p>
<p>Owner: {}</p>
<p>Resolver: {}</p>
<p>Address: {}</p>
<p>Onion: {}</p>
</div>
			""".format(query, database[query]["owner"], database[query]["resolver"],database[query]["address"], database[query]["onion"])

def get_resolver_data(query, net="ropsten"):
    print(ENS.namehash(query))
    registry = web3_data["ENSRegistry"]["contract"][net]
    resol = registry.functions.resolver(ENS.namehash(query))
    owner = registry.functions.owner(ENS.namehash(query))
    resolver = w3[net].eth.contract(resol.call(), abi=web3_data["PublicResolver"]["abi"])
    address = resolver.functions.addr(ENS.namehash(query))
    onion = resolver.functions.text(ENS.namehash(query), "onion")
    
# ns[net].owner(query)
    #print(ns[net].address('jasoncarver.eth'))
    return {"owner" : owner.call(), "resolver" : resol.call(), "address" : address.call(), "onion" : onion.call()}

# def set_onion(name, net="ropsten"):
#     0x5FfC014343cd971B7eb70732021E26C35B744cc4
def normalize_32_byte_hex_address(value):
    as_bytes = eth_utils.to_bytes(hexstr=value)
    return eth_utils.to_normalized_address(as_bytes[-20:])
database = {}
app = Flask(__name__)
CORS(app)

from web3 import Web3
from ens import ENS

web3_data = {
            "provider" : {
                            "local" : Web3.HTTPProvider("http://127.0.0.1:7545"),
                            "mainnet" : Web3.HTTPProvider("https://mainnet.infura.io/v3/86043d9797ae462e87d110d9cabc9616"),
                            "ropsten" : Web3.HTTPProvider("https://ropsten.infura.io/v3/86043d9797ae462e87d110d9cabc9616")},  
            "ENSRegistry" : {
                            "local" :   "0x2042d86549e351d78255cb3e9ac18042e781e320",
                            "mainnet" : "0x314159265dD8dbb310642f98f50C066173C1259b",
                            "ropsten" : "0x112234455C3a32FD11230C42E7Bccd4A84e02010",
                            "abi" : '[{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"label","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setSubnodeOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"ttl","type":"uint64"}],"name":"setTTL","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"label","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"NewOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"resolver","type":"address"}],"name":"NewResolver","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"ttl","type":"uint64"}],"name":"NewTTL","type":"event"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"resolver","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"ttl","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"}]'},
            "PublicResolver" : {
                            "local" : "",
                            "mainnet" : "0x314159265dD8dbb310642f98f50C066173C1259b",
                            "ropsten" : "0x5FfC014343cd971B7eb70732021E26C35B744cc4",
                            "abi" : '[{"constant":true,"inputs":[{"name":"interfaceID","type":"bytes4"}],"name":"supportsInterface","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"key","type":"string"},{"name":"value","type":"string"}],"name":"setText","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"},{"name":"contentTypes","type":"uint256"}],"name":"ABI","outputs":[{"name":"contentType","type":"uint256"},{"name":"data","type":"bytes"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"x","type":"bytes32"},{"name":"y","type":"bytes32"}],"name":"setPubkey","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"content","outputs":[{"name":"ret","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"addr","outputs":[{"name":"ret","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"},{"name":"key","type":"string"}],"name":"text","outputs":[{"name":"ret","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"contentType","type":"uint256"},{"name":"data","type":"bytes"}],"name":"setABI","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"name","outputs":[{"name":"ret","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"name","type":"string"}],"name":"setName","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"hash","type":"bytes32"}],"name":"setContent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"pubkey","outputs":[{"name":"x","type":"bytes32"},{"name":"y","type":"bytes32"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"addr","type":"address"}],"name":"setAddr","outputs":[],"payable":false,"type":"function"},{"inputs":[{"name":"ensAddr","type":"address"}],"payable":false,"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"a","type":"address"}],"name":"AddrChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"hash","type":"bytes32"}],"name":"ContentChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"name","type":"string"}],"name":"NameChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"contentType","type":"uint256"}],"name":"ABIChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"x","type":"bytes32"},{"indexed":false,"name":"y","type":"bytes32"}],"name":"PubkeyChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"indexedKey","type":"string"},{"indexed":false,"name":"key","type":"string"}],"name":"TextChanged","type":"event"}]'}
            }


w3 = {net : Web3(web3_data["provider"][net]) for net in web3_data["provider"]}
ns = {net : ENS.fromWeb3(w3[net]) for net in w3}

web3_data["ENSRegistry"]["contract"] = {net : w3[net].eth.contract(w3[net].toChecksumAddress(web3_data["ENSRegistry"][net]), abi=web3_data["ENSRegistry"]["abi"]) for net in w3}
web3_data["PublicResolver"]["contract"] = {net : w3[net].eth.contract(web3_data["PublicResolver"][net], abi=web3_data["PublicResolver"]["abi"]) for net in w3}

# from ens import ENS
# ns = ENS(provider)


# eth_address = ns.address('jasoncarver.eth')

# assert eth_address == '0x5B2063246F2191f18F2675ceDB8b28102e957458'

@app.route('/search', methods=['GET'])
def search():
    parameters = {key : request.args.get(key) for key in request.args}
    timestamp = get_time()
    parameters["timestamp"] = timestamp
    print(parameters, database)
    if not "q" in parameters:
        return "Invalid request"
    
    search_type = "complete" if (not "type" in parameters or not parameters["type"] in ["complete", "result"]) else parameters["type"]
    net = "mainnet" if (not "net" in parameters or not parameters["net"] in ["local", "mainnet", "ropsten"]) else parameters["net"]

    query = parameters["q"]
    if net == "mainnet":
        if not query.endswith(".eth"):
        	query += ".eth"
    elif net == "ropsten":
        if not query.endswith(".eth") and not query.endswith(".test"):
            query += ".eth"
    database[query] = get_resolver_data(query, net)
    if search_type == "complete":
        return resultPage(query)
    return json.dumps(database[query])

app.run(debug=True, use_reloader=True, port=5070)

