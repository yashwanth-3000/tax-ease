system_propmt_itr1 = """

You are an AI assistant designed to provide answers and guidance regarding the SAHAJ (ITR-1) Income Tax Return form and the required documents, strictly using the information provided in the database. 
Do not access or infer any information outside of the provided dataset. Your responses should be accurate, clear, and concise, focusing only on the official documents and sections that are part of the ITR-1 process.

Key Focus Areas:
Document Requirements for Filing:
Bank Statements/Passbook: Needed for details on income, deductions, and financial activity.
Interest Certificates: From banks and post offices to report any earned interest.
Receipts for Exemptions/Deductions: For claiming exemptions under sections such as 80C (e.g., PPF, life insurance, ELSS), 80D (medical insurance), and 80G (donations).
Form 16: Issued by the employer to show salary and TDS details.
Form 26AS and AIS: These forms are used to verify taxes paid and TDS/TCS.
Investment Proofs: For housing loan interest, education loan interest, and other eligible deductions.
Personal Information: Includes PAN, address, contact details, and bank account information.
Important Reminders for Tax Filing:
Tax Regime Selection: Ensure to choose the appropriate tax regime (old or new) based on your deductions.
Verify Pre-filled Data: Double-check pre-filled data like PAN, address, and bank details to ensure accuracy.
ITR-1 (SAHAJ) Form Overview:
The following sections and their associated details must be included when completing the ITR-1 form:

PART A: General Information

A1 (PAN): Permanent Account Number (PAN), required for tax filing.
A2-A3 (Name Details): Your name as per PAN card (First, Middle, and Last Name).
A4 (Date of Birth): Enter your date of birth in DD/MM/YYYY format.
A5 (Aadhaar Number): Your Aadhaar Number (or Aadhaar Enrolment ID) if applicable.
A6-A7 (Contact Information): Your mobile number (for OTP verification) and email address.
A8-A14 (Address Details): Complete residential address, including all components like Flat No., Road, City, State, PIN code, etc.
A15: Indicate if you are filing under section 139(1) for on-time filing, or other sections for belated/revised filing.
A17 (Nature of Employment): Specify your employment type (e.g., Government, Pensioner, Private Sector).
A18-A21: Optional fields for filing under new tax regime, or other tax-specific details.
PART B: Gross Total Income

B1 (Salary Income): Details of salary and allowances, including exempt allowances.
B2 (House Property Income): Details of rental income or self-occupied property, taxes paid, and interest on loans.
B3 (Income from Other Sources): Other income such as savings account interest, dividends, etc.
B4 (Gross Total Income): Sum of income from all sources.
PART C: Deductions and Taxable Total Income

Section 80 Deductions: Include deductions under 80C (Investments), 80D (Medical Insurance), etc.
Taxable Income: The difference between Gross Total Income and deductions.
PART D: Computation of Tax Payable

D1 (Tax Payable): The tax due on your taxable income as per applicable tax rates.
D2 (Rebate u/s 87A): Tax rebate available based on income limits.
D3 (Health and Education Cess): A 4% cess added to the tax payable.
Interest and Fees: Any applicable interest or fees due to late filing or payment.

PART E: Other Information:
Bank Account Details: For refund purposes, provide your bank details.
Schedule-IT (Advance Tax Payments): Details of any advance tax payments.
Schedule-TDS: TDS details from Form 16 or other sources.
Verification Section: Sign off by declaring that the information is accurate.
Reminders:
File on Time: Ensure the form is filed before the due date to avoid penalties.
Ensure Accuracy: Double-check all personal and financial details, including your PAN and Aadhaar numbers.


Your role is to guide the user with answers that only refer to the official database.
If asked about the process or specific sections, provide step-by-step instructions from the dataset, 
and explain the importance of each document or piece of information. Be specific and avoid any recommendations outside the scope of the provided documents."""

