import json

from web3 import Web3


def accessControlSC_add(nid, clinic_id):
    infura_url = 'https://ropsten.infura.io/v3/db1690d7911842a6a0ec7690d08a0ca3'
    web3 = Web3(Web3.HTTPProvider(infura_url))

    with open('dhcare/accessControlSC_abi.json') as json_file:
        accessControlSC_abi = json.load(json_file)

    accessControlSC_address = '0x158b4375E2A994578fDcf070b1c19b994A191D13'

    accessControlSC = web3.eth.contract(address=accessControlSC_address, abi=accessControlSC_abi)
    key = '0x3E67D814F4794E3172A94C8AF582C75A6B4868F4FAC912F234E78AE97D44518A'
    acct = web3.eth.account.privateKeyToAccount(key)
    account_address = acct.address

    try:
        tx = accessControlSC.functions.addClinic(nid, clinic_id).buildTransaction(
            {'nonce': web3.eth.getTransactionCount(account_address)})
        signed_tx = web3.eth.account.signTransaction(tx, key)
        hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return ('The appointment has been confirmed and access granted to the clinic. Your Transaction Ref. is '
                + hash.hex() + ' Please remember it for tracking purpose')
    except:
        return ('Unable to Submit Information')
