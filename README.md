# ASIN Marketplace Label Updater 🧠

This is a Streamlit-based tool for updating ASIN product labels based on the marketplace ID.

## 🛠 How It Works

1. Upload a CSV file containing at least these columns:
   - `asin`
   - `marketplace`
   - `correctedLabel`
2. Enter a list of ASINs and a marketplace ID.
3. Provide the value to update in the `correctedLabel` column.
4. Click "Update Now" — matching rows are updated.
5. Download the updated file.

## 🔧 Setup Locally

```bash
pip install streamlit pandas
streamlit run app.py
