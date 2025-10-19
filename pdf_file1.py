from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Sample Document Title", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def create_sample_pdf(file_name):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    sample_texts = [
        "This document discusses the impact of climate change on global agriculture. "
        "Studies indicate that rising temperatures will reduce crop yields in many regions.",

        "Economic consequences of these changes include food price volatility and increased poverty in vulnerable communities.",

        "Adaptation strategies include developing drought-resistant crops and improving irrigation efficiency.",

        "Renewable energy adoption is accelerating worldwide, with solar and wind power leading the way.",

        "Technological advances in battery storage are critical for a sustainable energy future.",

        "Urbanization trends are reshaping demographics and infrastructure demands globally.",

        "Artificial Intelligence is transforming industries from healthcare to finance.",

        "Cybersecurity remains a significant concern as digital threats evolve.",

        "Global trade policies impact economic growth and international relations.",

        "Sustainability initiatives are increasingly important in corporate strategy and governance."
    ]

    # Create 10 pages, one for each paragraph
    for i, text in enumerate(sample_texts, start=1):
        pdf.add_page()
        pdf.multi_cell(0, 10, f"Page {i}:\n\n{text}")

    pdf.output(file_name)
    print(f"Sample PDF '{file_name}' created successfully.")

if __name__ == "__main__":
    create_sample_pdf("sample.pdf")
