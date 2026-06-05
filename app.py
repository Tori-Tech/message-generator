from huggingface_hub import InferenceClient
import streamlit as st

st.set_page_config(page_title="Message Generator")

# Hide the Github links, header, and footer for privacy
st.markdown(
    """
    <style>
    /* Hide the default top decoration, menus, headers, and footers */
    #stDecoration {display:none !important; visibility:hidden !important;}
    .stDeployButton {display:none !important; visibility:hidden !important;}
    #MainMenu {display:none !important; visibility:hidden !important;}
    header {display:none !important; visibility:hidden !important;}
    footer {display:none !important; visibility:hidden !important;}
    
    /* Aggressive blanket ban on the Viewer/Profile Badge and its container */
    [data-testid="stViewerBadge"],
    [data-testid="stStatusWidget"],
    .stViewerBadge,
    iframe[title="viewer-badge"],
    div[class*="viewerBadge"],
    span[class*="viewerBadge"],
    a[class*="viewerBadge"],
    [class*="viewerBadge_container"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
        width: 0px !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }
    
    /* Close up the gap at the top of the page */
    .block-container {padding-top: 2rem !important;}
    </style>
    """,
    unsafe_allow_html=True
)

#Initialize Hugging Face client

client = InferenceClient(api_key=st.secrets["HF_TOKEN"])


#Passphrase check to protect the app from random people

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("Restricted Access")
    user_password = st.text_input("Enter the passphrase to unlock the app:", type="password")

    if st.button("Unlock"):
        if user_password == st.secrets["APP_PASSWORD"]:
            st.session_state["authenticated"] = True  
            st.rerun()
        else:
            st.error("Incorrect passphrase. Access denied.")
else:

    #Main code
    st.title("AI Message Generator")
    st.write("Just tell the AI what you want it to output.")


    #Context input goes here
    intent = st.text_area("What should this message say?", placeholder="e.g., I would like to politely tell a person that their performance is very poor.")

    recipient = st.text_input("Who is this going to?", placeholder="e.g., Steve, the IT guy.")

    if st.button("Generate Message"):

        if intent:

            with st.spinner("Generating message...."):
                #defining system prompt
                system_instruction = (
                    "You are an expert corporate communications assistant. Your job is to rewrite user prompts into highly professional, polite emails or messages. Crucially, you must heavily lean into flattery, corporate jargon, and endless well-wishing (e.g., 'I hope this email finds you well,','Thank you for your invaluable leadership,', 'It is always a pleasure collaborating with you'). Make the recipient look amazing while keeping the core message clear."
                )


            #Call the model
            

            messages = [
                {"role": "system", "content": "You are an expert corporate communications assistant. Your job is to generate messages based on the user prompts. Messages should be highly professional and polite. Heavily lean into flattery, corporate jargon, and endless well-wishing. However, all messages must be concise, no longer than six sentences. Make the recipient look amazing."},
                {"role": "user", "content": f"Recipient: {recipient}\nCore Message: {intent}\n\nPolished Message:"}
            ]

            completion = client.chat.completions.create(
                model="meta-llama/Meta-Llama-3-8B-Instruct", 
                messages=messages, 
                max_tokens=500,
                temperature=0.3
            )

            # Extract the text from the new response format
            response = completion.choices[0].message.content


            st.success("Here is your message:")
            st.text_area("Copy this:", value=response, height=250)
        else:
            st.warning("Please type what you want to say first!")
