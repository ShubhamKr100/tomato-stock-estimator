# Daily Tomato Stock Estimator

## The Tool
This is a lightweight Python script designed for Deepak Mahato, a vegetable vendor at Adityapur Market. It uses historical sales and wastage data to recommend an optimal wholesale purchase quantity using the Newsvendor Inventory Model.

## How to Run It
1. Ensure you have Python installed.
2. Ensure `pandas` is installed (`pip install pandas`).
3. Keep `data.csv` in the same directory as the script.
4. Run the command: `python script.py`

## Real Output
When run on the 24-day dataset, the script outputs:
```text
==================================================
🍅 DEEPAK's DAILY TOMATO STOCK CALCULATOR 🍅
==================================================
Average Profit per KG sold: ₹10.46
Average Loss per KG wasted: ₹31.58
--------------------------------------------------
Because throwing away a tomato hurts 3.0x more than
missing a sale, you should stock slightly LESS than average.
--------------------------------------------------
Historical Average Daily Sale: 33.0 kg
👉 OPTIMAL ORDER QUANTITY FOR TOMORROW: 31 kg 👈
==================================================