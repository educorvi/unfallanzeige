# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.ttfonts import TTFont

def createpdf():
    dateiname = "C:\Users\Besitzer\Documents\Dokomente\Python27\Tabelle.pdf"
    c = canvas.Canvas(dateiname, pagesize=A4)
    c.setAuthor(u"Pascal Daniel Paul")
    c.setTitle(u"Elektronische Tabelle")
    
    return c
    
def drawpdf(c):

    schriftart = "Helvetica"
    
    # Tabellen Unfang
    c.rect(4*cm, 11.9*cm, 13*cm, 14.9*cm)
    
    # Zeichnen von Linien
    c.line(4*cm, 25.7*cm, 17*cm, 25.7*cm)
    c.line(4*cm, 22.5*cm, 17*cm, 22.5*cm)
    c.line(4*cm, 18.2*cm, 17*cm, 18.2*cm)
    
    c.line(10.2*cm, 17.5*cm, 17*cm, 17.5*cm)
    x1=10.2*cm
    x2=17*cm
    y=17.5
    diff=0.8
    for i in range(4):
        c.line(x1, y*cm, x2, y*cm)
        y=y-diff
    
    c.line(4*cm, 14.4*cm, 17*cm, 14.4*cm)
    c.line(4*cm, 13.6*cm, 17*cm, 13.6*cm)
    c.line(4*cm, 12.8*cm, 17*cm, 12.8*cm)
    
    # sekrechte Linie
    c.line(10.2*cm, 26.8*cm, 10.2*cm, 11.9*cm)
    
    # Beschriftungen
    c.setFont(schriftart, 14)
    c.drawString(4.3*cm, 26.1*cm, u'Tätigkeiten:')
    c.drawString(4.3*cm, 24.8*cm, u'Gefahrstoffe:')
    c.drawString(4.3*cm, 21.4*cm, u'Mechanik:')
    c.drawString(4.3*cm, 13.8*cm, u'Schichtstärke:')
    c.drawString(4.3*cm, 13*cm, u'Stulpenlänge:')
    c.drawString(4.3*cm, 12.2*cm, u'Sonstiges:')
    
    c.setFont(schriftart, 10)
    c.drawString(10.5*cm, 17.8*cm, u'Stich:')
    c.drawString(10.5*cm, 17*cm, u'Stoss:')
    c.drawString(10.5*cm, 16.2*cm, u'Schnitt:')
    c.drawString(10.5*cm, 15.4*cm, u'Abrieb')
    c.drawString(10.5*cm, 14.6*cm, u'Sonstiges:')
    c.drawString(10.9*cm, 24.8*cm, u'Chemisch/biologisch')
    c.drawString(10.9*cm, 24.2*cm, u'mechamisch')
    
    # Ankreuzkestechen
    c.rect(10.4*cm, 24.8*cm, 0.4*cm, 0.4*cm)
    c.rect(10.4*cm, 24.2*cm, 0.4*cm, 0.4*cm)
    
    return c
    
def savepdf(c):

    # seitenumbruch
    c.showPage()
    #Dokument Speichern
    c.save()
    
if __name__=="__main__":

    c = createpdf()
    c = drawpdf(c)
    savepdf(c) 