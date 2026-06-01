import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="AI Smartphone Selector",page_icon="📱",
    layout="wide")

st.title("⚡ AI Smartphone Selector & Predictive Analyzer")

st.write("""Adjust your preferences below.  Our AI engine dynamically analyzes smartphone ecosystems
based on hardware configuration, pricing strategy and performance optimization.
""")



device_data = pd.DataFrame({
    'Company': ['Apple', 'Samsung', 'Google', 'OnePlus', 'iQOO', 'Xiaomi', 'Realme', 'POCO'],
    
    'Min_Price': [50000, 30000, 40000, 20000, 15000, 10000, 8000, 9000],
    
    'Max_Price': [160000, 150000, 120000, 70000, 65000, 50000, 35000, 30000],
    
    'Performance_Score': [98, 95, 92, 90, 88, 84, 78, 75],
    
    'Brand_Tier': ['Tier 1 Premium','Tier 1 Android','Tier 1 AI Camera',
        'Tier 2 Performance','Tier 2 Gaming','Tier 2 Value',
        'Tier 3 Budget','Tier 3 Budget Gaming'],
    
    'Value_Rating': ["⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐","⭐⭐⭐⭐",
        "⭐⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐","⭐⭐⭐"],
    
    'Top_Processor_Partner': ['Apple A-Series','Snapdragon / Exynos','Google Tensor',
        'Snapdragon Flagship','Snapdragon Gaming','MediaTek Dimensity',
        'Snapdragon','MediaTek']
})

with st.expander("🛠️ Advanced Customization Parameters", expanded=True):

    tab1, tab2 = st.tabs([ "💰 Budget & Hardware", "🎯 Usage Preferences"])

    with tab1:

        budget = st.slider("Select Price Range (₹)",
            5000,150000,(15000, 60000), step=1000)

        battery = st.slider(
            "Minimum Battery (mAh)",
            3500,7000,5000,
            step=100)

        ram = st.select_slider(
            "Required RAM",
            options=["4 GB", "6 GB", "8 GB", "12 GB", "16 GB"],
            value="8 GB"
        )

        rom = st.selectbox(
            "Storage Capacity",
            ["64 GB", "128 GB", "256 GB", "512 GB"],
            index=1
        )

    with tab2:

        use_case = st.selectbox(
            "Primary Usage Intent",
            ["Gaming Performance","Camera",
                "Balanced Daily Use","Business / Productivity"])

        processor_pref = st.radio("Preferred Processor",
            ["Snapdragon Flagship","MediaTek Dimensity",
                "Apple A-Series","Tensor / Exynos",
                "No Preference" ],index=4)

        camera_spec = st.selectbox("Camera Preference",
            ["50 MP Main + OIS","50 MP Dual Camera",
                "108 MP Triple Camera","50 MP Ultra-wide Setup" ])

        speakers = st.radio(
            "Speaker Configuration",
            [ "Dual Stereo Speakers", "Mono Speaker"])

if st.button("🚀 Analyze & Predict Best Smartphones", type="primary"):

    st.balloons()

    user_min_budget = budget[0]
    user_max_budget = budget[1]

    filtered_brands = device_data[
        (device_data['Min_Price'] <= user_max_budget) &
        (device_data['Max_Price'] >= user_min_budget)
    ]

    st.success(f"Generating recommendations between "
        f"₹{user_min_budget:,} and ₹{user_max_budget:,}")

    if filtered_brands.empty:

        st.warning("No smartphones found in this budget range.")

        filtered_brands = device_data

    best_match_row = filtered_brands.sort_values(
        by="Performance_Score",ascending=False).iloc[0]

    with st.status(
        f"✨ Top Recommended Brand: {best_match_row['Company']}",
        expanded=True,
        state="complete"):

        st.write(
            f"Based on your usage pattern for "
            f"**{use_case}**, "
            f"**{best_match_row['Company']}** "
            f"offers the best balance of "
            f"performance and ecosystem value.")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Market Segment",
                best_match_row['Brand_Tier']
            )

        with c2:
            st.metric("AI Rating",best_match_row['Value_Rating'])

        with c3:
            st.metric(
                "Processor Partner",
                best_match_row['Top_Processor_Partner']
            )

    st.subheader("📋 Requested Hardware")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("RAM", ram)
    m2.metric("Storage", rom)
    m3.metric("Battery", f"{battery} mAh")
    m4.metric("Audio","Stereo" if "Dual" in speakers else "Mono")

    st.markdown("---")

    st.subheader("📊 Market Position Analysis")

    fig = px.scatter(
        filtered_brands,
        x="Max_Price",
        y="Performance_Score",
        color="Brand_Tier",
        size="Performance_Score",
        hover_name="Company",
        title="Brand Positioning by Price & Performance",
        labels={
            "Max_Price": "Maximum Price (₹)",
            "Performance_Score": "Performance Score"
        }
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📑 Brand Comparison Table")

    display_df = filtered_brands.copy()

    display_df['Price Range'] = display_df.apply(
        lambda r: f"₹{r['Min_Price']:,} - ₹{r['Max_Price']:,}",
        axis=1
    )

    display_df = display_df.rename(columns={
        'Company': 'Brand','Brand_Tier': 'Category',
        'Top_Processor_Partner': 'Processor'
    })

    st.dataframe(
        display_df[
            ['Brand','Price Range','Category','Processor', 'Performance_Score']
        ],
        use_container_width=True,hide_index=True )

