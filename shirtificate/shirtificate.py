from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 30)
        self.ln(20)
        self.cell(w=0, txt="CS50 Shirtificate", new_y="NEXT", align="C")
        self.ln(20)


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(False)
    pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", x="C", w=pdf.epw)
    with pdf.local_context():
        pdf.set_font("helvetica", "B", 23)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, -250, txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if "__main__" == __name__:
    main()
