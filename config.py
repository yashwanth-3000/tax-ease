# config.py
class Config:
    # App Settings
    APP_NAME = "Tax Filing Assistant"
    APP_ICON = "📊"
    
    # Environment
    ENVIRONMENT = "development"  # or "production"
    
    # Theme Colors
    THEME_PRIMARY_COLOR = "#1a1a1a"
    THEME_SECONDARY_COLOR = "#2d2d2d"
    THEME_ACCENT_COLOR = "#4CAF50"
    THEME_TEXT_COLOR = "#ffffff"
    
    # Grid Layout
    GRID_COLUMNS = 3
    GRID_SPACING = "1rem"
    
    # Form Categories
    FORM_CATEGORIES = [
        "Income Tax",
        "Business Tax",
        "Property Tax",
        "Sales Tax",
        "Other Forms"
    ]
    
    # Search Settings
    SEARCH_MIN_CHARS = 2
    
    # Development Settings
    DEBUG = True
    MOCK_DATA = True