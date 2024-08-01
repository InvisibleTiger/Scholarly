from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
timer = load_lottiefile("pages/assets/timer.json")
st_lottie(timer, speed=1, reverse=False, loop=True, quality="low", height=None, width=None, key=None)