# utils/questionnaire.py

def get_questionnaire_content():
    """Returns the questions and options for the ITR questionnaire"""
    return {
        'questions': [
            {
                'id': 'income',
                'text': 'What is your total annual income?',
                'options': [
                    {'value': 1, 'label': 'Less than Rs. 50 Lakh'},
                    {'value': 2, 'label': 'More than Rs. 50 Lakh'}
                ]
            },
            {
                'id': 'income_source',
                'text': 'What are your sources of income?',
                'options': [
                    {'value': 1, 'label': 'Only salary and one house property'},
                    {'value': 2, 'label': 'Business/Professional income'},
                    {'value': 3, 'label': 'Multiple sources including foreign income'},
                    {'value': 4, 'label': 'Presumptive business income'}
                ]
            },
            {
                'id': 'status',
                'text': 'Which of these best describes your status?',
                'options': [
                    {'value': 1, 'label': 'Individual resident Indian'},
                    {'value': 2, 'label': 'Company/Corporate entity'},
                    {'value': 3, 'label': 'Charitable/Religious trust'},
                    {'value': 4, 'label': 'Partnership firm/LLP'}
                ]
            }
        ]
    }

def determine_itr(income, income_source, status):
    """Determines the appropriate ITR form based on user responses"""
    # If status is not individual
    if status == 2:
        return "ITR-6", "For Companies"
    elif status == 3:
        return "ITR-7", "For Charitable/Religious Trusts"
    elif status == 4:
        return "ITR-5", "For Partnership Firms/LLPs"
    
    # For individuals (status == 1)
    if income == 1 and income_source == 1:
        return "ITR-1", "Sahaj - For individuals with salary income and one house property"
    elif income_source == 2:
        return "ITR-3", "For individuals with business/professional income"
    elif income_source == 3:
        return "ITR-2", "For individuals with multiple sources including foreign income"
    elif income == 1 and income_source == 4:
        return "ITR-4", "Sugam - For individuals with presumptive business income"
    else:
        return "ITR-2", "For individuals with complex income sources"