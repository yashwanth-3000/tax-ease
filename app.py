import streamlit as st
import os
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.styles import get_custom_css
from utils.data import FormData
from config import Config

def init_session_state():
    """Initialize session state variables"""
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ""
    if 'filter_tax_info' not in st.session_state:
        st.session_state.filter_tax_info = None  # None means no filter applied

def create_hero_section():
    """Create the hero section of the application with reduced size"""
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

def display_buttons_for_filter():
    """Display buttons below the search bar to filter forms"""
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Income Tax Form"):
            st.session_state.filter_tax_info = "income_tax"
            st.rerun()  # Refresh the page to apply the filter
    with col2:
        if st.button("Income Tax Returns"):
            st.session_state.filter_tax_info = "income_return"
            st.rerun()  # Refresh the page to apply the filter

def display_form_grid(forms):
    """Display a 3x3 grid of forms"""
    # Apply the search filter based on tax_info (income_tax or income_return)
    filtered_forms = FormData.search_forms(st.session_state.search_query, forms)

    if st.session_state.filter_tax_info:
        filtered_forms = [form for form in filtered_forms if form.get("tax_info") == st.session_state.filter_tax_info]

    if not filtered_forms:
        st.info("No forms found matching your search criteria.")
        return

    # Limit the forms to 9 for a 3x3 grid
    filtered_forms = filtered_forms[:9]

    # Organize forms into a 3x3 grid layout
    rows = [filtered_forms[i:i+3] for i in range(0, len(filtered_forms), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for col, form in zip(cols, row):
            with col:
                st.markdown(f"""
                    <div class="form-card">
                        <div class="form-card-icon">{form['icon']}</div>
                        <h3 class="form-card-title">{form['name']}</h3>
                        <p class="form-card-description">{form['description']}</p>
                        <div class="form-card-eligibility">
                            <span style="color: #ff4444;">▸</span> Eligibility: {form['eligibility']}
                        </div>
                        <div class="card-buttons">
                            <button 
                                class="card-button" 
                                onclick="parent.postMessage({{action: 'fill', formId: '{form['id']}'}}, '*')"
                            >Fill Form</button>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    # Close grid container
    st.markdown('</div>', unsafe_allow_html=True)

def main():
    """Main application entry point"""
    st.set_page_config(
        page_title=Config.APP_NAME,
        page_icon=Config.APP_ICON,
        layout="wide"
    )
    
    # Initialize session state
    init_session_state()
    
    # Apply custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    # Create hero section
    create_hero_section()

    # Create search bar and display buttons below it
    create_search_bar()
    display_buttons_for_filter()  # Buttons to filter by tax info

    # Get forms and display them
    forms = FormData.get_sample_forms()
    display_form_grid(forms)

if __name__ == "__main__":
    main()
