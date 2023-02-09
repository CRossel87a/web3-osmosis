import requests


# https://docs.osmosis.zone/apis/interact-rest
# https://lcd.osmosis.zone
# https://docs.osmosis.zone/api/?v=LCD#/operations/NumPools !!

class Osmosis():
    
    # server = 'https://lcd.osmosis.zone'
    def __init__(self, server):
        self.server = server
        
        
    # 633 = USDC.gr / OSMO
    # https://github.com/osmosis-labs/osmosis    
    def get_pool_liquidity(self, pool_id) -> dict:
        query = f'{self.server}/osmosis/gamm/v1beta1/pools/{pool_id}/total_pool_liquidity'
        
        r = requests.get(url=query).json()
        
        pool = dict()
        
        for coin in r['liquidity']:
            pool[coin['denom']] = int(coin['amount'])
            
        return pool
    
    
    def get_spot_price(self, pool_id, base_token, quote_token) -> float:
        query = f'{self.server}/osmosis/gamm/v1beta1/pools/{pool_id}/prices'
        
        params = {'base_asset_denom':base_token, 'quote_asset_denom':quote_token}
        
        r = requests.get(url=query, params=params).json()
        
        return float(r['spot_price'])
    
    
    # https://github.com/osmosis-labs/osmosis/blob/9f14694c49340a6f0cf1c4d4121a3547be69a501/x/poolmanager/router_test.go
    def GetAmountOut(self, pool_id, payer,amountIn,token_out) -> float: # not working
        query = f'{self.server}/osmosis/gamm/v1beta1/{pool_id}/estimate/swap_exact_amount_in'
        
        routes = [{
                  "poolId": pool_id,
                  "tokenOutDenom": token_out
                }]
                
        params = {'sender':payer,'tokenIn':str(amountIn), 'routes':routes}
        #params = {'sender':payer,'tokenIn':str(amountIn), "tokenOutDenom": token_out}
        
        r = requests.get(url=query, params=params).json()
        
        
    def get_pool_type(self, pool_id):
        query = f'{self.server}/osmosis/gamm/v1beta1/pool_type/{pool_id}'
        r = requests.get(url=query).json()
        return r['pool_type']
 
    def get_latest_block(self):
        query = f'{self.server}/cosmos/base/tendermint/v1beta1/blocks/latest'
        r = requests.get(url=query).json()
        return r
    
    def get_block(self, block):
        query = f'{self.server}/cosmos/base/tendermint/v1beta1/blocks/{block}'
        r = requests.get(url=query).json()
        return r
    
    def get_transaction(self, hash):
        query = f'{self.server}/cosmos/tx/v1beta1/txs/{hash}'
        r = requests.get(url=query).json()
        return r
        
    
    
    # send transaction
    # https://docs.osmosis.zone/api/?v=LCD#/operations/BroadcastTx
        
        
            
        
        
        
    
        
    