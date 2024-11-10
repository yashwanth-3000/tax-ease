def get_custom_css():
    return """
        <style>
        /* Global Styles */
        .stApp {
            background-color: #0a0a0a;
            color: #ffffff;
        }

        /* Grid Layout */
        .stButton {
            width: 100% !important;
            margin-bottom: 1.5rem;
        }

        .stButton > button {
            width: 100% !important;
            padding: 0.75rem !important;
            border: 1px solid #ff4444 !important;
            border-radius: 4px !important;
            background-color: #222 !important;
            color: #ff4444 !important;
            cursor: pointer !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
            margin: 0 !important;
        }

        .stButton > button:hover {
            background-color: #ff4444 !important;
            color: #fff !important;
            transform: translateY(-2px);
        }

        /* Card Styles */
        .form-card {
            background: #111;
            border-radius: 10px;
            padding: 1.5rem;
            border: 1px solid #444;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            height: 100%;
            transition: 0.3s;
            color: #fff;
            position: relative;
            min-height: 380px;
            margin-bottom: 0.5rem;
        }

        .form-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 16px rgba(255, 0, 0, 0.2);
        }

        .form-card-content {
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .form-card-icon {
            font-size: 2rem;
            color: #ff4444;
            text-align: center;
            margin-bottom: 1rem;
        }

        .form-card-title {
            font-size: 1.25rem;
            font-weight: bold;
            color: #ff4444;
            margin-bottom: 0.75rem;
        }

        .form-card-description {
            color: #ddd;
            margin-bottom: 1rem;
            flex-grow: 1;
        }

        .form-card-eligibility {
            font-size: 0.875rem;
            color: #aaa;
            margin-bottom: 1rem;
            padding-top: 0.5rem;
            border-top: 1px solid #555;
        }

        /* Button Styles */
        .button-wrapper {
            width: 100%;
            margin-bottom: 1.5rem;
        }

        .fill-button {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ff4444;
            border-radius: 4px;
            background-color: #222;
            color: #ff4444;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .fill-button:hover {
            background-color: #ff4444;
            color: #fff;
            transform: translateY(-2px);
        }

        /* Special Card */
        .special-card {
            background: linear-gradient(135deg, #1a1a1a 0%, #2a2a2a 100%) !important;
            grid-column: span 2;
            text-align: center;
        }

        .special-card .form-card-content {
            align-items: center;
        }

        .special-card .form-card-title {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .special-card .form-card-description {
            font-size: 1.1rem;
            max-width: 80%;
            margin: 0 auto;
        }

        /* Hero Section */
        .hero-section {
            text-align: center;
            padding: 6rem 2rem;
            background: linear-gradient(180deg, #1a1a1a 0%, #0a0a0a 100%);
            border-radius: 10px;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }

        .hero-title {
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(255, 0, 0, 0.1);
        }

        .hero-subtitle {
            font-size: 1.5rem;
            margin-bottom: 2rem;
            color: rgba(255, 255, 255, 0.8);
        }

        .red-accent {
            color: #ff4444;
            font-weight: bold;
        }

        .hero-stats {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            color: rgba(255, 255, 255, 0.8);
        }

        /* Responsive Design */
        @media only screen and (max-width: 768px) {
            .form-card {
                min-height: 320px;
            }

            .hero-title {
                font-size: 28px;
            }

            .hero-subtitle {
                font-size: 16px;
            }

            .form-card-title {
                font-size: 18px;
            }

            .form-card-description {
                font-size: 14px;
            }

            .form-card-eligibility {
                font-size: 12px;
            }

            .fill-button {
                font-size: 12px;
                padding: 8px 16px;
            }
        }
        </style>
    """