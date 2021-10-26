from fpdf import FPDF
import os


def make_bill(fooditems, order_id):
    path = os.getcwd() + '\\customer\\Bill\\'
    print(path)
    pdf = FPDF(orientation='P', unit='cm')
    pdf.add_page()
    pdf.image(path + 'background.jpg', x=0, y=0, w=29.6, h=20.9)

    font_path = path + "Heading.ttf"
    pdf.add_font('pl_font', '', font_path, uni=True)
    pdf.set_font('pl_font', size=21)
    pdf.set_text_color(131, 115, 69)
    pdf.ln(0.62)
    pdf.cell(18, txt='NirCAS Bill', align='C', ln=2)

    pdf.add_font('pl_font', '', font_path, uni=True)
    pdf.set_font('pl_font', size=21)
    pdf.set_text_color(131, 115, 69)
    pdf.ln(2)
    pdf.cell(0, txt='Serial No.\t\t\t\tItems\t\t\t\t\t\t\t\tQuantity\t\t\t\t\t\tCost', align='L', ln=2)

    font_path = path + "Item.ttf"
    pdf.add_font('pl_font', '', font_path, uni=True)
    pdf.set_font('pl_font', size=21)
    pdf.set_text_color(131, 115, 69)
    pdf.ln(2)

    total_cost = 0
    for i in range(len(fooditems)):
        msg = '{}\t\t\t\t\t\t{}\t\t\t\t\t\t\t\t{}\t\t\t\t\t\t{}'.format(i,
                                                                    fooditems[i].food_id.name,
                                                                    fooditems[i].quantity,
                                                                    fooditems[i].food_id.cost * fooditems[i].quantity)
        total_cost += fooditems[i].food_id.cost * fooditems[i].quantity
        pdf.cell(0, txt=msg, align='L', ln=2)
        pdf.ln(1)

    pdf.add_font('pl_font', '', font_path, uni=True)
    pdf.set_font('pl_font', size=21)
    pdf.set_text_color(131, 115, 69)
    pdf.ln(2)
    pdf.cell(0, txt='Total Cost : {}'.format(total_cost), align='L', ln=2)
    pdf.ln(2)
    pdf.cell(0, txt='Order ID : {}'.format(order_id), align='L', ln=2)
    pdf.ln(1)

    path = os.getcwd() + '\\media\\bill\\'
    pdf.output(path + str(order_id) + '.pdf', 'F')
