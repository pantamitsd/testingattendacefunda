import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Live GPS Location Fetch", page_icon="📍")

st.title("📍 Live GPS Location Fetch (No Database)")
st.caption("Tip: Button dabao → Browser me location allow karo")

st.markdown("### 👉 Click the button to fetch your live GPS location")

# ---- Button trigger ----
clicked = st.button("📍 Get My Live Location")

if clicked:
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

    st.success("✅ Live GPS Coordinates Fetched")

    # Big visible, copy-friendly block
    st.markdown("### 📌 Your Current Coordinates")
    st.code(f"Latitude:  {lat}\nLongitude: {lon}", language="text")

    # Nice metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Latitude", f"{lat:.6f}")
    c2.metric("Longitude", f"{lon:.6f}")
    c3.metric("Status", "GPS Active")

    # Last updated
    st.caption(f"🕒 Last Updated: {datetime.now().strftime('%d %b %Y, %I:%M:%S %p')}")

    # Map view
    st.map([{"lat": lat, "lon": lon}])

else:
    st.warning("📡 GPS not fetched yet. Click the button above and allow location permission.")

# ---- Optional Refresh Button ----
if st.button("🔄 Refresh Location"):
    st.query_params.clear()
    st.rerun()
