# Baboucoin

## Data Structure

Use SQLite for database

Three tables:
* HEADERS
* TRANSACTIONS
* MEMPOOL

### HEADERS
* height
* difficulty
* timestamp
* merkletreeroot
* nonce

### TRANSACTIONS
* height
* from RSA
* to RSA
* value
* signature

### MEMPOOL
* from RSA
* to RSA
* value
* signature

MEMPOOL table is cleared each time a block is mined
