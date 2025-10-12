from time import strftime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime

def generate_financial_report(net_profit, total_profit, total_cost, inventory_sum, filename="financial_report.pdf"):

    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Financial Report", styles['Title']))

    story.append(Spacer(1, 13))

    today = datetime.datetime.now().strftime("%Y-%m-%d")

    story.append(Paragraph(f"Date: {today}", styles['Normal']))

    story.append(Spacer(1,13))

    story.append(Paragraph(f"<b>Company Assets: </b> {inventory_sum:.2f} $", styles['Normal']))

    story.append(Spacer(1, 13))

    story.append(Paragraph(f"<b>Total Profit: </b> {total_profit:.2f} $", styles['Normal']))

    story.append(Paragraph(f"<b>Total Cost: </b> {total_cost:.2f} $", styles['Normal']))

    story.append(Paragraph(f"<b>Net Profit: </b> {net_profit:.2f} $", styles['Normal']))



    story.append(Spacer(1,13))

    doc.build(story)
