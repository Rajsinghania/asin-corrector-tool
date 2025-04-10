import streamlit as st
import pandas as pd
from datetime import datetime

st.title("CSV Column Updater with ASIN Matching")

# File uploader
main_file = st.file_uploader("Upload your main CSV file", type="csv")

# Detect and reload if a new file is uploaded
if main_file:
    # Save the uploaded file timestamp
    if 'last_uploaded_filename' not in st.session_state or st.session_state.last_uploaded_filename != main_file.name:
        st.session_state.main_df = pd.read_csv(main_file)
        st.session_state.last_uploaded_filename = main_file.name
        st.success(f"New file '{main_file.name}' uploaded successfully!")

# Proceed only if DataFrame is loaded
if 'main_df' in st.session_state:
    main_df = st.session_state.main_df

    st.write("Main File Preview:")
    st.write(main_df.head())

    # Validate columns
    if 'asin' not in main_df.columns or 'marketplace' not in main_df.columns or 'correctedLabel' not in main_df.columns:
        st.error("The CSV must contain 'asin', 'marketplace', and 'correctedLabel' columns.")
    else:
        # User Inputs
        asin_input = st.text_area("Enter ASIN IDs (separated by new lines)")
        country_id = st.text_input("Enter Marketplace ID")
        update_text = st.text_input("Enter text to update in 'correctedLabel'")

        if st.button("Update Column"):
            if asin_input and country_id and update_text:
                asin_list = [x.strip() for x in asin_input.split('\n') if x.strip()]
                condition = (main_df['asin'].isin(asin_list)) & (main_df['marketplace'].astype(str) == country_id)

                st.session_state.main_df.loc[condition, 'correctedLabel'] = update_text
                st.success(f"Updated {condition.sum()} row(s).")

                st.write("Updated Preview:")
                st.write(st.session_state.main_df.head())
            else:
                st.error("Please enter all the required fields.")

        # Download button
        csv = st.session_state.main_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Full Updated CSV",
            data=csv,
            file_name='fully_updated_file.csv',
            mime='text/csv'
        )
