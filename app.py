import streamlit as st

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

# ---- Read Query Params (Latest Streamlit) ----
params = st.query_params
lat = params.get("lat")
lon = params.get("lon")

if lat and lon:
    lat = float(lat)
    lon = float(lon)

    st.success("✅ Live GPS Coordinates Fetched Successfully")

    col1, col2 = st.columns(2)
    col1.metric("Latitude", lat)
    col2.metric("Longitude", lon)

    st.map([{"lat": lat, "lon": lon}])

else:
    st.warning("📡 Fetching live GPS location... Please allow browser location permission.")
    st.info("Agar popup aaye to **Allow Location Access** zaroor karna.")

# ---- Optional Refresh Button ----
if st.button("🔄 Refresh Location"):
    st.query_params.clear()
    st.rerun()
