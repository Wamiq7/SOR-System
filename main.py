from market_data.databento_stream import start_market_data
from engine.strategy_engine import StrategyEngine
from engine.risk_manager import RiskManager

def main():
    print("Starting Smart Order Router...")
    start_market_data()
    strategy = StrategyEngine()
    strategy.run()
    # Execution + Risk logic would be plugged here

if __name__ == "__main__":
    main()
