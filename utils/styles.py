# utils/styles.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import Config

def get_custom_css():
    return f"""
        <style>
        /* Global Styles */
        .stApp {{
            background-color: {Config.THEME_PRIMARY_COLOR};
            color: {Config.THEME_TEXT_COLOR};
        }}

        /* Hero Section */
        .hero-section {{
            text-align: center;
            padding: 6rem 2rem;
            background: linear-gradient(180deg, {Config.THEME_SECONDARY_COLOR} 0%, {Config.THEME_PRIMARY_COLOR} 100%);
            border-radius: 10px;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }}
        .hero-section::before, .hero-section::after {{
            content: '';
            position: absolute;
            width: 100px;
            height: 100px;
            background: rgba(255, 0, 0, 0.1);
        }}
        .hero-section::before {{
            top: 0; right: 0;
            clip-path: polygon(100% 0, 0 0, 100% 100%);
        }}
        .hero-section::after {{
            bottom: 0; left: 0;
            clip-path: polygon(0 0, 0 100%, 100% 100%);
        }}
        .hero-title {{
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: {Config.THEME_TEXT_COLOR};
            text-shadow: 2px 2px 4px rgba(255, 0, 0, 0.1);
        }}
        .hero-subtitle {{
            font-size: 1.5rem;
            margin-bottom: 2rem;
            color: {Config.THEME_TEXT_COLOR}cc;
        }}
        .red-accent {{ color: #ff4444; font-weight: bold; }}

        .hero-stats {{
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: {Config.THEME_TEXT_COLOR}cc;
        }}

        /* Hero Buttons */
        .hero-buttons {{
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 2rem;
        }}
        .hero-buttons button {{
            background-color: #fff;
            color: #ff4444;
            font-size: 16px;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 200px;
            margin: 0 10px;
            transition: background-color 0.3s ease;
        }}
        .hero-buttons button:hover {{
            background-color: #ffcc00;
            color: white;
        }}

        /* Custom Button Styles */
        .custom-button {{
            background-color: {Config.THEME_SECONDARY_COLOR};
            color: {Config.THEME_TEXT_COLOR};
            padding: 0.75rem 1.5rem;
            border: 1px solid #ff4444;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }}
        .custom-button:hover {{
            box-shadow: 0 0 15px rgba(255, 68, 68, 0.3);
            transform: translateY(-2px);
        }}

        /* Form Grid */
        .form-grid-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            padding: 1rem;
            margin: 1rem 0;
        }}
        .form-card {{
            background: #111; /* Black background */
            border-radius: 10px;
            padding: 1.5rem;
            border: 1px solid #444; /* Dark gray border */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Stronger shadow for black theme */
            display: flex;
            flex-direction: column;
            height: 100%;
            transition: 0.3s;
            color: #fff; /* White text for readability */
        }}
        .form-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 16px rgba(255, 0, 0, 0.2); /* Red accent shadow on hover */
        }}
        .form-card-icon {{ font-size: 2rem; color: #ff4444; text-align: center; margin-bottom: 1rem; }}
        .form-card-title {{ font-size: 1.25rem; font-weight: bold; color: #ff4444; margin-bottom: 0.75rem; }}
        .form-card-description {{ color: #ddd; margin-bottom: 1rem; }}
        .form-card-eligibility {{
            font-size: 0.875rem;
            color: #aaa;
            margin-bottom: 1rem;
            padding-top: 0.5rem;
            border-top: 1px solid #555;
        }}

        /* Card Buttons */
        .card-buttons {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.75rem;
            margin-top: auto;
        }}
        .card-button {{
            padding: 0.5rem;
            border: 1px solid #ff4444;
            border-radius: 4px;
            background: #222;
            color: #ff4444;
            cursor: pointer;
            font-weight: 500;
            transition: 0.3s;
        }}
        .card-button:hover {{
            background: #ff4444;
            border-color: #ff4444;
            color: #fff;
            transform: translateY(-2px);
        }}

        /* Form Styling */
        .form-container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 2rem;
            background: #111; /* Black background */
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            color: #fff; /* White text for readability */
        }}
        .form-label {{
            font-size: 1rem;
            color: #ff4444; /* Red labels */
            margin-bottom: 0.5rem;
            display: block;
            font-weight: 600;
        }}
        .form-input {{
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #444;
            background-color: #222;
            font-size: 1rem;
            color: #fff;
            transition: border 0.3s;
        }}
        .form-input:focus {{
            border-color: #ff4444;
            outline: none;
            background-color: #333;
        }}
        .form-textarea {{
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #444;
            background-color: #222;
            font-size: 1rem;
            color: #fff;
            resize: vertical;
            transition: border 0.3s;
        }}
        .form-textarea:focus {{
            border-color: #ff4444;
            outline: none;
            background-color: #333;
        }}
        .form-submit {{
            padding: 0.75rem 1.5rem;
            background-color: #ff4444; /* Red submit button */
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            transition: background-color 0.3s;
        }}
        .form-submit:hover {{
            background-color: #cc0000; /* Darker red on hover */
        }}

        /* General Styling */
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}

        /* Column Layout */
        .stColumn {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}

        .stColumn .stButton {{
            margin: 10px;
        }}

        /* Responsive Design */
        @media only screen and (max-width: 768px) {{
            .form-grid-container {{
                grid-template-columns: 1fr 1fr;
            }}

            .hero-title {{
                font-size: 28px;
            }}

            .hero-subtitle {{
                font-size: 16px;
            }}

            .hero-buttons button {{
                width: 150px;
                font-size: 14px;
            }}

            .form-card-title {{
                font-size: 18px;
            }}

            .form-card-description {{
                font-size: 14px;
            }}

            .form-card-eligibility {{
                font-size: 12px;
            }}

            .card-button {{
                font-size: 12px;
                padding: 8px 16px;
            }}
        }}
        </style>
    """
