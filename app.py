import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Live GPS Location Fetch", page_icon="📍", layout="centered")

st.title("📍 Live GPS Location Fetch (No Database)")
st.caption("Button dabao → Browser me location allow karo → Coordinates mil jayenge")

# ---------------- GPS SCRIPT ----------------
st.markdown("""
<script>
function getLocation(){
  navigator.geolocation.getCurrentPosition(
    function(pos){
      const params = new URLSearchParams(window.location.search);
      params.set("lat", pos.coords.latitude);
      params.set("lon", pos.coords.longitude);
      window.location.search = params.toString();
    },
    function(err){
      alert("Location denied. Please allow GPS access in browser settings.");
      console.log(err);
    }
  );
}
</script>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("### 👉 Step 1: Click the button to fetch your live GPS location")
st.markdown('<button onclick="getLocation()" style="padding:10px 16px; font-size:16px;">📍 Get My Live Location</button>', unsafe_allow_html=True)

st.divider()

# ---------------- READ QUERY PARAMS ----------------
params = st.query_params

lat = params.get("lat")
lon = params.get("lon")

if lat and lon:
    try:
        lat = float(lat)
        lon = float(lon)

        st.success("✅ Live GPS Coordinates Fetched")

        # Big visible block (copy-friendly)
        st.markdown("### 📌 Your Current Coordinates")
        st.code(f"Latitude:  {lat}\nLongitude: {lon}", language="text")

        # Nice metrics
        c1, c2, c3 = st.columns(3)
        c1.metric("Latitude", f"{lat:.6f}")
        c2.metric("Longitude", f"{lon:.6f}")
        c3.metric("Status", "GPS Active")

        # Last updated
        st.caption(f"🕒 Last Updated: {datetime.now().strftime('%d %b %Y, %I:%M:%S %p')}")

        # Map
        st.map([{"lat": lat, "lon": lon}])

    except Exception as e:
        st.error("❌ Invalid GPS values received.")
        st.exception(e)
else:
    st.warning("📡 GPS not fetched yet. Click the button above and allow location permission.")

# ---------------- REFRESH ----------------
if st.button("🔄 Refresh Location"):
    st.query_params.clear()
    st.rerun()
