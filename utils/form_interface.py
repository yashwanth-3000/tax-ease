import streamlit as st
import base64
import os
import requests
from dataclasses import dataclass
import logging as log

# Configure logging
log.basicConfig(level=log.INFO)

@dataclass
class FunctionInputParams:
    query_text: str = ""
    collection_name: str = "itr1"
    limit: int = 5
    prompt: str = ""

def call_api(query_text: str, collection_name: str = "itr1", limit: int = 5):
    """Make API call to the Flask backend"""
    try:
        response = requests.post(
            "http://localhost:5050/api/schedule",
            json={
                "query_text": query_text,
                "collection_name": collection_name,
                "limit": limit
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        log.error(f"API call failed: {str(e)}")
        raise Exception(f"Failed to get response from API: {str(e)}")

def display_form_interface(form_data):
    # Custom CSS
    st.markdown("""
        <style>
            .stChatMessage {
                color: #FFFFFF !important;
            }
            
            .pdf-container {
                width: 100%;
                height: 80vh;
                overflow-y: auto;
                border-radius: 8px;
                background: #2b2b2b;
                padding: 10px;
            }
            
            .chat-message {
                display: flex;
                margin: 10px 0;
            }
            
            iframe {
                width: 100%;
                height: 100%;
                border: none;
                background: white;
            }
        </style>
    """, unsafe_allow_html=True)

    st.title(form_data['name'])

    col1, col2 = st.columns(2)

    # PDF Viewer
    with col1:
        pdf_path = os.path.join('data', 'forms', 'ITR-1.pdf')
        try:
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="100%"></iframe>'
            st.markdown(f'<div class="pdf-container">{pdf_display}</div>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("PDF file not found. Please check the file path.")
        except Exception as e:
            st.error(f"Error loading PDF: {str(e)}")

    # Chat Interface
    with col2:
        chat_container = st.container()
        with chat_container:
            st.title("Chat Assistant")
            
            messages_container = st.container()
            
            # Initialize messages
            if "messages" not in st.session_state:
                st.session_state.messages = [{
                    "role": "assistant",
                    "content": """Welcome! For filing ITR-1 Sahaj, please keep these documents ready:
                    
                    • PAN Card
                    • Aadhaar Card
                    • Form 16 from your employer
                    • Bank statements
                    • Rent receipts (if claiming HRA)
                    • Investment proofs (80C, 80D)
                    • Interest certificates
                    
                    How can I help you with the form today?"""
                }]
            
            # Display messages
            with messages_container:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.write(message["content"])
            
            # Chat input
            user_input = st.chat_input("Type your message...")

            # Handle user input
            if user_input:
                # Show user message
                st.session_state.messages.append({"role": "user", "content": user_input})
                
                with st.spinner("Processing your query..."):
                    try:
                        # Call the API
                        result = call_api(
                            query_text=user_input,
                            collection_name="itr1",
                            limit=5
                        )
                        
                        if result and "result" in result and "llm_response" in result["result"]:
                            assistant_response = result["result"]["llm_response"]
                            # Add assistant response to chat
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": assistant_response
                            })
                        else:
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": "I apologize, but I couldn't process your query. Please try again."
                            })
                    except Exception as e:
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": f"An error occurred: {str(e)}. Please try again."
                        })
                        
                    st.rerun()

        # Back button
        if st.button("← Back to Forms", use_container_width=True):
            st.session_state.show_form_interface = False
            st.session_state.current_form = None
            st.session_state.messages = []
            st.rerun()

if __name__ == "__main__":
    form_data = {
        "name": "ITR-1 Sahaj Form Assistant"
    }
    
    # Start the interface
    display_form_interface(form_data)