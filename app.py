import pyshorteners
import streamlit as st

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    return short_url

def main():
    """
    Main function for the URL Shortener app.

    This function creates a simple Streamlit app that allows users to input a long URL and get a shortened version of it.
    The app displays a title, a text input field for the URL, and a button to trigger the URL shortening process.
    If the input URL is valid and the button is pressed, the shortened URL is displayed; otherwise, an informational message is shown.

    Returns:
        None
    """
    st.set_page_config(page_title="URL Shortener App")
    st.title("URL Shortener")
    st.text("This app shortens URLs using the TinyURL service")
    long_url = st.text_input("Enter the URL", key="long_url_input")
    if st.button(label="Shorten"):
        if long_url != "":
            short_url = shorten_url(long_url)
            st.success(f"Shortened URL: {short_url}")
        else:    
            st.info("Please enter a URL to shorten")

if __name__ == "__main__":
    main()
