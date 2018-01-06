A buildpack for running an Electrum wallet in CLI mode, 
adapted from this older tutorial: http://www.genesisbloc.com/deploying-electrum-to-heroku/


Features:
- Wallet:
    - Initializes the entire wallet from a seed at startup (thanks to Electrum), no remote servers required.
    - Pays to an address.
    - Creates wallet addresses.
    - Checks wallet or address balance.
- JSON-RPC server:
    - Listens for commands for all the above; can support multiple wallets.


Flaws/TODO:
- Slow! There's overhead in starting up the Electrum script for every command. 
    - But I'm not experienced enough to do things manually using their Python library.
- "Battle testing" on my own Heroku server.


Use at your own risk. I barely know what I'm doing.
