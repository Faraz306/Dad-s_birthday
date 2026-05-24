from streamlit_confetti import confetti
import streamlit as st
from streamlit_extras.let_it_rain import rain

# Page Configuration
st.set_page_config(page_title="Happy Birthday, Dad!", page_icon="🎉")

# FIX: Using the native st.header with a built-in colorful divider line!
# You can use "rainbow", "red", "orange", "yellow", "green", "blue", "violet", or "gray"
st.header("🥳 Happy Birthday, Dad! 🥳", divider="rainbow")

# Create a clean side-by-side layout
st.success("🎉 Happy Birthday to you dad!")
st.info("💡 **Dad's Special Day Reminder:** Time to eat cake and relax!")

# Audio Control
st.subheader("🎵 Listen to your Birthday Track")
st.video('Faraz.mp3', autoplay=True)

# Full-Width Greeting Card
st.success("🎂 Happy birthday to you, Happy birthday to you, Happy Birthday to you, Dad, Happy Birthday to you!")

# Maximum Particle Decorations!
st.balloons()    # Floating native balloons
rain("🥳")       # Shower of falling emojis

# This shoots falling birthday emojis over the whole screen
rain(
    emoji="🎂",
    font_size=54,       # Adjust size of the birthday cakes
    falling_speed=4,    # Speed of the animation
    animation_length="short" # "short" bursts once, "infinite" keeps raining
)
