from flask import Flask, request, render_template, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/generar_pdf", methods=["POST"])
def generar_pdf():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    rut = request.form["rut"]
    pais_origen = request.form["pais_origen"]

    # Generar el archivo PDF
    pdf_filename = f"{nombre}_{apellido}_info.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Estilos para el PDF
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle(name='Title', parent=styles['Title'], fontSize=24)
    style_normal = styles["Normal"]
    style_normal.leading = 25
    style_normal.fontSize = 14  # Puedes ajustar el tamaño de fuente según tus preferencias


    # Contenido del PDF
    content = []

    content.append(Paragraph("Panamericanos 2023", style_title))
    # Agregar espacio antes del título
    content.append(Spacer(1, 12))

    # Agregar espacio después del título
    content.append(Spacer(1, 24))

    content.append(Paragraph(f"<b>Nombre:</b> {nombre}", style_normal))
    content.append(Paragraph(f"<b>Apellidos:</b> {apellido}", style_normal))
    content.append(Paragraph(f"<b>RUT:</b> {rut}", style_normal))
    content.append(Paragraph(f"<b>Nacionalidad:</b> {pais_origen}", style_normal))

    doc.build(content)

    return send_file(pdf_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
