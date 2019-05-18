from flask import Flask, request
from flask_cors import CORS
from time import gmtime, strftime
import eth_utils, json, multihash


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def resultPage(query):
	return """
<div>
<p>Query: {}</p>
<p>Owner: {}</p>
<p>Resolver: {}</p>
<p>Address: {}</p>
<p>Content: {}</p>
<p>ContentHash: {}</p>
<p>Onion: {}</p>
</div>
			""".format(query, database[query]["owner"], database[query]["resolver"],database[query]["address"], database[query]["content"], database[query]["contenthash"], database[query]["onion"])

def is_empty_hex(hash):
    return (hash in [b"", b"\x00\x00", b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"])

def get_resolver_data(query, net="ropsten"):
    registry = web3_data["ENSRegistry"]["contract"][net]
    resol = registry.functions.resolver(ENS.namehash(query)).call()
    owner = registry.functions.owner(ENS.namehash(query)).call()

    resolver = w3[net].eth.contract(resol, abi=web3_data["PublicResolver"]["abi"])
    if resolver.functions.supportsInterface("0x3b3b57de").call():#addr interface
        address = resolver.functions.addr(ENS.namehash(query)).call()
    else:
        address = ""

    contenthash = ""
    if resolver.functions.supportsInterface("0xbc1c58d1").call():#contentHash interface
        contenthashbytes = resolver.functions.contenthash(ENS.namehash(query)).call()
        print(is_empty_hex(contenthashbytes), "contenthash")
        if not is_empty_hex(contenthashbytes):
            buffer = multihash.encode(contenthashbytes, "sha2-256")
            contenthash = multihash.to_b58_string(buffer)
    
    content = ""      
    if resolver.functions.supportsInterface("0xd8389dc5").call():#content interface
        contentbytes = resolver.functions.content(ENS.namehash(query)).call()
        print(is_empty_hex(contentbytes), "content")
        if not is_empty_hex(contentbytes):
            buffer = multihash.encode(contentbytes, "sha2-256")
            content = multihash.to_b58_string(buffer)

    if resolver.functions.supportsInterface("0x59d1d43c").call():#text interface
        onion = resolver.functions.text(ENS.namehash(query), "onion").call()
    else:
        onion = ""
    
    return {"owner" : owner, "resolver" : resol, "address" : address, "content" : content, "contenthash" : contenthash, "onion" : onion}

database = {}
app = Flask(__name__)
CORS(app)

from web3 import Web3
from ens import ENS

web3_data = {
            "provider" : {
                            "mainnet" : Web3.HTTPProvider("https://mainnet.infura.io/v3/86043d9797ae462e87d110d9cabc9616"),
                            "ropsten" : Web3.HTTPProvider("https://ropsten.infura.io/v3/86043d9797ae462e87d110d9cabc9616")},  
            "ENSRegistry" : {
                            "mainnet" : "0x314159265dD8dbb310642f98f50C066173C1259b",
                            "ropsten" : "0x112234455C3a32FD11230C42E7Bccd4A84e02010",
                            "abi" : '[{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"label","type":"bytes32"},{"name":"owner","type":"address"}],"name":"setSubnodeOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"ttl","type":"uint64"}],"name":"setTTL","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"label","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"NewOwner","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"owner","type":"address"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"resolver","type":"address"}],"name":"NewResolver","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"ttl","type":"uint64"}],"name":"NewTTL","type":"event"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"resolver","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"ttl","outputs":[{"name":"","type":"uint64"}],"payable":false,"stateMutability":"view","type":"function"}]'},
            "PublicResolver" : {
                            "mainnet" : "0x314159265dD8dbb310642f98f50C066173C1259b",
                            "ropsten" : "0x5FfC014343cd971B7eb70732021E26C35B744cc4",
                            "abi" : '[{"constant":true,"inputs":[{"name":"interfaceID","type":"bytes4"}],"name":"supportsInterface","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"key","type":"string"},{"name":"value","type":"string"}],"name":"setText","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"},{"name":"contentTypes","type":"uint256"}],"name":"ABI","outputs":[{"name":"contentType","type":"uint256"},{"name":"data","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"x","type":"bytes32"},{"name":"y","type":"bytes32"}],"name":"setPubkey","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"hash","type":"bytes"}],"name":"setContenthash","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"hash","type":"bytes32"}],"name":"setContent","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"addr","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"content","outputs":[{"name":"ret","type":"bytes32"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"},{"name":"key","type":"string"}],"name":"text","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"contentType","type":"uint256"},{"name":"data","type":"bytes"}],"name":"setABI","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"name","type":"string"}],"name":"setName","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"contenthash","outputs":[{"name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"node","type":"bytes32"}],"name":"pubkey","outputs":[{"name":"x","type":"bytes32"},{"name":"y","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"node","type":"bytes32"},{"name":"addr","type":"address"}],"name":"setAddr","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"ensAddr","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"a","type":"address"}],"name":"AddrChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"name","type":"string"}],"name":"NameChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":true,"name":"contentType","type":"uint256"}],"name":"ABIChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"x","type":"bytes32"},{"indexed":false,"name":"y","type":"bytes32"}],"name":"PubkeyChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"indexedKey","type":"string"},{"indexed":false,"name":"key","type":"string"}],"name":"TextChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"node","type":"bytes32"},{"indexed":false,"name":"hash","type":"bytes"}],"name":"ContenthashChanged","type":"event"}]'}
                        }

w3 = {net : Web3(web3_data["provider"][net]) for net in web3_data["provider"]}
ns = {net : ENS.fromWeb3(w3[net]) for net in w3}

web3_data["ENSRegistry"]["contract"] = {net : w3[net].eth.contract(web3_data["ENSRegistry"][net], abi=web3_data["ENSRegistry"]["abi"]) for net in w3}
web3_data["PublicResolver"]["contract"] = {net : w3[net].eth.contract(web3_data["PublicResolver"][net], abi=web3_data["PublicResolver"]["abi"]) for net in w3}

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

