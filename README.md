# Smart Order Router (SOR)

A modular Smart Order Routing engine for real-time equities trading across multiple venues (IBKR, Lime). Supports TWAP, VWAP, and OFI-based execution.

## Components
- Databento MBP-10 Feed Integration
- Order Book Builder (L1/L2)
- Order Flow Imbalance (OFI) Calculation
- Strategy Engine (TWAP, VWAP)
- Risk Management & Order Execution
- Kafka Integration for Live Streaming
- FIX-based Adapters for IBKR & Lime

## Running Locally
```bash
python main.py
