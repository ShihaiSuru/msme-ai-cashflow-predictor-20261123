# MSME AI Cash Flow Predictor

**AI-powered cash flow forecasting and working capital estimator for Indian MSMEs.**

Built to help founders of micro, small, and medium enterprises in India gain clear visibility into their liquidity, predict shortfalls early, and make better decisions around UPI collections, GST compliance, and working capital.

## The Problem

Indian MSMEs face chronic cash-flow volatility:

- Delayed payments from customers (often 30–90 days)
- Fragmented inflows via UPI, NEFT, cheques, and cash
- GST input credit delays and filing mismatches that lock up capital
- No simple way to forecast the next 30–60 days of cash position
- Working capital gaps that force expensive informal borrowing or missed growth opportunities

Most tools are either too complex (full accounting suites) or too generic (personal finance apps). MSME founders need a lightweight, practical system focused on *cash* rather than books.

## The Solution

This repository provides a practical starter implementation of an AI cash-flow system tailored for Indian MSMEs:

- Ingest sample or real transaction data (UPI references, bank credits/debits, invoice due dates)
- Categorize inflows vs outflows
- Generate a simple 30-day cash flow forecast
- Estimate the working capital buffer needed to avoid shortfalls
- Flag potential GST-related delays or high-risk receivables
- Output a clear summary report that a founder can act on

The current version uses rule-based logic + basic statistical forecasting (easily extensible with real ML models). It demonstrates the core idea without requiring external APIs or heavy dependencies.

## Features

- Sample Indian MSME transaction dataset included
- Cash inflow / outflow categorization (UPI collections, vendor payments, GST outflows, etc.)
- 30-day rolling cash position forecast
- Working capital requirement estimator
- Shortfall alerts with recommended actions
- Clean CLI output + JSON report

## Usage

### Prerequisites
- Python 3.8+
- No external packages required (uses only the standard library)

### Run the demo
```bash
git clone https://github.com/ShihaiSuru/msme-ai-cashflow-predictor-20261123.git
cd msme-ai-cashflow-predictor-20261123
python cashflow_predictor.py
```

The script will:
1. Load the built-in sample transactions
2. Process and categorize them
3. Generate a 30-day cash flow forecast
4. Print a founder-friendly summary and estimated working capital need

### Extend it
- Replace the sample data with real CSV exports from your bank or UPI statements
- Add OCR/invoice parsing
- Integrate Account Aggregator APIs for live bank data
- Swap the simple forecasting logic with a proper time-series or LLM-based model

## Sample Output

```
=== MSME Cash Flow Summary (Next 30 Days) ===
Starting Balance: ₹1,25,000
Expected Inflows:  ₹3,40,000
Expected Outflows: ₹2,85,000
Projected End Balance: ₹1,80,000
Minimum Projected Balance: ₹45,000

Working Capital Buffer Recommended: ₹80,000
Alerts:
- High-value receivable overdue (Invoice INV-1042)
- GST outflow scheduled on day 18
```

## Why This Matters for Indian MSMEs

Cash is the oxygen of small businesses. A 15–30 day early warning on a shortfall can mean the difference between negotiating better terms, drawing a planned credit line, or facing a crisis. This tool is designed as a practical foundation for founders building real fintech products in the MSME space.

## License

MIT License — free to use, modify, and build upon.

---

**Created for ShihaiSuru** — building practical AI cash-flow systems for Indian MSMEs.
