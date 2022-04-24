from web3 import Web3
import time, json
from decimal import *
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))



#connecting web3 to Ganache
if  web3.isConnected() == True:
    print("web3 connected...\n")
else :
    print("error connecting...")



#accounts value and private key

account_1 = "0x242F5c9a1D42e962A1c6B479349FFAf188163757" ## add public key from first account (sender)
account_2 = "0x0F1eFBb7b0C2Af2CC7d0976655A4a0e95AdB2246" ## add public key from second account (reciver)
private_key = "3ddc37fdcd6ba99f9a16206467e459d4009ab30b3b4909a5ba0ca50ea40d2624" ## add ETH private key from first account (sender)



#Get balance account
address = '0x9FAE0B98d66321cc6Ac0B6A35d79b23aD8321976'
balance = web3.eth.get_balance(address)
# print(balance)

result = web3.fromWei(balance,'ether')
print(result)

gas_fee = 21000*5
gas_fee = Decimal(gas_fee)
gas_fee = web3.fromWei(gas_fee,'Gwei')


def get_balance_loop():
    balance=0
    while True:
        while 0.0005>balance:
            #Get balance account
            balance = web3.eth.getBalance(account_1)
            balance = web3.fromWei(balance, "ether") #convert to ether value

        balance = balance-gas_fee
        print(balance)
        # print(balance)
        # print(web3.fromWei(balance, "ether"))
        build_transaction(balance)
        


def build_transaction(balance):
    #get nonce number
    nonce = web3.eth.getTransactionCount(account_1)
#build transaction
    tx = {
        'nonce':nonce,
        'to':account_2,
        'value':web3.toWei(balance,'ether'),
        'gas':21000,
        'gasPrice':web3.toWei('56','gwei')
    }

    #sign transaction with private key
    signed_tx = web3.eth.account.signTransaction(tx,private_key)
    #send Transaction
    tx_hash= web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    print(web3.toHex(tx_hash))
    get_balance_loop()
get_balance_loop()