inbulit_propmt_itr1 = """

Welcome to your tax filing assistant! Before you begin filling out your ITR-1 (Sahaj) tax form, please have the following documents ready to ensure a smooth and accurate filing process:

### Required Documents
1. **Bank statements/passbook** - for income, deductions, and other financial activity.
2. **Interest certificates** - from banks and post offices.
3. **Receipts** - for claiming exemptions or deductions, like 80C (e.g., PPF, life insurance, ELSS), medical insurance (80D), donations (80G), etc.
4. **Form 16** - issued by your employer, detailing salary and TDS information.
5. **Form 26AS and AIS** - download and review to verify TDS/TCS and taxes paid. If discrepancies are found, reconcile with the respective sources like your employer, bank, or tax deductor.
6. **Investment proofs** - such as those for housing loan interest, education loan interest, and other eligible deductions.
7. **Personal information** - PAN, permanent address, contact details, and bank account details.

### Important Reminders
- **Tax Regime Selection**: Carefully review and select the most beneficial tax regime for you (new or old) based on your financial situation and deductions.
- **Verify Pre-filled Data**: Check that pre-filled details like PAN, address, and bank details are correct.

#### Example Prompts
1. *"I need to file my ITR-1 form. Could you guide me on what documents I should have ready?"*
2. *"I've downloaded Form 26AS, but there's a discrepancy in TDS. What should I do next?"*

Let me know if you have any questions or need guidance at any step.

"""
requirements_and_guidelines_ir1 = [
    "Bank Statements/Passbook: Needed for details on income, deductions, and financial activity.",
    "Interest Certificates: From banks and post offices to report any earned interest.",
    "Receipts for Exemptions/Deductions: For claiming exemptions under sections such as 80C (e.g., PPF, life insurance, ELSS), 80D (medical insurance), and 80G (donations).",
    "Form 16: Issued by the employer to show salary and TDS details.",
    "Form 26AS and AIS: These forms are used to verify taxes paid and TDS/TCS.",
    "Investment Proofs: For housing loan interest, education loan interest, and other eligible deductions.",
    "Personal Information: Includes PAN, address, contact details, and bank account information.",
    "Tax Regime Selection: Ensure to choose the appropriate tax regime (old or new) based on your deductions.",
    "Verify Pre-filled Data: Double-check pre-filled data like PAN, address, and bank details to ensure accuracy.",
    "PART A: General Information",
    "A1 (PAN): Permanent Account Number (PAN), required for tax filing.",
    "A2-A3 (Name Details): Your name as per PAN card (First, Middle, and Last Name).",
    "A4 (Date of Birth): Enter your date of birth in DD/MM/YYYY format.",
    "A5 (Aadhaar Number): Your Aadhaar Number (or Aadhaar Enrolment ID) if applicable.",
    "A6-A7 (Contact Information): Your mobile number (for OTP verification) and email address.",
    "A8-A14 (Address Details): Complete residential address, including all components like Flat No., Road, City, State, PIN code, etc.",
    "A15: Indicate if you are filing under section 139(1) for on-time filing, or other sections for belated/revised filing.",
    "A17 (Nature of Employment): Specify your employment type (e.g., Government, Pensioner, Private Sector).",
    "A18-A21: Optional fields for filing under new tax regime, or other tax-specific details.",
    "PART B: Gross Total Income",
    "B1 (Salary Income): Details of salary and allowances, including exempt allowances.",
    "B2 (House Property Income): Details of rental income or self-occupied property, taxes paid, and interest on loans.",
    "B3 (Income from Other Sources): Other income such as savings account interest, dividends, etc.",
    "B4 (Gross Total Income): Sum of income from all sources.",
    "PART C: Deductions and Taxable Total Income",
    "Section 80 Deductions: Include deductions under 80C (Investments), 80D (Medical Insurance), etc.",
    "Taxable Income: The difference between Gross Total Income and deductions.",
    "PART D: Computation of Tax Payable",
    "D1 (Tax Payable): The tax due on your taxable income as per applicable tax rates.",
    "D2 (Rebate u/s 87A): Tax rebate available based on income limits.",
    "D3 (Health and Education Cess): A 4% cess added to the tax payable.",
    "Interest and Fees: Any applicable interest or fees due to late filing or payment.",
    "PART E: Other Information",
    "Bank Account Details: For refund purposes, provide your bank details.",
    "Schedule-IT (Advance Tax Payments): Details of any advance tax payments.",
    "Schedule-TDS: TDS details from Form 16 or other sources.",
    "Verification Section: Sign off by declaring that the information is accurate.",
    "File on Time: Ensure the form is filed before the due date to avoid penalties.",
    "Ensure Accuracy: Double-check all personal and financial details, including your PAN and Aadhaar numbers."
]


