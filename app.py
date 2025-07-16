import streamlit as st
import wikipedia

def get_wiki_summary(query):
    try:
        summary = wikipedia.summary(query, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many options found. Try something more specific. Suggestions:\n{e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for your query."

st.title("📚 Wikipedia Knowledge Chatbot")
st.write("Ask me anything. I’ll find an answer from Wikipedia!")

user_input = st.text_input("Type your question:")

if user_input:
    st.markdown(f"**You asked:** {user_input}")
    response = get_wiki_summary(user_input)
    st.markdown(f"**🤖 Answer:** {response}")
