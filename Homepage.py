import streamlit as st


st.set_page_config(
    page_title="AEC Bot",
    page_icon="🏝️",
)
header = st.container()
with header:
    st.title('AEC Chatbot')
    st.info('Hi I am SEPI a virtual assistant for AEC professionals')
    st.write("Welcome to the AEC Chatbot FAQ section. Here you'll find answers to common questions and instructions on how to use our services.")
faq_expander = st.expander("How to create a speckle token?")
with faq_expander:
    st.write("""
    To add a model on Speckle, follow these steps:
    1. Log into your Speckle account and go to your profile page at /profile..
    2. Scroll down to the "Your Apps" section to see your personal access tokens.
    3. Click the "New Token" button. A dialog box will appear.
    4. Enter a memorable token name and set the token scopes.
    5. Create the token. The dialog will display the token once. Copy it and store it securely.
    For more visit [Speckle](https://speckle.guide/dev/tokens.html)
    """)
# Footer
st.markdown(
    """
    ---
    Made with ❤️ by [Ashish](https://ashu-a.github.io/ashish_ranjan/)
    """
)
