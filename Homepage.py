import streamlit as st


st.set_page_config(
    page_title="AEC Bot",
    page_icon="🏝️",
)
header = st.container()
with header:
    st.title('Island Chatbot')
    st.info('Hi I am SEPI a virtual assistant for AEC professionals')

# Footer
st.markdown(
    """
    ---
    Made with ❤️ by [Ashish](https://ashu-a.github.io/ashish_ranjan/)
    """
)
