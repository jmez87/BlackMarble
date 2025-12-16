from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# File path
output_path = "Black_Marble_AI_Services_OnePager.pdf"

# Document setup
doc = SimpleDocTemplate(output_path, pagesize=landscape(letter),
                        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Header', fontSize=20, leading=24, textColor=colors.black, alignment=1, spaceAfter=12))
styles.add(ParagraphStyle(name='SubHeader', fontSize=14, leading=18, textColor=colors.HexColor("#4A4A4A"), spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name='Body', fontSize=11, leading=15, textColor=colors.black))
styles.add(ParagraphStyle(name='Quote', fontSize=11, leading=15, textColor=colors.HexColor("#333333"), leftIndent=20, italic=True))
styles.add(ParagraphStyle(name='Footer', fontSize=9, leading=11, textColor=colors.gray, alignment=1))

content = []

# Header
content.append(Paragraph("BLACK MARBLE ADVISORY GROUP", styles['Header']))
content.append(Paragraph("AI & Automation Services Overview", styles['SubHeader']))
content.append(Spacer(1, 12))

# Intro
content.append(Paragraph("""At <b>Black Marble Advisory Group</b>, we integrate accounting expertise with advanced AI technology to streamline financial processes, enhance accuracy, and deliver insights that drive results.""", styles['Body']))
content.append(Spacer(1, 12))

# Services Section
content.append(Paragraph("Our AI Services", styles['SubHeader']))
content.append(Paragraph("""• <b>Automated Bookkeeping</b> - AI-powered transaction categorization and reconciliation<br/>
• <b>Financial Forecasting</b> - Predictive analytics for cash flow and budget planning<br/>
• <b>Tax Optimization</b> - Machine learning algorithms to identify deductions and compliance opportunities<br/>
• <b>Custom Dashboards</b> - Real-time financial reporting with interactive visualizations""", styles['Body']))
content.append(Spacer(1, 12))

# Benefits Section
content.append(Paragraph("Key Benefits", styles['SubHeader']))
content.append(Paragraph("""✓ Reduce manual data entry by up to 80%<br/>
✓ Improve accuracy and eliminate human errors<br/>
✓ Get real-time insights for better decision making<br/>
✓ Scale operations without proportional cost increases""", styles['Body']))
content.append(Spacer(1, 12))

# Contact Section
content.append(Paragraph("Contact Information", styles['SubHeader']))
content.append(Paragraph("""<b>BLACK MARBLE ADVISORY GROUP</b><br/>
Email: info@blackmarbleadvisory.com<br/>
Phone: (555) 123-4567<br/>
Web: www.blackmarbleadvisory.com""", styles['Body']))

# Build the PDF
doc.build(content)
print(f"PDF generated successfully at: {output_path}")