import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="CI/CD Monitor", layout="wide")
st.title("🚀 CI/CD Pipeline Monitor")

# Pipeline status
if st.button("Check Pipeline Status"):
    try:
        # Check app health
        health = requests.get("https://your-app.elasticbeanstalk.com/", timeout=10)
        st.metric("App Status", "✅ Healthy" if health.status_code == 200 else "❌ Down")
        
        # Simple metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Last Check", datetime.now().strftime("%H:%M:%S"))
        col2.metric("Response Time", f"{health.elapsed.total_seconds():.2f}s")
        col3.metric("Status Code", health.status_code)
        
    except:
        st.error("❌ Application is unreachable")

st.info("Pipeline runs automatically on every git push!")
