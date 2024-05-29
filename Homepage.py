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
    To create Speckle Token, follow these steps:
    1. Log into your Speckle account and go to your profile page at /profile..
    2. Scroll down to the "Your Apps" section to see your personal access tokens.
    3. Click the "New Token" button. A dialog box will appear.
    4. Enter a memorable token name and set the token scopes.
    5. Create the token. The dialog will display the token once. Copy it and store it securely.
    For more visit [Speckle](https://speckle.guide/dev/tokens.html)
    """)

faq_expander = st.expander("How to Use the PDF Chat Page?")
with faq_expander:
    st.write("""
    1. Go to the PDF Chat option in the sidebar.
    2. In the sidebar, use the "Browse File" option to select the documents you want to add.
    3. After selecting the documents, click the "Process" button.
    4. Wait for the loader to stop. This may take some time.
    5. Once the loader stops, you can start adding your prompt to get data from the SEPI.
    """)
faq_expander = st.expander("How to View the Model?")
with faq_expander:
    st.write("""
    1. First, enter your Speckle token.
    2. A dropdown will appear with all the Speckle streams connected to your token. Select your preferred Speckle stream from the dropdown.
    3. Another dropdown will appear with all the branches of the selected stream. Choose the branch you want to view.
    4. SEPI will now display the model based on your selections.
    """)

faq_expander = st.expander("How to Extract Data and Chat with It?")
with faq_expander:
    st.write("""
    1. Input your Speckle token.
    2. Choose your desired Speckle stream from the dropdown.
    3. Pick the branch from which you want to extract data.
    4. Choose the main category, select parameters, and click "Run".
    5. Download the extracted data in Excel format.
    6. Enter your query in the query box and click "Send" to get insights from the data.
    """)

# Footer
st.markdown(
    """
    ---
    Made with ❤️ by [Ashish](https://ashu-a.github.io/Ashish_portfolio/)
    """
)
