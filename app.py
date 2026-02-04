import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Live GPS Location Fetch", page_icon="📍")

st.title("📍 Live GPS Location Fetch (No Database)")

# ---- Browser GPS Script ----
st.components.v1.html("""
<script>
navigator.geolocation.getCurrentPosition(
    (pos) => {
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;

        const url = new URL(window.location);
        url.searchParams.set("lat", lat);
        url.searchParams.set("lon", lon);

        window.location.replace(url.toString());
    },
    (err) => {
        alert("Location permission denied. Please allow GPS access.");
        console.log(err);
    }
);
</script>
""", height=0)

# ---- Read Query Params ----
params = st.query_params
lat = params.get("lat")
lon = params.get("lon")

if lat and lon:
    lat = float(lat)
    lon = float(lon)

    st.success("✅ GPS Active – Live Coordinates Fetched")

    # ---- Big visible text (copy-friendly) ----
    st.markdown("### 📌 Current Coordinates (Copyable)")
    st.code(f"Latitude:  {lat}\nLongitude: {lon}", language="text")

    # ---- Metrics Row ----
    col1, col2, col3 = st.columns(3)
    col1.metric("Latitude", lat)
    col2.metric("Longitude", lon)
    col3.metric("Status", "GPS Active")

    # ---- Last Updated Time ----
    st.caption(f"🕒 Last Updated: {datetime.now().strftime('%d %b %Y, %I:%M:%S %p')}")

    # ---- Map View ----
    st.map([{"lat": lat, "lon": lon}])

else:
    st.warning("📡 Fetching live GPS location... Please allow browser location permission.")
    st.info("Agar popup aaye to **Allow Location Access** zaroor karna.")

# ---- Manual Refresh Button ----
if st.button("🔄 Refresh Location"):
    st.query_params.clear()
    st.rerun()
