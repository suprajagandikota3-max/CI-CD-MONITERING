import streamlit as st
import wikipedia

st.set_page_config(page_title="📚 Wikipedia Chatbot", page_icon="🤖")
st.title("📚 Wikipedia Chatbot")

# Small credit line under title
st.markdown("<h6 style='text-italian: center; color: pink;'>🍂 Created by honey </h6>", unsafe_allow_html=True)


# Add background color using CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #blue; /* Change this code to blue color */
}

[data-testid="stHeader"] {
    background-color: red(0,0,0,0); /* Make header transparent */
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""


# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_wikipedia_summary(query):
    try:
        # Search for pages matching the query
        results = wikipedia.search(query)
        if not results:
            return "Sorry, I couldn't find anything on that topic."

        # Get summary of the top result (limit to 2 sentences)
        summary = wikipedia.summary(
            results[0], sentences=2, auto_suggest=False, redirect=True
        )
        return summary
    except wikipedia.DisambiguationError as e:
        return f"Your query is ambiguous, did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.PageError:
        return "Sorry, I couldn't find a page matching your query."
    except Exception:
        return "Oops, something went wrong."

# User input box at the bottom
if user_input := st.chat_input("Ask me anything about Wikipedia..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get Wikipedia response
    bot_response = get_wikipedia_summary(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Button to delete chat
if st.button("🗑️ delete Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
