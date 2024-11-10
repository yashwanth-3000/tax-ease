import streamlit as st
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.styles import get_custom_css
from utils.data import FormData
from utils.questionnaire import get_questionnaire_content, determine_itr
from config import Config

def init_session_state():
    """Initialize session state variables"""
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""
    if 'filter_tax_info' not in st.session_state:
        st.session_state.filter_tax_info = None
    if 'show_questionnaire' not in st.session_state:
        st.session_state.show_questionnaire = False
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False

def create_hero_section():
    """Create the hero section of the application"""
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Simplifying Your <span class="red-accent">Tax</span> Filing Journey</h1>
            <p class="hero-subtitle">Navigate through your tax forms with ease and confidence</p>
            <div class="hero-stats">
                <span class="red-accent">✓</span> Quick Filing 
                <span class="red-accent">•</span> 
                <span class="red-accent">✓</span> Expert Guidance 
                <span class="red-accent">•</span> 
                <span class="red-accent">✓</span> Secure Process
            </div>
        </div>
    """, unsafe_allow_html=True)

def create_search_bar():
    """Create the search bar below the hero section"""
    return st.text_input(
        "Search forms...", 
        key="search_query",
        placeholder="Enter form name, description, or category"
    )

def display_questionnaire():
    """Display the ITR form determination questionnaire"""
    if not st.session_state.show_questionnaire:
        return

    st.markdown("""
        <div class="questionnaire-container">
            <h2>ITR Form Determination Questionnaire</h2>
        </div>
    """, unsafe_allow_html=True)

    questions = get_questionnaire_content()['questions']
    
    if st.session_state.show_result:
        form_type, description = determine_itr(
            st.session_state.answers['income'],
            st.session_state.answers['income_source'],
            st.session_state.answers['status']
        )
        
        st.success(f"Based on your responses, you should file: {form_type}")
        st.info(f"Description: {description}")
        
        if st.button("Start Over"):
            st.session_state.show_questionnaire = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.session_state.show_result = False
            st.rerun()
            
        return

    current_q = questions[st.session_state.current_question]
    st.write(f"### {current_q['text']}")
    
    answer = st.radio(
        "Select your answer:",
        options=range(len(current_q['options'])),
        format_func=lambda x: current_q['options'][x]['label'],
        key=f"q_{current_q['id']}"
    )

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Back", disabled=st.session_state.current_question == 0):
            st.session_state.current_question -= 1
            st.rerun()

    with col2:
        if st.button("Next" if st.session_state.current_question < len(questions)-1 else "Submit"):
            st.session_state.answers[current_q['id']] = current_q['options'][answer]['value']
            
            if st.session_state.current_question < len(questions)-1:
                st.session_state.current_question += 1
            else:
                st.session_state.show_result = True
            st.rerun()

def display_form_grid(forms):
    """Display a grid of forms with a special card"""
    if st.session_state.show_questionnaire:
        display_questionnaire()
        return

    filtered_forms = FormData.search_forms(st.session_state.search_query, forms)

    if st.session_state.filter_tax_info:
        filtered_forms = [form for form in filtered_forms if form.get("tax_info") == st.session_state.filter_tax_info]

    if not filtered_forms:
        st.info("No forms found matching your search criteria.")
        return

    total_forms = len(filtered_forms)

    # Create columns for the grid layout
    cols = st.columns(3)
    
    # Display regular form cards
    for i in range(min(total_forms, 7)):
        with cols[i % 3]:
            st.markdown(f"""
                <div class="form-card">
                    <div class="form-card-content">
                        <div class="form-card-icon">{filtered_forms[i]['icon']}</div>
                        <h3 class="form-card-title">{filtered_forms[i]['name']}</h3>
                        <p class="form-card-description">{filtered_forms[i]['description']}</p>
                        <div class="form-card-eligibility">
                            <span style="color: #ff4444;">▸</span> Eligibility: {filtered_forms[i]['eligibility']}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Button below the card
            st.markdown(f"""
                <div class="button-wrapper">
                    <button class="fill-button" onclick="parent.postMessage({{action: 'fill', formId: '{filtered_forms[i]['id']}'}}, '*')">
                        Fill {filtered_forms[i]['name']}
                    </button>
                </div>
            """, unsafe_allow_html=True)
    
    # Add special card if we have exactly 7 forms
    if total_forms == 7:
        # Take the last two columns for the special card
        with cols[1]:
            st.markdown("""
                <div class="form-card special-card">
                    <div class="form-card-content">
                        <div class="form-card-icon">❓</div>
                        <h3 class="form-card-title">Need Help Choosing?</h3>
                        <p class="form-card-description">
                            Don't know which income tax return form to fill? 
                            Answer these simple questions to find out!
                        </p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Button for questionnaire
            if st.button("Start Questionnaire", key="start_questionnaire", type="primary", use_container_width=True):
                st.session_state.show_questionnaire = True
                st.rerun()

def main():
    """Main application entry point"""
    st.set_page_config(
        page_title=Config.APP_NAME,
        page_icon=Config.APP_ICON,
        layout="wide"
    )
    
    init_session_state()
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    create_hero_section()
    
    if not st.session_state.show_questionnaire:
        create_search_bar()
    
    forms = FormData.get_sample_forms()
    display_form_grid(forms)

if __name__ == "__main__":
    main()