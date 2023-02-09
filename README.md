# Web3 Osmosis

## Quickstart

```python
from osmosis.main import Osmosis


server = 'https://lcd.osmosis.zone'

conn = Osmosis(server)

liquidity = conn.get_pool_liquidity(633)

t0 = list(liquidity.keys())[0]

t1 = list(liquidity.keys())[1]

spot_price = conn.get_spot_price(633,t0,t1)
```