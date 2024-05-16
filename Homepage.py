import streamlit as st


st.set_page_config(
    page_title="AEC Bot",
    page_icon="🏝️",
)
header = st.container()
with header:
    st.title('Island Chatbot')
    st.info('Hi I am SEPI a virtual assistant for AEC professionals')
# st.image('team.jpeg', caption='Team Island 2024', width=600)
# st.sidebar.success('select a page above.')


# Footer
st.markdown(
    """
    ---
    Made with ❤️ by [Ashish](https://ashu-a.github.io/ashish_ranjan/)
    """
)
