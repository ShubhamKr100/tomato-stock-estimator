# Research: Daily Tomato Stock & Wastage Estimator

## The Problem
1. Deepak Mahato runs an open-air vegetable stall at Adityapur Market near NIT Jamshedpur, buying fresh tomatoes every morning from the wholesale mandi based purely on guesswork.
2. Because tomatoes spoil rapidly without cold storage, overestimating demand leads to unsold stock, costing him ₹30–₹34 per kg in lost capital.
3. Conversely, underestimating demand causes early stockouts, forfeiting ₹8–₹15 per kg in missed evening sales profit.
4. This lack of a data-driven balance causes his daily profit to fluctuate wildly between ₹72 and ₹535.
5. He needs a lightweight tool that uses his past sales records to recommend an optimal daily purchase quantity before he leaves for the morning market.

## Existing Solutions & Why They Don't Fit
1. **Commercial Retail POS & Inventory Apps (e.g., Vyapar, Zoho Inventory):**
   These tools are designed for packaged retail shops with barcode scanners, SKU catalogs, and digital invoicing. At a fast-moving open-air vegetable stall where loose tomatoes are weighed in polybags and prices change every morning, entering every sale into an app is too slow, complex, and expensive.
2. **Manual Spreadsheets (Excel / Google Sheets):**
   While spreadsheets can track daily purchases and wastage, Deepak does not own a laptop and leaves for the wholesale market around 5:00 AM. He needs a zero-setup, single-command calculation that works immediately from his daily log rather than building or maintaining formulas himself.

## Sources Read
1. **"The Newsvendor Problem: Balancing Overstock and Understock Costs" (Operations Research Basics)**
   * This article explains how to calculate the optimal order quantity for perishable goods by comparing the exact cost of overstocking against the cost of understocking.
   * It helped me realize that Deepak doesn't need to perfectly predict daily demand, but rather find the "critical ratio" of his financial risk.
   * I will use the mathematical logic from this model in my Python script to find his optimal purchase weight.

2. **"Why B2B Tech Fails in India's Unorganized Retail" (Business Case Study on Micro-entrepreneurs)**
   * This piece highlighted why complex dashboards fail for street vendors due to high cognitive load, lack of time, and hardware limitations.
   * It validated my decision to avoid making an "app" and instead build a backend script that just outputs one actionable number.
   * It guided the design constraint: the final tool must output a single sentence answer that can just be told or texted to Deepak.