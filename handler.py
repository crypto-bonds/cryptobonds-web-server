from sawtooth_sdk.processor.exceptions import InvalidTransaction
from sawtooth_sdk.processor.handler import TransactionHandler


#calling the actions from the folder
from actions import acceptOrder
from actions import issuingBond
from actions import buyBandBond
from actions import initiateTrade
from actions import cancelTrade
from actions import bitcoin

#
class BondHandler(TransactionHandler):
    @property
    def bond_name(self):
        return "crptobond"

    @property
    def namespaces(self):
        return ['123456']

    @property   
    def bond_version(self):
        return ['1.0']

    def apply(self, transaction,context):

    #takes in the payload and figures out what order to do with the payload

    payload = decode(transaction.payload)

    action = payload.action
    publicKey = transaction.header.signerPublicKey

    if action == "Issuing_Bond_to_Bank" {
        return issuingBond(payload,header=transaction.header,state=state)
    }
    elif action == "Trader_Buys_Bank_Bond" {
        return buyBankBond(payload,header=transaction.header,state=state)
    }
    elif action == "Trader_Initiates_Trade" {
        return initiateTrade(payload,header=transaction.header,state=state)
    }
    elif action == "Trader_Cancels_Trade" {
        return cancelTrade(payload,header=transaction.header,state=state)
    }
    elif action == "Trader_Accepts_Order" {
        return acceptOrder(payload,header=transaction.header,state=state)
    }
    elif action == "Add_Bitcoin" {
        return bitcoin(payload,header=transaction.header,state=state)
    }