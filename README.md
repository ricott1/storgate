# storgate
ENS for TOr

propose to add new standard interface to supportInterface function in resolver, to point to address.onion on tor network.

var myRegistrar = fifsRegistrarContract.at(address);
new Date(testRegistrar.expiryTimes(web3.sha3('myname')).toNumber() * 1000)

//If this line returns a date earlier than the current date, the name is available and you’re good to go.

testRegistrar.register(web3.sha3('myname'), eth.accounts[0], {from: eth.accounts[0]});



## Todo

Add option to choose which blockchain to search for (Mainnet, Ropsten, ...). Add provider for each blockchain on server, maybe using infura, and different research option in get request.