# Fieldwork & Data Collection

## 1. Location & Time
* **Place:** Deepak Mahato's Vegetable Stall, Adityapur Market (walking distance from NIT Jamshedpur)
* **Date & Time:** November 17, 2026, 6:00 PM – 6:34 PM (on-site observation and vendor interview)
* **Photographic Evidence:**
  * **Photo 1 (`17-NOV-2026, 6:00 PM`):** 
    ![Stall Setup at 6:00 PM]![Evening stall setup showing fresh tomato crates alongside other vegetables before the peak rush.](<WhatsApp Image 2026-11-17 at 6.40.49 PM (1).jpg>) 
  * **Photo 2 (`17-NOV-2026, 6:34 PM`):**
    ![Evening Rush at 6:34 PM]![ Active evening customer rush and remaining tomato inventory in the crate.](<WhatsApp Image 2026-11-17 at 6.40.48 PM (1).jpg>)

      * **Photo 3 (`17-NOV-2026, 6:34 PM`):**  
![Close-up of the crates showing the high volume of unsold tomatoes still left amidst the evening crowd.](<../cv/pjt/WhatsApp Image 2026-11-17 at 6.40.49 PM.jpeg>)


  * **Photo 4 (`17-NOV-2026, 6:34 PM`):**  
![Wide shot of the stall location capturing the heavy footfall and customers making purchases.](<WhatsApp Image 2026-11-17 at 6.40.48 PM (1).jpeg>)
## 2. Conversation with the Vendor
* **Name:** Deepak Mahato
* **Role:** Roadside Vegetable Stall Owner (Adityapur Market)
 
**3 Things He Said:**
1. *"If I buy too much, the tomatoes become soft by the next afternoon and nobody buys them at full price—I have to throw them away or sell them at a steep loss."*
2. *"During festivals, people buy large quantities even when the price jumps, whereas around weddings, customers often ask me to bring extra stock and then buy less—leaving me with unsold tomatoes that rot the next day."*
3. *"The wholesale mandi price changes every single morning, so I usually just look at yesterday's sales and guess how many crates to buy, sometimes facing a loss even on slow normal days."*

**1 Thing That Surprised Me:**
I initially assumed running out of stock early was his biggest problem and that higher prices always reduce sales. However, talking to Deepak and checking his numbers surprised me in two ways: first, during the recent festival, customers bought heavily (45–46 kg on Nov 14–15) even when prices jumped to ₹46–₹51/kg; second, **overstocking hurts him nearly 3x more than understocking**—every unsold spoiled kilogram (especially after cancelled wedding bulk expectations or slow normal days) costs him ₹26–₹43 in lost wholesale capital, whereas running out early only costs him ₹8–₹15 per kg in missed profit margin.

## 3. Data Collection Note
* **Source:** Physical pocket diary kept by Deepak Mahato in his cash box, covering 24 days from **25-Oct-2026 to 17-Nov-2026**.
* **How It Was Recorded:** During my visit on November 17, 2026, I transcribed his daily handwritten entries—wholesale purchase quantity (`purchased_kg`), wholesale cost (`purchase_price_rs_per_kg`), retail selling rate (`selling_price_rs_per_kg`), and end-of-day spoiled tomatoes (`wasted_kg`)—into `data.csv`.
* **Derived Columns:** `sold_kg` was calculated as `purchased_kg - wasted_kg`, and `estimated_profit_rs` reflects net daily profit after accounting for the wholesale cost of wasted stock.