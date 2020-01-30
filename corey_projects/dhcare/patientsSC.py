import json

from web3 import Web3


def patientsSC_get(account_address):
    infura_url = 'https://ropsten.infura.io/v3/db1690d7911842a6a0ec7690d08a0ca3'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    with open('dhcare/patientsSC_abi.json') as json_file:
        patientsSC_abi = json.load(json_file)

    patientsSC_address = '0x9a38c0a3F4128CA1ef9f6bffD3821C75826461Fa'

    patientsSC = web3.eth.contract(address=patientsSC_address, abi=patientsSC_abi)

    try:
        getProvider = patientsSC.functions.getProvider(account_address).call()
        provider = {'provider_name': getProvider[0], 'provider_webAddress': getProvider[1]}
        return (provider)
    except:
        return ('Unable to Retrieve Information')


def patientsSC_post(name, webAddress):
    infura_url = 'https://ropsten.infura.io/v3/db1690d7911842a6a0ec7690d08a0ca3'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    with open('dhcare/patientsSC_abi.json') as json_file:
        patientsSC_abi = json.load(json_file)

    patientsSC_address = '0x9a38c0a3F4128CA1ef9f6bffD3821C75826461Fa'

    patientsSC = web3.eth.contract(address=patientsSC_address, abi=patientsSC_abi)
    key = '0x3E67D814F4794E3172A94C8AF582C75A6B4868F4FAC912F234E78AE97D44518A'
    acct = web3.eth.account.privateKeyToAccount(key)
    account_address = acct.address

    try:
        tx = patientsSC.functions.createProvider(name, webAddress).buildTransaction(
            {'nonce': web3.eth.getTransactionCount(account_address)})
        signed_tx = web3.eth.account.signTransaction(tx, key)
        hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return ('Information was Submitted Successfully! Transaction Ref. ' + hash.hex())
    except:
        return ('Unable to Submit Information')
