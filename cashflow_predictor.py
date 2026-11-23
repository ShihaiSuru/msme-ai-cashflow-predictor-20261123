#!/usr/bin/env python3
"""
MSME AI Cash Flow Predictor
A practical starter tool for Indian MSMEs to forecast cash position
and estimate working capital needs from transaction data.

Focus areas: UPI collections, delayed receivables, GST outflows, vendor payments.
Uses only Python standard library for easy demo and extension.
"""

from datetime import datetime, timedelta
from collections import defaultdict
import json

# ---------------------------------------------------------------------------
# Sample Indian MSME transaction data
# In a real system this would come from bank statements, UPI exports,
# or Account Aggregator APIs. Amounts in INR.
# ---------------------------------------------------------------------------
SAMPLE_TRANSACTIONS = [
    {"date": "2026-11-01", "type": "inflow", "amount": 85000, "category": "UPI Collection", "note": "Customer payment - Retail"},
    {"date": "2026-11-03", "type": "outflow", "amount": 42000, "category": "Vendor Payment", "note": "Raw material supplier"},
    {"date": "2026-11-05", "type": "inflow", "amount": 120000, "category": "Invoice Receipt", "note": "INV-1041 settled"},
    {"date": "2026-11-08", "type": "outflow", "amount": 18500, "category": "GST Payment", "note": "GSTR-3B outflow"},
    {"date": "2026-11-10", "type": "inflow", "amount": 65000, "category": "UPI Collection", "note": "Multiple small UPI"},
    {"date": "2026-11-12", "type": "outflow", "amount": 35000, "category": "Vendor Payment", "note": "Logistics"},
    {"date": "2026-11-15", "type": "inflow", "amount": 95000, "category": "Invoice Receipt", "note": "INV-1043 partial"},
    {"date": "2026-11-18", "type": "outflow", "amount": 22000, "category": "GST Payment", "note": "Input tax adjustment"},
    {"date": "2026-11-20", "type": "outflow", "amount": 48000, "category": "Vendor Payment", "note": "Packaging"},
    {"date": "2026-11-22", "type": "inflow", "amount": 110000, "category": "UPI Collection", "note": "Festival sales peak"},
]

STARTING_BALANCE = 125000  # INR


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d")


def categorize_and_aggregate(transactions):
    """Group transactions by day and type for forecasting."""
    daily = defaultdict(lambda: {"inflow": 0, "outflow": 0})
    for tx in transactions:
        day = parse_date(tx["date"]).date()
        daily[day][tx["type"]] += tx["amount"]
    return daily


def generate_forecast(daily_data, starting_balance, days=30):
    """
    Simple rolling cash position forecast.
    In production this would use time-series models or LLM reasoning
    over historical patterns + pending invoices.
    """
    today = datetime(2026, 11, 23).date()
    forecast = []
    balance = starting_balance
    min_balance = starting_balance

    # Project forward using average daily net from sample (simplified)
    total_in = sum(d["inflow"] for d in daily_data.values())
    total_out = sum(d["outflow"] for d in daily_data.values())
    avg_daily_net = (total_in - total_out) / max(len(daily_data), 1)

    for i in range(days):
        current_day = today + timedelta(days=i)
        # Apply average + any known scheduled items (placeholder logic)
        net = avg_daily_net
        if i == 18:  # Example GST day
            net -= 20000
        balance += net
        min_balance = min(min_balance, balance)
        forecast.append({
            "date": current_day.isoformat(),
            "projected_balance": round(balance, 2),
            "net_change": round(net, 2)
        })

    return forecast, min_balance


def estimate_working_capital(min_balance, starting_balance):
    """Recommend a buffer so the business never drops below a safe floor."""
    safe_floor = starting_balance * 0.4  # 40% of current as minimum comfort
    shortfall = max(0, safe_floor - min_balance)
    buffer = shortfall + 30000  # extra cushion for MSME volatility
    return round(buffer)


def generate_alerts(transactions, forecast):
    alerts = []
    # Flag high-value or delayed items (simplified)
    for tx in transactions:
        if tx["type"] == "inflow" and tx["amount"] > 80000 and "INV" in tx["note"]:
            alerts.append(f"Monitor receivable: {tx['note']} (₹{tx['amount']:,})")
    alerts.append("GST outflow expected around day 18 of forecast period")
    if any(f["projected_balance"] < 50000 for f in forecast[:15]):
        alerts.append("Potential shortfall within first 15 days — review collections")
    return alerts


def main():
    print("=" * 55)
    print("  MSME AI Cash Flow Predictor — Demo")
    print("  For Indian Micro, Small & Medium Enterprises")
    print("=" * 55)

    daily = categorize_and_aggregate(SAMPLE_TRANSACTIONS)
    forecast, min_balance = generate_forecast(daily, STARTING_BALANCE)
    wc_need = estimate_working_capital(min_balance, STARTING_BALANCE)
    alerts = generate_alerts(SAMPLE_TRANSACTIONS, forecast)

    total_in = sum(tx["amount"] for tx in SAMPLE_TRANSACTIONS if tx["type"] == "inflow")
    total_out = sum(tx["amount"] for tx in SAMPLE_TRANSACTIONS if tx["type"] == "outflow")

    print(f"\nStarting Balance:     ₹{STARTING_BALANCE:,}")
    print(f"Sample Period Inflows:  ₹{total_in:,}")
    print(f"Sample Period Outflows: ₹{total_out:,}")
    print(f"\n--- 30-Day Forecast ---")
    print(f"Projected End Balance:  ₹{forecast[-1]['projected_balance']:,.0f}")
    print(f"Minimum Balance Seen:   ₹{min_balance:,.0f}")
    print(f"\nRecommended Working Capital Buffer: ₹{wc_need:,}")

    print("\nAlerts:")
    for a in alerts:
        print(f"  • {a}")

    # Also write a JSON report for further use
    report = {
        "starting_balance": STARTING_BALANCE,
        "projected_end_balance": forecast[-1]["projected_balance"],
        "min_projected_balance": min_balance,
        "working_capital_recommended": wc_need,
        "alerts": alerts,
        "forecast_sample": forecast[:5]  # first 5 days
    }
    with open("cashflow_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nDetailed report saved to cashflow_report.json")
    print("\nThis is a starter demo. Extend with real bank/UPI data, pending invoices,")
    print("and ML models for production use in MSME fintech products.")


if __name__ == "__main__":
    main()
