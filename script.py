import pandas as pd

def calculate_optimal_stock(csv_file):
    # 1. Read the historical data
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: Could not find {csv_file}")
        return

    # 2. Calculate average costs and margins
    avg_margin = df['margin_rs_per_kg'].mean()
    avg_loss_per_wasted_kg = df['purchase_price_rs_per_kg'].mean()

    # 3. Apply the Newsvendor Model formula
    # Critical Ratio = Cost of Understocking / (Cost of Understocking + Cost of Overstocking)
    # Cost of understocking = missed profit (margin)
    # Cost of overstocking = wasted capital (purchase price)
    
 
    cost_understock = avg_margin
    cost_overstock = avg_loss_per_wasted_kg
    
    critical_ratio = cost_understock / (cost_understock + cost_overstock)
    
    # 4. Find the optimal quantity based on historical demand distribution
    optimal_qty = df['sold_kg'].quantile(critical_ratio)

    # 5. Print the recommendation clearly for the user
    print("==================================================")
    print("🍅 DEEPAK's DAILY TOMATO STOCK CALCULATOR 🍅")
    print("==================================================")
    print(f"Average Profit per KG sold: ₹{avg_margin:.2f}")
    print(f"Average Loss per KG wasted: ₹{avg_loss_per_wasted_kg:.2f}")
    print("--------------------------------------------------")
    print(f"Because throwing away a tomato hurts {cost_overstock/cost_understock:.1f}x more than")
    print("missing a sale, you should stock slightly LESS than average.")
    print("--------------------------------------------------")
    print(f"Historical Average Daily Sale: {df['sold_kg'].mean():.1f} kg")
    print(f"👉 OPTIMAL ORDER QUANTITY FOR TOMORROW: {round(optimal_qty)} kg 👈")
    print("==================================================")

if __name__ == "__main__":
    calculate_optimal_stock('data.csv')