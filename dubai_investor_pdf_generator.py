
from fpdf import FPDF
from PIL import Image

class ProfessionalPDF(FPDF):
    def header(self):
        self.set_fill_color(44, 62, 80)
        self.rect(0, 0, 210, 20, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 16)
        self.set_y(5)
        self.cell(0, 10, "Dubai Renovation Investor Case Study", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(33, 47, 61)
        self.set_fill_color(230, 230, 230)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(2)

    def section_body(self, text):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, text)
        self.ln()

overview_text = "This document outlines the economics of a recently completed property renovation project in Dubai, executed by the developer under a design and build contract. The project was completed in 6 months."
financials = "- Built-Up Area (BUA): 5,800 sqft\n- Purchase Price (incl. fees): AED 17M\n- Refurbishment Cost: AED 3.5M\n- Total Investment: AED 20.5M\n- Sale Price: AED 25.5M\n- Gross Profit: AED 5M"
terms = "Investors receive:\n- Full return of capital: AED 20.5M\n- 12% per annum preferred return (6% for 6-month duration): AED 1.23M\n- Any profit above AED 21.73M is split 50/50 between investors and developer"
distribution = "- Total Profit: AED 5M\n- Capital + Preferred Return to Investors: AED 21.73M\n- Remaining Profit to Split: AED 3.77M\n\nDistribution under 50/50 model:\n- Investor Share of Remaining Profit: AED 1.885M\n- Developer Share of Remaining Profit: AED 1.885M\n\nInvestor Total Return: AED 23.115M\nDeveloper Total Return: AED 1.885M"
closing = "This model offers a compelling, repeatable investment opportunity with high annualized returns for investors, while rewarding the developer for efficient execution and value creation. The structure ensures alignment of interests and strong upside potential for all parties."

pdf = ProfessionalPDF()
pdf.add_page()
pdf.section_title("Project Overview")
pdf.section_body(overview_text)
pdf.section_title("Financial Summary")
pdf.section_body(financials)
pdf.section_title("Investor Terms")
pdf.section_body(terms)
pdf.section_title("Profit Distribution Breakdown")
pdf.section_body(distribution)
pdf.section_title("Conclusion")
pdf.section_body(closing)

# Add images
image_paths = ["image1.png", "image2.png"]
for path in image_paths:
    pdf.add_page()
    img = Image.open(path)
    width, height = img.size
    aspect = width / height
    page_width = 190
    img_height = page_width / aspect
    pdf.image(path, x=10, y=30, w=page_width, h=img_height)

pdf.output("Pro_Styled_Dubai_Renovation_Case_Study_With_Two_Images.pdf")
