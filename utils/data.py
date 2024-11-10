class FormData:
    @staticmethod
    def get_sample_forms():
        """Return sample tax forms data with additional fields like website_url and tax_info"""
        return [
            #income tax return forms - ITR
            {
                "id": "ITR-1",
                "name": "ITR-1 Sahaj",
                "icon": "📝",
                "description": "For individuals with income up to Rs. 50 Lakh from salary, pension, one house property, and other sources (excluding winning from lottery).",
                "eligibility": "Ordinary residents with income up to Rs.50 Lakh, from salary, pension, one house property, and agricultural income up to Rs.5,000",
                "ineligibility": "Non-residents, HUF, individuals with income over Rs.50 Lakh, foreign income, or directorship in companies",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-2",
                "name": "ITR-2",
                "icon": "📄",
                "description": "For individuals and HUFs with income exceeding Rs. 50 Lakh, including from salary, capital gains, foreign assets, and agricultural income over Rs. 5,000.",
                "eligibility": "Non-resident Indians, residents, and HUFs with income over Rs. 50 Lakh, or foreign income",
                "ineligibility": "Individuals or HUFs with business or professional income",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-3",
                "name": "ITR-3",
                "icon": "🏢",
                "description": "For individuals and HUFs with income from business or profession, including being a partner in a firm.",
                "eligibility": "Individuals and HUFs with business or professional income, partners in a firm",
                "ineligibility": "Individuals or HUFs without commercial or professional income",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-4",
                "name": "ITR-4 Sugam",
                "icon": "💼",
                "description": "For individuals, HUFs, and firms with income up to Rs. 50 Lakh from business or profession on a presumptive basis (excluding LLPs).",
                "eligibility": "Individuals, HUFs, and firms with presumptive income up to Rs.50 Lakh, excluding LLPs",
                "ineligibility": "Individuals with income over Rs.50 Lakh, agricultural income above Rs.5,000, or directorship in companies",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-5",
                "name": "ITR-5",
                "icon": "📜",
                "description": "For firms, LLPs, AOPs, BOIs, co-operatives, local authorities, and other entities except individuals or HUFs.",
                "eligibility": "Firms, LLPs, AOPs, BOIs, co-operatives, and other eligible entities",
                "ineligibility": "Individuals, HUFs, or entities filing ITR-7",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-6",
                "name": "ITR-6",
                "icon": "🏦",
                "description": "For companies excluding those claiming exemption under Section 11 (income from religious or charitable purposes).",
                "eligibility": "Companies registered under the Companies Act except those exempt under Section 11",
                "ineligibility": "Charitable/religious entities, foreign corporations",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            },
            {
                "id": "ITR-7",
                "name": "ITR-7",
                "icon": "🏥",
                "description": "For entities filing returns under Sections 139(4A), 139(4B), 139(4C), and 139(4D), such as trusts, political parties, research institutions.",
                "eligibility": "Religious/charitable trusts, political parties, hospitals, research institutions",
                "ineligibility": "All other entities",
                "website_url": "https://incometaxindia.gov.in/forms",
                "tax_info": "income_tax_return"
            }
        ]

    @staticmethod
    def search_forms(query, forms):
        """Search forms based on query string"""
        if not query:
            return forms
            
        query = query.lower()
        return [
            form for form in forms
            if query in form['name'].lower() or
               query in form['description'].lower() or
               query in form['eligibility'].lower() or
               query in form['tax_info'].lower()
        ]