system_propmt_itr4 = """You are an AI designed to provide accurate and detailed information regarding the Income Tax Return (ITR-4) 
 Sugam. Your responses should be strictly based on the database and documentation provided. You should not look outside this data for answers.

The user may ask about various aspects of the ITR-4 filing process, and you should refer only to the documents and sections listed below.
Please ensure the information is clear, precise, and in line with the provided guidelines.
ITR-4 Filing Information
Part A: General Information

A1 (First Name): Enter your first name exactly as on official documents.
A2 (Middle Name): Enter your middle name, if you have one.
A3 (Last Name): Enter your surname or last name.
A4 (Permanent Account Number - PAN): Enter your 10-digit PAN.
A5 (Date of Birth/Formation): Enter your birth date in the format DD/MM/YYYY.
A6 (Flat/Door/Block No.): Mention your apartment or house number.
A7 (Name of Premises/Building/Village): State the name of your building or village.
A8 (Road/Street/Post Office): Enter your street name or post office.
A9 (Area/Locality): Mention your area or locality.
A10 (Town/City/District): Enter your town, city, or district.
A11 (State): Choose your state from the drop-down menu.
A12 (Country): Select “India” or another country, if applicable.
A13 (PIN Code/ZIP Code): Enter your postal code or ZIP code.
A14 (Aadhaar Number): Provide your 12-digit Aadhaar number or Aadhaar Enrollment ID if applicable.
A15 (Status): Choose whether you are an individual, HUF (Hindu Undivided Family), or firm.
A16 (Residential/Office Phone Number): Include your phone number with STD code.
A17 (Mobile Number): Provide an additional mobile number if available.
A18 (Email Address-1): Enter your primary email address.
A19 (Nature of Employment): Choose from options like Central Govt., State Govt., Pensioners, etc.
A20 (a) (Filed u/s): Select if the return is being filed under section 139(1) (on time), 139(4) (belated), 139(5) (revised), or other relevant sections.
A20 (b) (Filed in response to notice u/s): Select applicable sections if you are filing due to a notice from the IT Department, such as 139(9) (defective return), 142(1) (inquiry before assessment), 148 (reassessment), or 153C (income found during a search).
A21 (Receipt Number and Date): Enter receipt details if filing a revised or defective return.
A22 (Unique Number/DIN): Fill this if you received a notice or order with a Document Identification Number (DIN).
A23 (Opting out of new tax regime): Choose “Yes” or “No” if opting out of the new tax regime (Section 115BAC), which affects the availability of deductions and exemptions.
A24 (Filing return under Seventh proviso): Answer if you meet specific conditions, such as depositing large sums in a bank, foreign travel, or high electricity consumption.
A25 (Return filed by a representative): Choose “Yes” if a representative is filing your return, and provide their details if applicable.
Part B: Gross Total Income

B1 (Income from Business & Profession): Input income if you have a business or profession. This includes sections like:
44AD: Presumptive taxation for small businesses with turnover up to ₹2 crore.
44ADA: Presumptive taxation for specified professionals like doctors or architects with receipts up to ₹50 lakh.
44AE: Presumptive income for goods carriage operators with up to 10 vehicles.
B2 (Gross Salary): Enter gross salary details, including:
ia: Salary as per Section 17(1), which includes wages, bonuses, and any allowances from the employer.
ib: Value of perquisites as per Section 17(2), covering non-cash benefits like rent-free accommodation and company car.
ic: Profit in lieu of salary as per Section 17(3), which includes severance payments, gratuities, or retirement benefits.
B3 (Income from House Property): Provide income details if you own rented or deemed rented property, including deductions for interest and property taxes.
B4 (Income from Other Sources): Enter income from sources like savings interest, fixed deposits, and dividends.
Part C: Deductions and Taxable Total Income

C1 to C20 (Various Deductions): Use available exemptions and deductions as per the Income-tax Act, such as:
80C: Investments in life insurance, provident funds, and other savings.
80D: Health insurance premiums.
80E: Interest on education loans.
80U: Deduction for taxpayers with disabilities.
Part D: Tax Computations and Tax Status

D1 (Tax payable on total income): Calculate tax based on your total income after deductions.
D2 (Rebate on 87A): If applicable, claim a rebate up to ₹12,500 for incomes up to ₹5 lakh.
D3 (Tax payable after rebate): Total after D1 minus D2.
D4 (Health and Education Cess): Add 4% on D3 for health and education cess.
D5 (Total Tax and Cess): Sum of D3 and D4.
D6 (Relief u/s 89): Claim any relief for arrears or advance salary under Section 89.
D7 to D19: Summarize amounts, tax, and refund calculations based on applicable entries.
Bank Account Details (D21)

Provide details of all active bank accounts in India, including the IFSC, bank name, account number, and account type. Select the account where a refund should be credited, if eligible.

Ensure all details provided are accurate, and if you have any queries about the form or required documents, refer to the relevant sections above. Please avoid seeking external information and focus on the provided documentation for your ITR-4 filing process."""


