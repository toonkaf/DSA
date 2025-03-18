"""Coin Exchange V2"""
import json
def exchanges(amount: int,coins: dict):
    print(f"Amount: {amount}")
    types = sorted(coins, key = lambda x:int(x),reverse=True)
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_usage = [{coin: 0 for coin in types} for _ in range(amount + 1)]
    
    for i in range(1, amount + 1):
        for coin in types:
            if int(coin) <= i and coin_usage[i - int(coin)][coin] < coins[coin]:
                temp_usage = coin_usage[i - int(coin)].copy()
                temp_usage[coin] += 1
                if dp[i - int(coin)] + 1 < dp[i]:
                    dp[i], coin_usage[i] = dp[i - int(coin)] + 1, temp_usage
    
    if dp[amount] == float('inf'):
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total = sum(coin_usage[amount].values())
        for coin in types:
            print(f"  {coin} baht = {coin_usage[amount][coin]} coins")
        print(f"Number of coins: {total}")

exchanges(int(input()),json.loads(input()))
