# sTorGate

 Open the portal to the Tor network! Register your hidden service onion address on the ENS, use Metamask to explore Tor directly from your search bar, or just use our search engine.
## Inspiration
The [TOR network](https://2019.www.torproject.org/docs/onion-services.html.en) provides privacy to [millions of users](https://metrics.torproject.org/userstats-relay-country.html) around the world. Today, one of the major drawback for a wide adoption of Tor is the lack of a human-readable naming system. The onion addresses used to reach a node in the Tor network are part of the cryptographic protocol, and as such they are a practically a random sequence of characters.

The community has proposed [various solutions](https://blog.torproject.org/cooking-onions-names-your-onions), but there are shortcomings for each of them. 
The [ENS](https://ens.domains/) offers the perfect platform to solve many of these issues. Users can register an onion address and have their ENS name resolve it. The ENS takes care of the names distribution market, and provides a distributed "address book" that users can access via Metamask or our server.

## What it does
Our project contains several parts: 
- [we extended Metamask](https://github.com/ricott1/metamask-extension) to resolve .eth domain also to their `text["onion"]` entry;
- we added the option to [set an onion address](https://github.com/jvluso/ens-app) in the ens-app, to facilitate the registration of a hidden service to the ENS;
- we put [online](http://tnsksqdywtzhe5yrel5b5apizwhfbiqrhhmjmg66vtojkdmiascrlpyd.onion/) a hidden service that can resolve onion addresses, acting as a search engine for users that prefer to avoid installing addons. Our server use [Infura](https://infura.io/)  to connect to the Mainnet and the Ropsten blockchains. The hidden service is registered at storgate.eth on Mainnet and Ropsten;
- we wrote a simple [addon](https://github.com/ricott1/storgate) that connects directly to our server.
- we setup a Tor [Rocketchat](http://x25ufqll2pk53hqx.onion) (chat.storgate.eth) to use as a platform for discussion on future improvements.

## Challenges we ran into
We spent some time trying to adapt the `setContent()` function already provided by the ENSPublicResolver to accept onion addresses, but unluckily we were not able to use it as the v3 onions are too long. 

Our project has many different components, and getting them to work all together has represented a hurdle that we are proud to have overcome.

## Accomplishments that we're proud of
sTorGate works. People around the world can start using it today, they just need to [download the modified Metamask addon](https://github.com/ricott1/metamask-extension) or the [sTorGate addon](https://github.com/ricott1/storgate) to visit our server, and start surfing Tor and [register](https://github.com/jvluso/ens-app) their hidden services on the ENS.

## What we learned
We learned a lot about the ENS and Tor platforms, and the way Metamask can be integrated with the ENS to provide an integrated user experience.

## What's next for sTorGate
If this platform gets adopted by the community, it could be useful to define a special resolver for onion addresses, in an analogous way to the Ipfs resolver. 

We would like to see our pull requests accepted and integrated in the main repositories.