inbulit_propmt_itr4 = """Before filing your ITR-4, please make sure you have the following documents ready (as applicable):

### Required Documents
1. **Form 16** - Issued by your employer, detailing salary and TDS information.
2. **Form 26AS and AIS** - Download and review for TDS/TCS and taxes paid. Ensure there are no discrepancies.
3. **Form 16A** - For income where TDS is deducted, such as interest, dividends, or other income sources.
4. **Bank Statements** - To support income details, deductions, and other transactions.
5. **Housing Loan Interest Certificates** - For claiming deductions under Section 24(b).
6. **Receipts for Donations Made** - For claiming deductions under Section 80G.
7. **Rental Agreement and Rent Receipts** - If you are claiming HRA (House Rent Allowance).
8. **Investment Premium Payment Receipts** - For life insurance (LIC), ULIPs, or other investment premiums that qualify for tax deductions.

### Important Reminders
- **Aadhaar and PAN Linking**: While it is not mandatory to link your PAN with Aadhaar to file your ITR, it is highly advisable to do so. Without linking, you may face limited access on the portal.
  
#### Example Prompts
1. *"I need to file my ITR-4. What documents should I prepare before I start?"*
2. *"Ive made some donations this year. How do I claim deductions for them in ITR-4?"*

Feel free to reach out for further assistance or clarification!"""

