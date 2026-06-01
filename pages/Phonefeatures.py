import streamlit as st
import pandas as pd

st.title("⚡ AI Smartphone Selector & Predictive Analyzer")
st.write("""Adjust your preferences below. Our algorithm dynamically parses hardware configurations
to calculate the ultimate device ecosystem matching your exact lifestyle parameters.""")

device_data = pd.DataFrame({
    'Company': ['Apple', 'Samsung','OnePlus', 'iQOO','Xiaomi','Realme'],
    'Min_Price': [50000,30000, 20000, 12000, 10000, 8000],
    'Max_Price': [160000, 150000,70000,65000,40000, 30000],
    'Brand_Tier': ['Tier 1 (Premium Android)','Tier 1 (Premium OS and Security)','Tier 2 (Performance)','Tier 2 (All-Rounder Variety)','Tier 2 (Gaming)','Tier 3 (Budget Value)'],
    'Value_Rating': ["⭐⭐⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐", "⭐⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐"],
    'Top_Processor_Partner': ['Apple Censor','Exynos','Snapdragon flagship','Snapdragon dimensity','MediaTek Dimensity','Snapdragon']})

filtered_brands = device_data.copy()
with st.expander("🛠 Advanced Customization Parameters", expanded=True):

    tab1, tab2 = st.tabs(["Budget and Hardware","Usage Specific Purpose"])
    with tab1:
        budget = st.slider("Select Price Range (₹)", 5000,150000, (15000, 60000), step=1000)
        battery = st.slider("Minimum Battery (mAh)", 3500, 6500, 5000, step=100)
        ram = st.select_slider("Required RAM ", options=["4 GB", "6 GB", "8 GB", ], value="8 GB")
        rom = st.selectbox("Storage Capacity (ROM)", ["64 GB", "128 GB", "256 GB"], index=1)
        
    with tab2:
        use_case = st.selectbox("Primary Usage Intent", ["Gaming Performance", "Camera", "Balanced Daily Use"])
        processor_pref = st.radio("Preferred Processor Line", ["Snapdragon flagship","MediaTek Dimensity","Apple A-Series","Exynos/Tensor", "No Preference"],index=4)
        camera_spec = st.selectbox("Rear Camera Setup Focus", [
            "50 MP + Main (OIS Enriched)", 
            "50 MP + 13 MP Dual ", 
            "50 MP + 50 MP + 2 MP wide "
        ])
        speakers = st.radio("Speaker Configuration", ["Dual Stereo Speakers (Dolby Atmos)", "Standard Mono Speaker"])


        if st.button("🚀 Analyze & Predict Best Smartphones", type="primary"):
            st.balloons()
    
            user_min_budget = budget[0]
            user_max_budget = budget[1]

            filtered_brands = device_data[
             (device_data['Min_Price'] <= user_max_budget) & 
             (device_data['Max_Price'] >= user_min_budget)   ]    
            st.subheader("🎯 AI Recommendation Engine Report")
            st.info("Targeting active price window:**₹{user_min_budget:,} - ₹{user_max_budget:,}** maximizing for **{use_case}**.")
    
            if filtered_brands.empty:
              st.warning("No brands perfectly fit this narrow financial boundary. Displaying industry baseline alternatives below.")
              filtered_brands = device_data
        
            best_match_row = filtered_brands.iloc[0]
    
    with st.status(f"✨ Top Recommended Brand Ecosystem:['Company']",expanded=True, state="complete"):
        st.write("Based on your optimization intent for **{use_case}**, devices built by **{best_match_row['Company']}** show the highest hardware compilation score within your price bracket.")
        
        stat_col1, stat_col2, stat_col3 = st.columns(3)
        with stat_col1:
         st.markdown("**Market Segment:**\n['Brand_Tier']")
            
        with stat_col2:
         st.markdown("**AI Performance Index:**\n['Value_Rating']")
        
        with stat_col3:
         st.markdown("**Recommended Silicon:**\n['Top_Processor_Partner']")
         

    st.write(" ") 
    
    st.subheader("📋 Requested Hardware")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Memory Allocation", value=ram)
    m2.metric(label="Storage Space", value=rom)
    m3.metric(label="Battery ",value=f"{battery}mAh")
    m4.metric(label="Audio Driver", value="Stereo" if "Dual" in speakers else "Mono")

    st.markdown("---")
    
    st.subheader("📊 Manufacturer  Filtering")
    st.markdown("This sorted dashboard visualizes brand hierarchy positions alongside their active price.")

    display_df = filtered_brands.copy()
    display_df['Price'] = display_df.apply(lambda r:"₹{r['Min_Price']:,} - ₹{r['Max_Price']:,}", axis=1)
    
    display_df = display_df.rename(columns={
        'Company': 'Manufacturer',
        'Brand_Tier': 'Market Classification',
        'Top_Processor_Partner': 'Primary Silicon Implementation'})
    
    st.dataframe(
        display_df[['Manufacturer','Price','Market Classification','Primary Silicon Implementation']],
        use_container_width=True,hide_index=True )

      
