# Reflection

**What I got wrong at the start:**

At first, I thought Deepak Mahato needs a machine learning model to predict tomato demand. I also assumed that running out of stock early was his biggest problem. But after checking his 24 days notebook from Adityapur Market, I understood that 24 rows are not enough for using ML. I also found that spoiled tomatoes cost him almost 3 times more per kg compared to missing some late evening sales.

**What I would cut:**

If I do this again, I would not focus too much on profit margin and daily price changes in the beginning. I will mainly focus on how much tomatoes he purchase and how much gets wasted daily. Adding too many columns and complex calculations makes it difficult for a small vendor who has to make buying decisions at 5 AM in the morning.

**Where AI helped:**

AI helped me in cleaning the raw CSV data, finding duplicate entries and applying the Newsvendor critical ratio formula using Python. It also helped to handle incorrect or missing rows so the code does not crash.

**Where AI wasted time:**

Initially AI suggested some general templates and complicated inventory logic which was not really suitable for a roadside tomato seller. His buying process is different as he purchases crates from the morning mandi. So I had to simplify the whole approach and focus on giving just one clear number which can help him decide how much to buy.