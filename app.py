from datetime import date, timedelta
import streamlit as st

from wanderwise.data import DESTINATIONS, INTERESTS, PACES, PARTIES, BUDGET_STYLES
from wanderwise.planner import build_trip
from wanderwise.pdf_export import create_itinerary_pdf
from wanderwise.utils import format_inr

st.set_page_config(
    page_title="WanderWise | Smart Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.block-container { padding-top: 1.4rem; padding-bottom: 3rem; max-width: 1280px; }
.hero { padding: 2rem 2.2rem; border-radius: 22px; color: white;
        background: linear-gradient(120deg, #11243d 0%, #176b87 58%, #36a6a0 100%); margin-bottom: 1.4rem; }
.hero h1 { color: white; font-family: 'Manrope', sans-serif; font-size: 2.25rem; margin: 0; }
.hero p { color: #e5f4f7; font-size: 1.02rem; margin: .55rem 0 0; }
.metric-card { background: #f5f8fb; border: 1px solid #e3eaf1; border-radius: 15px; padding: 1rem; min-height: 100px; }
.metric-label { color: #536578; font-size: .84rem; margin-bottom: .3rem; }
.metric-value { color: #14283d; font-size: 1.45rem; font-weight: 800; }
.section-title { font-family: 'Manrope', sans-serif; color: #13283e; font-size: 1.3rem; font-weight: 800; }
div[data-testid="stSidebar"] { background: #f4f7fa; }
.stButton > button, .stDownloadButton > button { border-radius: 10px; font-weight: 700; min-height: 2.65rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✈️ WanderWise")
    st.caption("Smart Travel Itinerary Planner")
    st.markdown("---")
    destination = st.selectbox("Destination", list(DESTINATIONS), index=2)
    start_date = st.date_input(
        "Trip start date",
        value=date.today() + timedelta(days=14),
        min_value=date.today(),
    )
    days = st.slider("Trip duration", min_value=1, max_value=14, value=3)
    party = st.selectbox("Travel party", PARTIES, index=1)
    pace = st.selectbox("Travel pace", PACES, index=1)
    budget_style = st.selectbox("Budget style", BUDGET_STYLES, index=1)
    interests = st.multiselect("Interests", INTERESTS, default=["History & culture", "Food"])
    generate = st.button("✨ Generate my trip", type="primary", use_container_width=True)
    st.markdown("---")
    st.caption("Demo mode · No API key required")
    st.caption("All prices are estimates; no bookings are made.")

# Generate initially and whenever the user explicitly requests a refreshed plan.
if "trip" not in st.session_state:
    st.session_state.trip = None
if generate or st.session_state.trip is None:
    st.session_state.trip = build_trip(
        destination=destination,
        start_date=start_date,
        days=days,
        party=party,
        pace=pace,
        interests=interests,
        budget_style=budget_style,
    )

trip = st.session_state.trip

st.markdown("""
<div class="hero">
  <h1>Make every trip memorable.</h1>
  <p>A personalized day-by-day itinerary, a practical budget, and a travel guide you can take anywhere.</p>
</div>
""", unsafe_allow_html=True)

# Keep the selected controls and displayed plan in sync.
if trip["destination"] != destination or trip["start_date"] != start_date or trip["days"] != days:
    st.info("Your trip settings have changed. Select **Generate my trip** to update the itinerary.")
st.markdown(f"### Your trip to {trip['destination']}")
st.markdown(
    f"<span style='color:#65778a'>{DESTINATIONS[trip['destination']]['region']} · "
    f"{trip['days']} day(s) · {trip['party']} · {trip['pace']}</span>",
    unsafe_allow_html=True,
)

c1, c2, c3, c4 = st.columns(4)
metrics = [
    (c1, "Duration", f"{trip['days']} days"),
    (c2, "Travel style", trip["budget_style"]),
    (c3, "Interests", str(len(trip["interests"]))),
    (c4, "Estimated total", format_inr(trip["total"])),
]
for col, label, value in metrics:
    col.markdown(
        f"<div class='metric-card'><div class='metric-label'>{label}</div>"
        f"<div class='metric-value'>{value}</div></div>",
        unsafe_allow_html=True,
    )

st.markdown("")
tab_itinerary, tab_budget, tab_tips = st.tabs(
    ["🗓️ Itinerary", "💰 Budget breakdown", "🧭 Travel tips"]
)

with tab_itinerary:
    st.markdown("<div class='section-title'>Your day-by-day itinerary</div>", unsafe_allow_html=True)
    st.caption("Your plan adapts to the destination, travel pace, interests, and trip duration.")
    for day in trip["itinerary"]:
        with st.container(border=True):
            st.markdown(f"#### Day {day['day']} · {day['date']}")
            cols = st.columns(3)
            for idx, (period, description) in enumerate(day["plan"]):
                with cols[idx]:
                    st.markdown(f"**{period}**")
                    st.write(description)
    st.info("Before leaving, verify attraction opening hours, local transit, weather, and travel advisories.")

with tab_budget:
    st.markdown("<div class='section-title'>Estimated trip budget</div>", unsafe_allow_html=True)
    st.caption("Illustrative estimates in INR. Actual costs depend on season, booking choices, and travel origin.")
    for category, amount in trip["costs"].items():
        left, right = st.columns([3, 1])
        left.write(category)
        right.markdown(f"**{format_inr(amount)}**")
    st.divider()
    st.markdown(f"### Estimated total: {format_inr(trip['total'])}")
    st.caption("Includes lodging, food, activities, local transport, and estimated travel to/from the destination.")

with tab_tips:
    st.markdown("<div class='section-title'>Before you go</div>", unsafe_allow_html=True)
    for tip in [
        "Confirm hotel check-in/check-out times and cancellation policies.",
        "Check the weather forecast and pack suitable clothing.",
        "Keep digital and offline copies of identification, tickets, and reservations.",
        "Verify attraction opening days, entry fees, and any required permits.",
        "Keep emergency contacts and contingency money available.",
        "For adventure activities, use licensed operators and follow local safety guidance.",
    ]:
        st.markdown(f"- {tip}")
    st.warning("WanderWise is a planning demo. It does not provide live prices or make reservations.")

pdf_bytes = create_itinerary_pdf(trip)
st.markdown("---")
left, right = st.columns([2, 1])
with left:
    st.markdown("### Take your plan with you")
    st.write("Export your itinerary and estimated budget as a formatted PDF travel guide.")
with right:
    st.download_button(
        "⬇️ Download travel guide (PDF)",
        data=pdf_bytes,
        file_name=f"WanderWise_{trip['destination'].replace(' ', '_')}_Itinerary.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
st.caption("WanderWise · Final-year student project · Python + Streamlit")
