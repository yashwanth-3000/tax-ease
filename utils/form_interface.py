import streamlit as st
import base64
import os

def display_form_interface(form_data):
    # Custom CSS for the interface
    st.markdown("""
        <style>
            /* Make message text brighter */
            .stChatMessage {
                color: #FFFFFF !important;
            }
            
            /* PDF container style */
            .pdf-container {
                width: 100%;
                height: 80vh;
                overflow-y: auto;
                border-radius: 8px;
                background: #2b2b2b;
                padding: 10px;
            }
            
            /* Chat message styling */
            .chat-message {
                display: flex;
                margin: 10px 0;
            }
            
            /* Ensure iframe takes full width */
            iframe {
                width: 100%;
                height: 100%;
                border: none;
                background: white;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.title(form_data['name'])

    # Create two columns
    col1, col2 = st.columns(2)

    # Left column - Scrollable PDF Viewer
    with col1:
        # Use os.path.join to handle file paths correctly across platforms
        pdf_path = os.path.join('data', 'forms', 'ITR-1.pdf')  # Replace with your specific path
        try:
            with open(pdf_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            # Embed PDF using base64
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="100%"></iframe>'
            st.markdown(f'<div class="pdf-container">{pdf_display}</div>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.error("PDF file not found. Please check the file path.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Right column - Chat Interface
    with col2:
        chat_container = st.container()
        with chat_container:
            st.title("Chat Assistant")
            
            # Create a fixed height box for messages
            messages_container = st.container()
            
            # Initialize messages if not exists
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
            
            # Chat input should be defined before messages display
            user_input = st.chat_input("Type your message...")
            
            # Display messages in a scrollable container
            with messages_container:
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.write(message["content"])

            # Handle user input
            if user_input:
                # Add user message
                st.session_state.messages.append({"role": "user", "content": user_input})
                # Add assistant response
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": f"I'll help you with filling {form_data['name']}. What specific field do you need help with?"
                })
                st.rerun()

        # Back button
        if st.button("← Back to Forms", use_container_width=True):
            st.session_state.show_form_interface = False
            st.session_state.current_form = None
            st.session_state.messages = []
            st.rerun()
