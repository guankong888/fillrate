import os
from dotenv import load_dotenv
from utils.flxpoint_client import get_recent_orders
from utils.airtable_client import upsert_fill_rate
from collections import defaultdict
from datetime import datetime

load_dotenv()

def calculate_fill_rates(orders):
    stats = defaultdict(lambda: {"ordered": 0, "shipped": 0})

    for order in orders:
        vendor = order.get("source", {}).get("name") or "UNKNOWN"
        for item in order.get("line_items", []):
            ordered = item.get("quantity", 0)
            shipped = item.get("shipped_quantity", 0)
            stats[vendor]["ordered"] += ordered
            stats[vendor]["shipped"] += shipped

    return stats

def main():
    print("Fetching Flxpoint data...")
    orders = get_recent_orders()
    stats = calculate_fill_rates(orders)

    week_str = datetime.now().strftime("%Y-%m-%d")

    print("Pushing to Airtable...")
    for vendor, values in stats.items():
        ordered = values["ordered"]
        shipped = values["shipped"]
        fill_rate = round((shipped / ordered), 4) if ordered else 0
        upsert_fill_rate(vendor, ordered, shipped, fill_rate, week_str)
        print(f"{vendor}: {fill_rate*100:.1f}% ({shipped}/{ordered})")

if __name__ == "__main__":
    main()