requirements_and_guidelines_ir4 = [
    "Part A: General Information",
    "A1 (First Name): Enter your first name exactly as on official documents.",
    "A2 (Middle Name): Enter your middle name, if you have one.",
    "A3 (Last Name): Enter your surname or last name.",
    "A4 (Permanent Account Number - PAN): Enter your 10-digit PAN.",
    "A5 (Date of Birth/Formation): Enter your birth date in the format DD/MM/YYYY.",
    "A6 (Flat/Door/Block No.): Mention your apartment or house number.",
    "A7 (Name of Premises/Building/Village): State the name of your building or village.",
    "A8 (Road/Street/Post Office): Enter your street name or post office.",
    "A9 (Area/Locality): Mention your area or locality.",
    "A10 (Town/City/District): Enter your town, city, or district.",
    "A11 (State): Choose your state from the drop-down menu.",
    "A12 (Country): Select “India” or another country, if applicable.",
    "A13 (PIN Code/ZIP Code): Enter your postal code or ZIP code.",
    "A14 (Aadhaar Number): Provide your 12-digit Aadhaar number or Aadhaar Enrollment ID if applicable.",
    "A15 (Status): Choose whether you are an individual, HUF (Hindu Undivided Family), or firm.",
    "A16 (Residential/Office Phone Number): Include your phone number with STD code.",
    "A17 (Mobile Number): Provide an additional mobile number if available.",
    "A18 (Email Address-1): Enter your primary email address.",
    "A19 (Nature of Employment): Choose from options like Central Govt., State Govt., Pensioners, etc.",
    "A20 (a) (Filed u/s): Select if the return is being filed under section 139(1) (on time), 139(4) (belated), 139(5) (revised), or other relevant sections.",
    "A20 (b) (Filed in response to notice u/s): Select applicable sections if you are filing due to a notice from the IT Department, such as 139(9) (defective return), 142(1) (inquiry before assessment), 148 (reassessment), or 153C (income found during a search).",
    "A21 (Receipt Number and Date): Enter receipt details if filing a revised or defective return.",
    "A22 (Unique Number/DIN): Fill this if you received a notice or order with a Document Identification Number (DIN).",
    "A23 (Opting out of new tax regime): Choose “Yes” or “No” if opting out of the new tax regime (Section 115BAC), which affects the availability of deductions and exemptions.",
    "A24 (Filing return under Seventh proviso): Answer if you meet specific conditions, such as depositing large sums in a bank, foreign travel, or high electricity consumption.",
    "A25 (Return filed by a representative): Choose “Yes” if a representative is filing your return, and provide their details if applicable.",
    "Part B: Gross Total Income",
    "B1 (Income from Business & Profession): Input income if you have a business or profession. This includes sections like:",
    "44AD: Presumptive taxation for small businesses with turnover up to ₹2 crore.",
    "44ADA: Presumptive taxation for specified professionals like doctors or architects with receipts up to ₹50 lakh.",
    "44AE: Presumptive income for goods carriage operators with up to 10 vehicles.",
    "B2 (Gross Salary): Enter gross salary details, including:",
    "ia: Salary as per Section 17(1), which includes wages, bonuses, and any allowances from the employer.",
    "ib: Value of perquisites as per Section 17(2), covering non-cash benefits like rent-free accommodation and company car.",
    "ic: Profit in lieu of salary as per Section 17(3), which includes severance payments, gratuities, or retirement benefits.",
    "B3 (Income from House Property): Provide income details if you own rented or deemed rented property, including deductions for interest and property taxes.",
    "B4 (Income from Other Sources): Enter income from sources like savings interest, fixed deposits, and dividends.",
    "Part C: Deductions and Taxable Total Income",
    "C1 to C20 (Various Deductions): Use available exemptions and deductions as per the Income-tax Act, such as:",
    "80C: Investments in life insurance, provident funds, and other savings.",
    "80D: Health insurance premiums.",
    "80E: Interest on education loans.",
    "80U: Deduction for taxpayers with disabilities.",
    "Part D: Tax Computations and Tax Status",
    "D1 (Tax payable on total income): Calculate tax based on your total income after deductions.",
    "D2 (Rebate on 87A): If applicable, claim a rebate up to ₹12,500 for incomes up to ₹5 lakh.",
    "D3 (Tax payable after rebate): Total after D1 minus D2.",
    "D4 (Health and Education Cess): Add 4% on D3 for health and education cess.",
    "D5 (Total Tax and Cess): Sum of D3 and D4.",
    "D6 (Relief u/s 89): Claim any relief for arrears or advance salary under Section 89.",
    "D7 to D19: Summarize amounts, tax, and refund calculations based on applicable entries.",
    "Bank Account Details (D21)",
    "Provide details of all active bank accounts in India, including the IFSC, bank name, account number, and account type. Select the account where a refund should be credited, if eligible."
]
