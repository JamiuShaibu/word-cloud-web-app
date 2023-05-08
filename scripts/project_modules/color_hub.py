import streamlit as st


@st.cache_resource(show_spinner=False)
def get_image_colors() -> list[str]:
    """Returns sorted list of colors"""
    colors = ["Red", "Green", "Blue", "Yellow", "Navy", "Black", "White", "Brown", "Orange", "Gray",
              "Pink", "Purple", "Silver", "Olive", "Maroon", "Teal", "Coral", "Cyan", "Azure",
              "Indigo", "Tan", "Gold", "wheat", "Violet", "Turquoise", "Beige", "IndianRed",
              "LightCoral", "DarkRed", "Crimson", "LightSalmon", "MediumVioletRed", "Tomato", "OrangeRed",
              "DarkKhaki", "Khaki", "RebeccaPurple", "RoyalBlue", "DarkSlateBlue", "DarkMagenta",
              "Lavender", "Thistle", "LawnGreen", "MediumAquamarine", "DarkOliveGreen", "GreenYellow",
              "SteelBlue", "SaddleBrown", "RosyBrown", "DimGray", "CornflowerBlue", "Chocolate", "DarkOrange",
              "DarkSlateGray", "DarkSeaGreen", "FireBrick", "HotPink", "MediumBlue", "MidnightBlue",
              "PaleVioletRed"]
    colors.sort()
    return colors
