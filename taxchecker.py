from web3 import Web3
import sys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--a", help="Token address")
args = parser.parse_args()

w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))
token_address = w3.toChecksumAddress(args.a)
swapabi = '[{"inputs": [{"internalType": "address","name": "_factory","type": "address"},{"internalType": "address", "name": "_WETH","type": "address"},{"internalType": "address","name": "_UTILS","type": "address"},{"internalType": "address","name": "_TIGS","type": "address"}], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [], "name": "DEV", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "FEE", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "FEEQuote", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "LimitSwap", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "STATUS", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "TIGS", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "TIGSStaking", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "UTILS", "outputs": [ { "internalType": "contract TIGSSwapUtils", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "WETH", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_token", "type": "address" }, { "internalType": "address", "name": "_spender", "type": "address" } ], "name": "approveToken", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "factory", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "Token", "type": "address" } ], "name": "fetchBestBaseToken", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "Token", "type": "address" } ], "name": "fetchLiquidityETH", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "Token", "type": "address" }, { "internalType": "uint256", "name": "Slippage", "type": "uint256" } ], "name": "fromETHtoToken", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "Token", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" }, { "internalType": "uint256", "name": "Slippage", "type": "uint256" } ], "name": "fromTokentoETH", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "TokenA", "type": "address" }, { "internalType": "address", "name": "TokenB", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" }, { "internalType": "uint256", "name": "Slippage", "type": "uint256" } ], "name": "fromTokentoToken", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountOut", "type": "uint256" }, { "internalType": "uint256", "name": "reserveIn", "type": "uint256" }, { "internalType": "uint256", "name": "reserveOut", "type": "uint256" } ], "name": "getAmountIn", "outputs": [ { "internalType": "uint256", "name": "amountIn", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountIn", "type": "uint256" }, { "internalType": "uint256", "name": "reserveIn", "type": "uint256" }, { "internalType": "uint256", "name": "reserveOut", "type": "uint256" } ], "name": "getAmountOut", "outputs": [ { "internalType": "uint256", "name": "amountOut", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountOut", "type": "uint256" }, { "internalType": "address[]", "name": "path", "type": "address[]" } ], "name": "getAmountsIn", "outputs": [ { "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountIn", "type": "uint256" }, { "internalType": "address[]", "name": "path", "type": "address[]" } ], "name": "getAmountsOut", "outputs": [ { "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "Token", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "getOutputfromETHtoToken", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "Token", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "getOutputfromTokentoETH", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "TokenA", "type": "address" }, { "internalType": "address", "name": "TokenB", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "getOutputfromTokentoToken", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "address[]", "name": "", "type": "address[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "Token", "type": "address" } ], "name": "getTokenInformations", "outputs": [ { "internalType": "uint256", "name": "BuyEstimateOutput", "type": "uint256" }, { "internalType": "uint256", "name": "BuyRealOutput", "type": "uint256" }, { "internalType": "uint256", "name": "SellEstimateOutput", "type": "uint256" }, { "internalType": "uint256", "name": "SellRealOutput", "type": "uint256" }, { "internalType": "bool", "name": "Buy", "type": "bool" }, { "internalType": "bool", "name": "Approve", "type": "bool" }, { "internalType": "bool", "name": "Sell", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "makeBuyback", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "minWETH", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "input", "type": "address" }, { "internalType": "address", "name": "output", "type": "address" } ], "name": "pairFor", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_factory", "type": "address" }, { "internalType": "address", "name": "path1", "type": "address" }, { "internalType": "address", "name": "path2", "type": "address" } ], "name": "pairForTest", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountA", "type": "uint256" }, { "internalType": "uint256", "name": "reserveA", "type": "uint256" }, { "internalType": "uint256", "name": "reserveB", "type": "uint256" } ], "name": "quote", "outputs": [ { "internalType": "uint256", "name": "amountB", "type": "uint256" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_FEE", "type": "uint256" }, { "internalType": "uint256", "name": "_FEEQuote", "type": "uint256" }, { "internalType": "uint256", "name": "_minWETH", "type": "uint256" } ], "name": "setFeeOptions", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_LimitSwap", "type": "address" } ], "name": "setLimitSwapContract", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_UTILS", "type": "address" } ], "name": "setNewUtils", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "bool", "name": "_new", "type": "bool" } ], "name": "setStatus", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "amountIn", "type": "uint256" }, { "internalType": "uint256", "name": "amountOutMin", "type": "uint256" }, { "internalType": "address[]", "name": "path", "type": "address[]" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "deadline", "type": "uint256" } ], "name": "swapExactTokensForTokensAdmin", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "stateMutability": "payable", "type": "receive" }]'


class TXN():
    def __init__(self):
        self.token_address = token_address
        self.swapper_address, self.swapper = self.setup_swapper()
    
    def setup_swapper(self):
        #honeypot checker and tax
        swapper_address = '0x18be7f977Ec1217B71D0C134FBCFF36Ea4366fCD'
        contract_abi = swapabi
        swapper = w3.eth.contract(address=swapper_address, abi=contract_abi)
        return swapper_address, swapper    

    def checkToken(self):
        tokenInfos = self.swapper.functions.getTokenInformations(self.token_address).call()
        buy_tax = round((tokenInfos[0] - tokenInfos[1]) / tokenInfos[0] * 100 ,2) 
        sell_tax = round((tokenInfos[2] - tokenInfos[3]) / tokenInfos[2] * 100 ,2)
        if tokenInfos[5] and tokenInfos[6] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot

    def checkifTokenBuyDisabled(self):
        disabled = self.swapper.functions.getTokenInformations(self.token_address).call()[4] #True if Buy is enabled, False if Disabled.
        #todo: find a solution for bugged tokens that never can be buy.
        return disabled

    def awaitEnabledBuy(self):
        print('Checking Trade Status !')
        while True:
            try:
                if self.checkifTokenBuyDisabled() == True:
                    break
            except Exception as e:
                if "UPDATE" in str(e):
                    print(e)
                    sys.exit()
                continue
            except KeyboardInterrupt:
                break
        print('Trade is Enabled')

    def tax(self):
        while True:
            try:
                honeyTax = self.checkToken()
                print('Buy Tax : '+str(honeyTax[0])+'%  '+'Sell Tax : '+str(honeyTax[1])+'%')
                if honeyTax[0] > 25:
                    print('Waiting Tax Lower than '+str(honeyTax[0])+'%')
                    while True:
                        honeyTax = self.checkToken()
                        if honeyTax[0] < 25:
                            break
                if honeyTax[0] < 25:
                    break
            except Exception as e:
                if 'execution reverted' in str(e):
                    break

    def run(self):
        start = time.time()
        self.awaitEnabledBuy()
        self.tax()
        end = time.time()
        print(end-start, 'Seconds')

TXN().run()
