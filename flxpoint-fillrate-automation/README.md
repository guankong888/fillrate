# Flxpoint → Airtable Fill Rate Automation

This script pulls order/fulfillment data from Flxpoint (v2 API), calculates weekly fill rates per vendor, and pushes the results into an Airtable dashboard.

## Features
- Uses Flxpoint v2 API (`/orders`)
- Aggregates total shipped vs. ordered quantities
- Calculates fill rate as a percent
- Writes clean summaries to Airtable
- Intended to run weekly via cron or manual trigger

## Setup

1. Create a `.env` file using `.env.template`
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the script:
```bash
python flxpoint_to_airtable.py
```
