# 🛍️ Customer Shopping Behavior Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A data analysis project exploring customer purchasing patterns, preferences, and trends to uncover actionable insights from retail shopping data.

---

## 📌 Project Overview

This project analyzes a customer shopping behavior dataset to understand:
- Who the customers are (age, gender, location)
- What they buy (category, product, purchase amount)
- How they shop (season, frequency, payment method, review ratings)
- What drives repeat purchases (discounts, promo codes, subscription status)

The goal is to practice end-to-end data analysis — from cleaning and exploration to visualization and insight generation.

---

## 📂 Dataset

| Feature | Detail |
|---|---|
| Source | [Kaggle – Customer Shopping Trends Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset) |
| Records | ~3,900 rows |
| Columns | 18 features |

**Key Columns:**
- `Customer ID`, `Age`, `Gender`, `Location`
- `Item Purchased`, `Category`, `Purchase Amount (USD)`
- `Season`, `Review Rating`, `Subscription Status`
- `Payment Method`, `Frequency of Purchases`, `Discount Applied`, `Promo Code Used`

---

## 🛠️ Tools & Libraries

- **Python** — core language
- **Pandas** — data cleaning and manipulation
- **Matplotlib / Seaborn** — data visualization
- **Jupyter Notebook** — interactive analysis environment

---

## 📊 Analysis Performed

1. **Data Cleaning** — handled missing values, corrected data types, removed duplicates
2. **Exploratory Data Analysis (EDA)**
   - Customer demographics (age distribution, gender split)
   - Top-selling categories and products
   - Purchase amount distribution
3. **Trend Analysis**
   - Seasonal purchasing patterns
   - Payment method preferences
   - Impact of discounts and promo codes on sales
4. **Customer Segmentation**
   - Purchase frequency groups
   - Subscription vs. non-subscription behavior
5. **Visualization Dashboard** — multi-panel charts summarizing key findings

---

## 📁 Project Structure

```
customer-shopping-behavior-analysis/
│
├── data/
│   └── shopping_trends.csv          # Raw dataset
│
├── notebooks/
│   └── shopping_analysis.ipynb      # Main analysis notebook
│
├── visuals/
│   └── dashboard.png                # Summary dashboard image
│
├── README.md
└── requirements.txt
```

---

## 🔍 Key Insights

- **Clothing** is the most purchased category across all seasons.
- Customers aged **25–45** account for the majority of purchases.
- **Free shipping** is the most preferred shipping type.
- **Promo code users** tend to have higher average purchase amounts.
- Purchase frequency peaks during **Fall and Winter** seasons.

> ⚠️ *Insights are based on the sample dataset and are for learning/portfolio purposes.*

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/noorthisis/customer-shopping-behavior-analysis.git
   cd customer-shopping-behavior-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open the notebook:
   ```bash
   jupyter notebook notebooks/shopping_analysis.ipynb
   ```

---

## 📦 Requirements

```
pandas
matplotlib
seaborn
jupyter
```

---

## 👩‍💻 Author

**Shabnoor**
BCA (AI & Data Science) | Graphic Era University, Dehradun
📧 shabnoorq307@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/shabnoor) | [GitHub](https://github.com/noorthisis)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
