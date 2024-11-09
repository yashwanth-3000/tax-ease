class FormData:
    @staticmethod
    def get_sample_forms():
        """Return sample tax forms data with additional fields like website_url and tax_info"""
        return [
            {
                "id": "1040",
                "name": "Form 1040",
                "icon": "📝",
                "description": "U.S. Individual Income Tax Return. The standard form used by U.S. taxpayers to file their annual income tax returns.",
                "eligibility": "All U.S. taxpayers",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-1040",
                "tax_info": "income_tax"
            },
            {
                "id": "w2",
                "name": "Form W-2",
                "icon": "💼",
                "description": "Wage and Tax Statement. Shows your annual wages and taxes withheld from your paycheck.",
                "eligibility": "Employed individuals",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-w-2",
                "tax_info": "income_tax"
            },
            {
                "id": "1099",
                "name": "Form 1099",
                "icon": "💰",
                "description": "Information returns for various types of income other than wages, salaries, and tips.",
                "eligibility": "Self-employed, contractors, investors",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-1099",
                "tax_info": "income_tax"
            },
            {
                "id": "schedule_c",
                "name": "Schedule C",
                "icon": "🏢",
                "description": "Profit or Loss from Business. Used to report income or loss from a business you operated or profession you practiced as a sole proprietor.",
                "eligibility": "Self-employed individuals",
                "website_url": "https://www.irs.gov/forms-pubs/about-schedule-c",
                "tax_info": "income_tax"
            },
            {
                "id": "schedule_a",
                "name": "Schedule A",
                "icon": "📊",
                "description": "Itemized Deductions. Used to claim various deductions like medical expenses, taxes paid, interest paid, and charitable contributions.",
                "eligibility": "Taxpayers who itemize deductions",
                "website_url": "https://www.irs.gov/forms-pubs/about-schedule-a-form-1040",
                "tax_info": "income_tax"
            },
            {
                "id": "8962",
                "name": "Form 8962",
                "icon": "🏥",
                "description": "Premium Tax Credit. Used to reconcile advance payments of the premium tax credit and to claim the premium tax credit.",
                "eligibility": "Healthcare Marketplace insurance users",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8962",
                "tax_info": "income_tax"
            },
            # 15 additional dummy data entries:
            {
                "id": "8889",
                "name": "Form 8889",
                "icon": "💳",
                "description": "Health Savings Accounts (HSAs). Used to report contributions to, and distributions from, a health savings account.",
                "eligibility": "Individuals with Health Savings Accounts",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8889",
                "tax_info": "income_tax"
            },
            {
                "id": "2441",
                "name": "Form 2441",
                "icon": "👶",
                "description": "Child and Dependent Care Expenses. Used to claim the Child and Dependent Care Credit.",
                "eligibility": "Taxpayers who pay for child or dependent care",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-2441",
                "tax_info": "income_tax"
            },
            {
                "id": "8862",
                "name": "Form 8862",
                "icon": "💸",
                "description": "Information to Claim Earned Income Credit After Disallowance. Used to claim the Earned Income Tax Credit (EITC) after a disallowance.",
                "eligibility": "Taxpayers claiming the EITC after disallowance",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8862",
                "tax_info": "income_tax"
            },
            {
                "id": "8880",
                "name": "Form 8880",
                "icon": "🔑",
                "description": "Credit for Qualified Retirement Savings Contributions. Used to claim a credit for retirement contributions.",
                "eligibility": "Taxpayers who contribute to retirement savings accounts",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8880",
                "tax_info": "income_tax"
            },
            {
                "id": "8863",
                "name": "Form 8863",
                "icon": "🎓",
                "description": "Education Credits. Used to claim education credits like the American Opportunity Credit and the Lifetime Learning Credit.",
                "eligibility": "Taxpayers who pay for qualified education expenses",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8863",
                "tax_info": "income_tax"
            },
            {
                "id": "8862",
                "name": "Form 8862",
                "icon": "💡",
                "description": "Information to Claim Earned Income Credit After Disallowance. Used to claim the Earned Income Tax Credit (EITC) after a disallowance.",
                "eligibility": "Taxpayers claiming the EITC after disallowance",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8862",
                "tax_info": "income_tax"
            },
            {
                "id": "1040nr",
                "name": "Form 1040NR",
                "icon": "🌎",
                "description": "Nonresident Alien Income Tax Return. Used by non-resident aliens to file their U.S. income tax return.",
                "eligibility": "Nonresident aliens with U.S. income",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-1040nr",
                "tax_info": "income_tax"
            },
            {
                "id": "941",
                "name": "Form 941",
                "icon": "🏢",
                "description": "Employer's Quarterly Federal Tax Return. Used by employers to report income taxes, Social Security, and Medicare taxes withheld from employees' paychecks.",
                "eligibility": "Employers",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-941",
                "tax_info": "income_tax"
            },
            {
                "id": "2106",
                "name": "Form 2106",
                "icon": "💼",
                "description": "Employee Business Expenses. Used to deduct work-related expenses of employees.",
                "eligibility": "Employees with business expenses",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-2106",
                "tax_info": "income_tax"
            },
            {
                "id": "2555",
                "name": "Form 2555",
                "icon": "🌍",
                "description": "Foreign Earned Income Exclusion. Used to exclude income earned outside of the U.S. from U.S. taxation.",
                "eligibility": "U.S. citizens living abroad",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-2555",
                "tax_info": "income_tax"
            },
            {
                "id": "8885",
                "name": "Form 8885",
                "icon": "🏥",
                "description": "Health Coverage Tax Credit. Used to claim the health coverage tax credit for certain workers and retirees.",
                "eligibility": "Eligible workers and retirees",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8885",
                "tax_info": "income_tax"
            },
            {
                "id": "8886",
                "name": "Form 8886",
                "icon": "📊",
                "description": "Reportable Transaction Disclosure Statement. Used to report certain transactions that may require disclosure to the IRS.",
                "eligibility": "Taxpayers involved in certain transactions",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8886",
                "tax_info": "income_tax"
            },
            {
                "id": "8960",
                "name": "Form 8960",
                "icon": "💼",
                "description": "Net Investment Income Tax. Used to report net investment income tax (NIIT) for certain individuals.",
                "eligibility": "Individuals with net investment income",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8960",
                "tax_info": "income_tax"
            },
            {
                "id": "8959",
                "name": "Form 8959",
                "icon": "💸",
                "description": "Additional Medicare Tax. Used to report and pay the additional Medicare tax on high-income individuals.",
                "eligibility": "High-income individuals",
                "website_url": "https://www.irs.gov/forms-pubs/about-form-8959",
                "tax_info": "income_tax"
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
