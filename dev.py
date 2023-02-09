from osmosis.main import Osmosis


#rpc_server = 'https://osmosis-mainnet-rpc.allthatnode.com:1317'
server = 'https://lcd.osmosis.zone'

conn = Osmosis(server)

# tests for pool 633

# get pool liquidity and tokens
liquidity = conn.get_pool_liquidity(633)

# get tokens in the pool
t0 = list(liquidity.keys())[0]
t1 = list(liquidity.keys())[1]

spot_price = conn.get_spot_price(633,t0,t1)