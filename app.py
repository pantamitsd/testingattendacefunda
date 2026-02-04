import streamlit as st

st.set_page_config(page_title="Live GPS Location Fetch", page_icon="📍")

st.title("📍 Live GPS Location Fetch (No Database)")

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

    st.code(f"Latitude: {lat}\nLongitude: {lon}", language="text")
    st.map([{"lat": lat, "lon": lon}])

else:
    st.warning("📡 GPS not fetched yet. Click the button above and allow location permission.")
