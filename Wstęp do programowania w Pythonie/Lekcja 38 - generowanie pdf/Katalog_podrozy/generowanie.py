from fpdf import FPDF

A4W = 210
A4H = 297

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=32)
pdf.set_text_color(255, 0, 0)
pdf.text(x=30, y=20, text="Oferta biura Huricane Trave's")

pdf.image(
    "logo.png",
    x=A4W*0.25,
    y=A4W*0.25,
    w=A4W*0.5,
    h=A4W*0.5
)

pdf.output("wycieczka.pdf")