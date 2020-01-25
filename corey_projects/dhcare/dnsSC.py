import json

from web3 import Web3


def dnsSC_get(account_address):
    infura_url = 'https://ropsten.infura.io/v3/db1690d7911842a6a0ec7690d08a0ca3'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    with open('dhcare/dnsSC_abi.json') as json_file:
        dnsSC_abi = json.load(json_file)

    dnsSC_address = '0x274D835998CDb077C224531619eB6e4D86b7739d'

    dnsSC = web3.eth.contract(address=dnsSC_address, abi=dnsSC_abi)

    try:
        getProvider = dnsSC.functions.getProvider(account_address).call()
        provider = {'provider_name': getProvider[0], 'provider_webAddress': getProvider[1]}
        return (provider)
    except:
        return ('Unable to Retrieve Information')


def dnsSC_post(name, webAddress):
    infura_url = 'https://ropsten.infura.io/v3/db1690d7911842a6a0ec7690d08a0ca3'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    with open('dhcare/dnsSC_abi.json') as json_file:
        dnsSC_abi = json.load(json_file)

    dnsSC_address = '0x274D835998CDb077C224531619eB6e4D86b7739d'

    dnsSC = web3.eth.contract(address=dnsSC_address, abi=dnsSC_abi)
    key = '0x3E67D814F4794E3172A94C8AF582C75A6B4868F4FAC912F234E78AE97D44518A'
    acct = web3.eth.account.privateKeyToAccount(key)
    account_address = acct.address

    try:
        tx = dnsSC.functions.createProvider(name, webAddress).buildTransaction(
            {'nonce': web3.eth.getTransactionCount(account_address)})
        signed_tx = web3.eth.account.signTransaction(tx, key)
        hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return ('Information was Submitted Successfully! Transaction Ref. ' + hash.hex())
    except:
        return ('Unable to Submit Information')
