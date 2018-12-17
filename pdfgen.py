# -*- coding:utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.ttfonts import TTFont

def createpdf():
    dateiname = "C:\Users\Besitzer\Documents\Dokomente\Python27\Unfallanzeige.pdf"
    c = canvas.Canvas(dateiname, pagesize=A4)
    c.setAuthor(u"Pascal Daniel Paul")
    c.setTitle(u"Elektronische Unfallanzeige")
	
    #Überschrift
    #c.setFont(schriftart, 12)
    #c.drawString(7*cm, 15*cm, u"Pascal Daniel Paul")
    
    return c
      
def drawpdf(c):
    schriftart = "Helvetica"
    schriftartfett = "Helvetica-Bold"
    ##Zeichnen von linien:##
    
    #Domumentramen:
    c.rect(2.5*cm, 1.8*cm, 17.2*cm, 25.4*cm)
    
    
    #paralellinien oben wagerecht:
    x1=2.5*cm
    x2=19.7*cm
    y=20.3
    diff=0.8
    for i in range(4):
        c.line(x1, y*cm, x2, y*cm)
        y=y-diff  
    
    
    #Trennsrich Z1 Spanlten 2-4 durchgezogen:
    c.line(12.5*cm, 17.9*cm, 12.5*cm, 20.3*cm)
    
    
    #Feld Unternehmensnummer:
    c.line(12.2*cm, 25.5*cm, 19.7*cm, 25.5*cm)
    c.line(12.2*cm, 25.5*cm, 12.2*cm, 26.2*cm)
    
    
    #Feld Empfenger/in:
    c.line(2.8*cm, 24*cm, 3.1*cm, 24*cm)
    c.line(2.8*cm, 20.8*cm, 2.8*cm, 20.5*cm)
    c.line(2.8*cm, 20.5*cm, 3.1*cm, 20.5*cm)
    c.line(2.8*cm, 23.7*cm, 2.8*cm, 24*cm) 
    c.line(10.4*cm, 24*cm, 10.7*cm, 24*cm)
    c.line(10.7*cm, 23.7*cm, 10.7*cm, 24*cm)
    c.line(10.7*cm, 20.5*cm, 10.7*cm, 20.8*cm)
    c.line(10.4*cm, 20.5*cm, 10.7*cm, 20.5*cm)
    
    
    #paralellinien unten wagerecht:
    x1=2.5*cm
    x2=19.7*cm
    y=6.6
    diff=0.8
    for i in range(5):
        c.line(x1, y*cm, x2, y*cm)
        y=y-diff
    
    
    #Trennstriche Tag/Monat/Jahr-durchgezogen:
    y1=19.5*cm
    y2=20.3*cm
    x=15
    diff=1.2
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
        
        
    #Trennstriche Tag/Monat/Jahr halbdurchgezogen:    
    y1=19.5*cm
    y2=19.8*cm
    x=15.6
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    c.line(15.6*cm, 19.5*cm, 15.6*cm, 19.8*cm)
    
    c.line(17.9*cm, 19.5*cm, 17.9*cm, 19.8*cm)
    y1=19.5*cm
    y2=19.8*cm
    x=17.9
    diff=0.6
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
     
    #Trennstriche Z2 Durchgezogen:
    c.line(9.7*cm, 18.7*cm, 9.7*cm, 19.5*cm)
    
    
    #halbdurchgezogen:
    c.line(10.2*cm, 18.7*cm, 10.2*cm, 19.0*cm)
    y1=18.7*cm
    y2=19.0*cm
    x=10.2
    diff=0.6
    for i in range(4):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    
    #Allgemein Trennsrich Durchgezogen:
    c.line(7.9*cm, 14.6*cm, 7.9*cm, 15.6*cm)
    c.line(5.9*cm, 13.6*cm, 5.9*cm, 14.6*cm)
    c.line(12.9*cm, 13.6*cm, 12.9*cm, 14.6*cm)
    c.line(11.1*cm, 9.1*cm, 11.1*cm, 9.8*cm)
    c.line(12.7*cm, 6.6*cm, 12.7*cm, 7.9*cm)
    c.line(11.7*cm, 5.8*cm, 11.7*cm, 6.6*cm)
    c.line(7*cm, 13.6*cm, 7*cm, 14.2*cm)
    y1=13.6*cm
    y2=14.2*cm
    x=7
    diff=1.1
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    c.line(6.45*cm, 13.6*cm, 6.45*cm, 14*cm)
    y1=13.6*cm
    y2=14*cm
    x=6.45
    diff=1.1
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(10.5*cm, 13.6*cm, 10.5*cm, 14.2*cm)
    y1=13.6*cm
    y2=14.2*cm
    x=10.5
    diff=1.1
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(14*cm, 6.6*cm, 14*cm, 7.2*cm)
    y1=6.6*cm
    y2=7.2*cm
    x=14
    diff=1.2
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(17.4*cm, 6.6*cm, 17.4*cm, 7.2*cm)
    y1=6.6*cm
    y2=7.2*cm
    x=17.4
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(16.4*cm, 5.8*cm, 16.4*cm, 6.6*cm)
    y1=5.8*cm
    y2=6.6*cm
    x=16.4
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
   
    c.line(16.2*cm, 4.2*cm, 16.2*cm, 5*cm)
    y1=4.2*cm
    y2=5*cm
    x=16.2
    diff=1.2
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(15*cm, 3.4*cm, 15*cm, 4.2*cm)
    y1=3.4*cm
    y2=4.2*cm
    x=15
    diff=1.2
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
        
    #Halbduchrchgezogen:
    c.line(8.7*cm, 13.6*cm, 8.7*cm, 14*cm)
    y1=13.6*cm
    y2=14*cm
    x=8.7
    diff=0.6
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
        
    c.line(11.05*cm, 13.6*cm, 11.05*cm, 14*cm)
    y1=13.6*cm
    y2=14*cm
    x=11.05
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(14.6*cm, 6.6*cm, 14.6*cm, 7*cm)
    y1=6.6*cm
    y2=7*cm
    x=14.6
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(18*cm, 6.6*cm, 18*cm, 7*cm)
    y1=6.6*cm
    y2=7*cm
    x=18
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(17*cm, 5.8*cm, 17*cm, 6.2*cm)
    y1=5.8*cm
    y2=6.2*cm
    x=17
    diff=1.2
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(18.7*cm, 5.8*cm, 18.7*cm, 6.2*cm)
    y1=5.8*cm
    y2=6.2*cm
    x=18.7
    diff=0.5
    for i in range(2):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(16.8*cm, 4.2*cm, 16.8*cm, 4.6*cm)
    y1=4.2*cm
    y2=4.6*cm
    x=16.8
    diff=1.2
    for i in range(3):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    
    c.line(18.6*cm, 3.4*cm, 18.6*cm, 3.8*cm)
    c.line(15.6*cm, 3.4*cm, 15.6*cm, 3.8*cm)
    y1=3.4*cm
    y2=3.8*cm
    x=15.6
    diff=1.2
    for i in range(4):
        c.line(x*cm, y1, x*cm, y2)
        x=x+diff
    c.line(18.6*cm, 4.2*cm, 18.6*cm, 5*cm)
    
    
    #Trennsrich Z3-Spalte 5 Durchgezogen:
    c.line(6.3*cm, 15.6*cm, 6.3*cm, 18.7*cm)
    
    
    #Allgemein Wagerecht durgezogenelinien:
    c.line(2.5*cm, 15.6*cm, 19.7*cm, 15.6*cm)
    c.line(2.5*cm, 15.6*cm, 19.7*cm, 15.6*cm)
    c.line(2.5*cm, 14.6*cm, 19.7*cm, 14.6*cm)
    c.line(2.5*cm, 13.6*cm, 19.7*cm, 13.6*cm)
    c.line(2.5*cm, 9.8*cm, 19.7*cm, 9.8*cm)
    c.line(2.5*cm, 9.1*cm, 19.7*cm, 9.1*cm)
    c.line(2.5*cm, 7.9*cm, 19.7*cm, 7.9*cm)
    c.line(2.5*cm, 2.3*cm, 19.7*cm, 2.3*cm)
    
    
    #Ankreuzekestchen:
    c.rect(2.7*cm, 18*cm, 0.3*cm, 0.3*cm)
    c.rect(4.7*cm, 18*cm, 0.3*cm, 0.3*cm)
    c.rect(12.7*cm, 18*cm, 0.3*cm, 0.3*cm)
    c.rect(14.7*cm, 18*cm, 0.3*cm, 0.3*cm)
    c.rect(2.7*cm, 17.2*cm, 0.3*cm, 0.3*cm)
    c.rect(4.7*cm, 17.2*cm, 0.3*cm, 0.3*cm)
    c.rect(10.5*cm, 17.5*cm, 0.3*cm, 0.3*cm)
    c.rect(10.5*cm, 16.9*cm, 0.3*cm, 0.3*cm)
    c.rect(14.7*cm, 17.5*cm, 0.3*cm, 0.3*cm)
    c.rect(15.4*cm, 16.9*cm, 0.3*cm, 0.3*cm)
    c.rect(15.4*cm, 16.5*cm, 0.3*cm, 0.3*cm)
    c.rect(15.4*cm, 15.75*cm, 0.3*cm, 0.3*cm)
    c.rect(4.2*cm, 14.75*cm, 1.2*cm, 0.4*cm)
    c.line(4.8*cm, 14.75*cm, 4.8*cm, 15.15*cm)
    c.rect(2.7*cm, 13.85*cm, 0.3*cm, 0.3*cm)
    c.rect(4.7*cm, 13.85*cm, 0.3*cm, 0.3*cm)
    c.rect(8.8*cm, 9.9*cm, 0.3*cm, 0.3*cm)
    c.rect(12.4*cm, 9.9*cm, 0.3*cm, 0.3*cm)
    c.rect(13.9*cm, 8*cm, 0.3*cm, 0.3*cm)
    c.rect(16*cm, 8*cm, 0.3*cm, 0.3*cm)
    c.rect(13*cm, 4.6*cm, 0.3*cm, 0.3*cm)
    c.rect(11*cm, 4.6*cm, 0.3*cm, 0.3*cm)
    c.rect(13*cm, 3.8*cm, 0.3*cm, 0.3*cm)
    c.rect(11*cm, 3.8*cm, 0.3*cm, 0.3*cm)
    
    
    #Zahlen:
    c.setFont(schriftartfett, 8)
    c.drawString(2.7*cm, 26.3*cm, '1')
    c.drawString(12.3*cm, 26.3*cm, '2')
    c.drawString(2.7*cm, 24.1*cm, '3')
    c.drawString(2.7*cm, 20*cm, '4')
    c.drawString(12.7*cm, 20*cm, '5')
    c.drawString(2.7*cm, 19.2*cm, '6')
    c.drawString(2.7*cm, 18.4*cm, '7')
    c.drawString(6.4*cm, 18.4*cm, '8')
    c.drawString(12.7*cm, 18.4*cm, '9')
    c.drawString(2.7*cm, 17.6*cm, '10')
    c.drawString(6.4*cm, 17.6*cm, '11')
    c.drawString(2.7*cm, 15.3*cm, '12')
    c.drawString(8*cm, 15.3*cm, '13')
    c.drawString(2.7*cm, 14.3*cm, '14')
    c.drawString(6*cm, 14.3*cm, '15')
    c.drawString(13*cm, 14.3*cm, '16')
    c.drawString(2.7*cm, 13.3*cm, '17')
    c.drawString(2.7*cm, 9.5*cm, '18')
    c.drawString(11.2*cm, 9.5*cm, '19')
    c.drawString(2.7*cm, 8.8*cm, '20')
    c.drawString(2.7*cm, 7.6*cm, '21')
    c.drawString(12.9*cm, 7.6*cm, '22')
    c.drawString(2.7*cm, 6.3*cm, '23')
    c.drawString(11.9*cm, 6.3*cm, '24')
    c.drawString(2.7*cm, 5.5*cm, '25')
    c.drawString(2.7*cm, 4.65*cm, '26')
    c.drawString(2.7*cm, 3.85*cm, '27')
    c.drawString(2.7*cm, 1.95*cm, '28')
    
    
    #Beschriftungen:
    c.setFont(schriftartfett, 16)
    c.drawString(12.3*cm, 26.6*cm, 'U N F A L L A N Z E I G E')
    c.setFont(schriftart, 8) 
    c.drawString(2.9*cm, 26.3*cm, 'Name und Anschrift des Unternehmens')
    c.drawString(12.5*cm, 26.3*cm, u'Unternehmensnummer des Unfallversicherungsträgers')
    c.drawString(2.9*cm, 24.1*cm, u'Empfänger/-in')
    c.drawString(2.9*cm, 20*cm, 'Name, Vorname der versicherten Person')
    c.drawString(12.9*cm, 20*cm, 'Geburtsdatum')
    c.drawString(15.35*cm, 20*cm, 'Tag')
    c.drawString(16.4*cm, 20*cm, 'Monat')
    c.drawString(18.2*cm, 20*cm, 'Jahr')
    c.drawString(2.9*cm, 19.2*cm, u'Straße, Hausnummer')
    c.drawString(9.8*cm, 19.2*cm, 'Postleitzahl')
    c.drawString(12.7*cm, 19.2*cm, 'Ort')
    c.drawString(2.9*cm, 18.4*cm, u'Geschlecht')
    c.drawString(3.1*cm, 18.05*cm, u'Mänlich')
    c.drawString(5.1*cm, 18.05*cm, 'Weiblich')
    c.drawString(13.1*cm, 18.05*cm, 'Ja')
    c.drawString(15.1*cm, 18.05*cm, 'Nein')
    c.drawString(6.6*cm, 18.4*cm, u'Staatsangehörigkeit')
    c.drawString(12.9*cm, 18.4*cm, 'Leiharbeitnehmer/-in')
    c.drawString(3.1*cm, 17.6*cm, 'Auszubildende/-r')
    c.drawString(3.1*cm, 17.25*cm, 'Ja')
    c.drawString(5.1*cm, 17.25*cm, 'Nein')
    c.drawString(6.75*cm, 17.6*cm, 'Die versicherte Person ist')
    c.drawString(11.1*cm, 17.55*cm, 'Unternehmer/-in')
    c.drawString(15.2*cm, 17.6*cm, 'mit der Unternehmerin/')
    c.drawString(15.2*cm, 17.35*cm, u'dem Unternehmer:')
    c.drawString(11.1*cm, 16.95*cm, 'Gesellschafter/-in')
    c.drawString(11.1*cm, 16.65*cm, u'Geschäftsführer/-in')
    c.drawString(15.8*cm, 16.95*cm, 'verheiratet')
    c.drawString(15.8*cm, 16.55*cm, 'in eingetragener')
    c.drawString(15.8*cm, 16.21*cm, 'Lebenspartnerschaft lebend')
    c.drawString(15.8*cm, 15.85*cm, 'verwandt')
    c.drawString(3.1*cm, 15.3*cm, 'Anspruch auf Entgeltfortzahlung')
    c.drawString(2.7*cm, 14.85*cm, u'besteht für')
    c.drawString(5.5*cm, 14.85*cm, 'Wochen')
    c.drawString(8.4*cm, 15.3*cm, u'Krankenkasse (Name, PLZ, Ort)')
    c.drawString(3.1*cm, 14.3*cm, u'Tödlicher Unfall?')
    c.drawString(6.4*cm, 14.3*cm, u"Unfallzeitpunkt")
    c.drawString(13.4*cm, 14.3*cm, u"Unfallort")
    c.setFont(schriftart, 6)
    c.drawString(14.5*cm, 14.35*cm, u"(genaue Orts- und Straßenangabe mit PLZ)")
    c.setFont(schriftart, 8)
    c.drawString(3.1*cm, 13.95*cm, 'Ja')
    c.drawString(5.1*cm, 13.95*cm, 'Nein')
    c.drawString(6.2*cm, 14.05*cm, u"Tag")
    c.drawString(7.2*cm, 14.05*cm, u"Monat")
    c.drawString(9*cm, 14.05*cm, u"Jahr")
    c.drawString(10.6*cm, 14.05*cm, u"Stunde")
    c.drawString(11.8*cm, 14.05*cm, u"Minute")
    c.drawString(3.1*cm, 13.3*cm, u"Ausführliche Schilderung des Unfallhergangs")
    c.setFont(schriftart, 6)
    c.drawString(8.9*cm, 13.3*cm, u"(Verlauf, Bezeichnung des Betriebsteils, ggf. Beteiligung von Maschinen, Anlagen, Gefahrstoffen)")
    c.setFont(schriftart, 8)
    c.drawString(2.7*cm, 9.9*cm, u"Die Angaben beruhen auf der Schilderung")
    c.drawString(9.2*cm, 9.9*cm, u'der versicherten Person')
    c.drawString(12.9*cm, 9.9*cm, u'anderer Personen')
    c.drawString(3.1*cm, 9.5*cm, u'Verletzte Körperteile')
    c.drawString(11.6*cm, 9.5*cm, u'Art der Verletzung')
    c.drawString(3.1*cm, 8.8*cm, u'Wer hat von dem Unfall zuerst Kenntnis genommen?')
    c.setFont(schriftart, 6)
    c.drawString(9.8*cm, 8.8*cm, u'(Name, Anschrift)')
    c.setFont(schriftart, 8)
    c.drawString(13.9*cm, 8.8*cm, u'War diese Person Augenzeugin/Augenzeuge')
    c.drawString(13.9*cm, 8.5*cm, u'des Unfalls?')
    c.drawString(14.3*cm, 8.05*cm, 'Ja')
    c.drawString(16.42*cm, 8.05*cm, 'Nein')
    c.drawString(3.1*cm, 7.6*cm, 'Erstbehandlung')
    c.drawString(2.7*cm, 7.35*cm, 'Name und Anschrift der Ärztin/des Arztes oder des Krankenhauses')
    c.drawString(13.4*cm,7.6*cm, 'Beginn und Ende der Arbeitszeit')
    c.drawString(12.9*cm, 7.35*cm, 'der versicherten Person')
    c.drawString(12.9*cm, 6.7*cm, 'Beginn')
    c.drawString(14.15*cm, 7.05*cm, 'Stunde')
    c.drawString(15.35*cm, 7.05*cm, 'Minute')
    c.drawString(16.5*cm, 6.7*cm, 'Ende')
    c.drawString(17.55*cm, 7.05*cm, 'Stunde')
    c.drawString(18.75*cm, 7.05*cm, 'Minute')
    c.drawString(3.1*cm, 6.3*cm, u'Zum Unfallzeitpunkt beschäftigt/tätig als')
    c.drawString(12.25*cm, 6.3*cm, u'Seit wann bei dieser Tätigkeit?')
    c.drawString(16.6*cm, 6.3*cm, 'Monat')
    c.drawString(18.4*cm ,6.3*cm, 'Jahr')
    c.drawString(3.1*cm, 5.5*cm, u'In welchem Teil des Unternehmens ist die versicherte Person ständig tätig?')
    c.drawString(3.1*cm, 4.65*cm, u'Hat die versicherte Person die Arbeit eingestellt?')
    c.drawString(11.4*cm, 4.65*cm, 'Nein')
    c.drawString(13.4*cm, 4.65*cm, 'Sofort')
    c.drawString(14.65*cm, 4.65*cm, u'Später, am')
    c.drawString(16.55*cm, 4.65*cm, 'Tag')
    c.drawString(17.6*cm, 4.65*cm, 'Monat')
    c.drawString(18.75*cm, 4.65*cm, 'Stunde')
    c.drawString(3.1*cm, 3.85*cm, u'Hat die versicherte Person die Arbeit wieder aufgenommen?')
    c.drawString(11.4*cm, 3.85*cm, 'Nein')
    c.drawString(13.4*cm, 3.85*cm, u'Ja, am')
    c.drawString(15.35*cm, 3.9*cm, 'Tag')
    c.drawString(16.4*cm, 3.9*cm, 'Monat')
    c.drawString(18.4*cm, 3.9*cm, 'Jahr')
    c.drawString(3.2*cm, 1.95*cm, u'Datum')
    c.drawString(5*cm, 1.95*cm, u'Unternehmer/-in(Bevollmächtigte/-r)')
    c.drawString(11.2*cm, 1.95*cm, u'Betriebsrat(Personalrat)')
    c.drawString(15.4*cm, 1.95*cm, u'Telefon Nr. für Rückfragen')
   
    
    return c
    
def kundetopdf(c, kunde): 

    c.drawString(3*cm, 25.9*cm, kunde.get('name'))
    c.drawString(3*cm, 25.4*cm, kunde.get('anschrift'))
    c.drawString(3*cm, 24.9*cm, kunde.get('plz')) 
    c.drawString(4*cm, 24.9*cm, kunde.get('ort')) 

    return c 

def uvtopdf(c, uv):

    schriftart = "Helvetica"
    
    c.setFont(schriftart, 10)
    c.drawString(3*cm, 22.9*cm, uv.get('name'))
    c.drawString(3*cm, 22.3*cm, uv.get('anschrift')) 
    c.drawString(3*cm, 21.7*cm, uv.get('plz'))
    c.drawString(4.2*cm, 21.7*cm, uv.get('ort'))
    
    return c
        
def setcross(c,x,y):
    
    c.line(x*cm, y*cm, (x+0.3)*cm, (y+0.3)*cm)
    c.line(x*cm, (y+0.3)*cm, (x+0.3)*cm, y*cm)
       
    return c
    
def datatopdf(c, data):
    schriftart = "Helvetica"
   
    # Formular beschriftung 
    c.setFont(schriftart, 10)
    c.drawString(2.7*cm, 19.6*cm, data.get('name'))
    c.drawString(4*cm, 19.6*cm, data.get('vorname'))
    c.drawString(15.2*cm, 19.6*cm, data.get('tag')[0])
    c.drawString(15.8*cm, 19.6*cm, data.get('tag')[1])
    c.drawString(16.4*cm, 19.6*cm, data.get('monat')[0])
    c.drawString(17*cm, 19.6*cm, data.get('monat')[1])
    c.drawString(17.6*cm, 19.6*cm, data.get('jahr')[0])
    c.drawString(18.1*cm, 19.6*cm, data.get('jahr')[1])
    c.drawString(18.7*cm, 19.6*cm, data.get('jahr')[2])
    c.drawString(19.3*cm, 19.6*cm, data.get('jahr')[3])
    c.drawString(2.7*cm, 18.81*cm, data.get('strasse'))
    c.drawString(6.1*cm, 18.81*cm, data.get('hausnummer'))
    c.drawString(9.89*cm, 18.81*cm, data.get('plz')[0])
    c.drawString(10.4*cm, 18.81*cm, data.get('plz')[1])
    c.drawString(11*cm, 18.81*cm, data.get('plz')[2])
    c.drawString(11.6*cm, 18.81*cm, data.get('plz')[3])
    c.drawString(12.1*cm, 18.81*cm, data.get('plz')[4])
    c.drawString(12.8*cm, 18.81*cm, data.get('ort'))
    c.drawString(6.6*cm, 18.05*cm, data.get('staartangehoerigkeit'))
    c.drawString(4.45*cm, 14.8*cm, data.get('geldanspruch')[0])
    c.drawString(5*cm, 14.8*cm, data.get('geldanspruch')[1])
    c.drawString(8.3*cm, 14.85*cm, data.get('krankenkasse'))
    c.drawString(6.1*cm, 13.7*cm, data.get('tag1')[0])
    c.drawString(6.6*cm, 13.7*cm, data.get('tag1')[1])
    c.drawString(7.2*cm, 13.7*cm, data.get('monat1')[0])
    c.drawString(7.7*cm, 13.7*cm, data.get('monat1')[1])
    c.drawString(8.3*cm, 13.7*cm, data.get('jahr1')[0])
    c.drawString(8.9*cm, 13.7*cm, data.get('jahr1')[1])
    c.drawString(9.5*cm, 13.7*cm, data.get('jahr1')[2])
    c.drawString(10*cm, 13.7*cm, data.get('jahr1')[3])
    c.drawString(10.7*cm, 13.7*cm, data.get('stunde')[0])
    c.drawString(11.2*cm, 13.7*cm, data.get('stunde')[1])
    c.drawString(11.85*cm, 13.7*cm, data.get('minute')[0])
    c.drawString(12.4*cm, 13.7*cm, data.get('minute')[1])
    c.drawString(13.2*cm, 13.8*cm, data.get('unfallort'))
    c.drawString(2.7*cm, 9.15*cm, data.get('koerperteile'))
    c.drawString(11.5*cm, 9.15*cm, data.get('verlaetzung'))
    c.drawString(2.7*cm, 8.2*cm, data.get('unallzeuge'))
    c.drawString(2.7*cm, 6.7*cm, data.get('arzt'))
    c.drawString(14.2*cm, 6.7*cm, data.get('stunde1')[0])
    c.drawString(14.8*cm, 6.7*cm, data.get('stunde1')[1])
    c.drawString(15.4*cm, 6.7*cm, data.get('minute1')[0])
    c.drawString(16*cm, 6.7*cm, data.get('minute1')[1])
    c.drawString(17.6*cm, 6.7*cm, data.get('stunde2')[0])
    c.drawString(18.2*cm, 6.7*cm, data.get('stunde2')[1])
    c.drawString(18.8*cm, 6.7*cm, data.get('minute2')[0])
    c.drawString(19.4*cm, 6.7*cm, data.get('minute2')[1])
    c.drawString(2.7*cm, 5.9*cm, data.get('taetig'))
    c.drawString(11.9*cm, 5.9*cm, data.get('taetig1'))
    c.drawString(16.6*cm, 5.9*cm, data.get('monat2')[0])
    c.drawString(17.2*cm, 5.9*cm, data.get('monat2')[1])
    c.drawString(17.8*cm, 5.9*cm, data.get('jahr2')[0])
    c.drawString(18.35*cm, 5.9*cm, data.get('jahr2')[1])
    c.drawString(18.9*cm, 5.9*cm, data.get('jahr2')[2])
    c.drawString(19.4*cm, 5.9*cm, data.get('jahr2')[3])
    c.drawString(2.7*cm, 5.1*cm, data.get('taetig1'))

    
    #If Abfragen
    
    if data.get('geschlecht') == 'm':
       setcross(c,x=2.7,y=18)
    else:
       setcross(c,x=4.7,y=18)
       
    if data.get('leiarbeitnehmer') == 'j':
       setcross(c,x=12.7,y=18)
    else:
       setcross(c,x=14.7,y=18)
       
    if data.get('azubi') == 'j':
       setcross(c,x=2.7,y=17.2)
    else:
       setcross(c,x=4.7,y=17.2)
       
    if data.get('versicherte') == 'unternehmer':
       setcross(c,x=10.5,y=17.5)
    
    elif data.get('versicherte') == 'gf':
        setcross(c,x=10.5,y=16.9)
        
    elif data.get('versicherte') == 'verheiratet':
        setcross(c,x=14.7,y=17.5)
        setcross(c,x=15.4,y=16.9)
        
    elif data.get('versicherte') == 'lebenspatnher':
        setcross(c,x=14.7,y=17.5)
        setcross(c,x=15.4,y=16.5)
        
    elif data.get('versicherte') == 'verwandt':
        setcross(c,x=14.7,y=17.5)
        setcross(c,x=15.4,y=15.8)
        
    if data.get('unfalltod') == 'n':
       setcross(c,x=4.7,y=13.85)
    else:
       setcross(c,x=2.7,y=13.85)
       
    if data.get('versicherten Person') == 'geschuetzt':
       setcross(c,x=8.8,y=9.9)
    else:
       setcross(c,x=12.4,y=9.9)
       
    if data.get('augenzeuge') == 'j':
       setcross(c,x=13.9,y=8)
    elif data.get('augenzeuge') == 'n':
       setcross(c,x=16,y=8)
       
    if data.get('einstellung') == 'n':
       setcross(c,x=11,y=4.6)
    elif data.get('einstellung') == 'sofort':
       setcross(c,x=13,y=4.6)
    else:
        c.drawString(16.4*cm, 4.3*cm, data.get('einstellung')[0])
        c.drawString(17.05*cm, 4.3*cm, data.get('einstellung')[1])
        c.drawString(17.6*cm, 4.3*cm, data.get('einstellung')[2])
        c.drawString(18.2*cm, 4.3*cm, data.get('einstellung')[3])
        c.drawString(18.8*cm, 4.3*cm, data.get('einstellung')[4])
        c.drawString(19.4*cm, 4.3*cm, data.get('einstellung')[5])  

    if data.get('aufnahme') == 'n':
       setcross(c,x=11,y=3.8)
    else:
        setcross(c,x=13,y=3.8)
        
        c.drawString(15.2*cm, 3.5*cm, data.get('aufnahme')[0])
        c.drawString(15.8*cm, 3.5*cm, data.get('aufnahme')[1])
        c.drawString(16.4*cm, 3.5*cm, data.get('aufnahme')[2])
        c.drawString(17*cm, 3.5*cm, data.get('aufnahme')[3])
        c.drawString(17.6*cm, 3.5*cm, data.get('aufnahme')[4])
        c.drawString(18.2*cm, 3.5*cm, data.get('aufnahme')[5])
        c.drawString(18.8*cm, 3.5*cm, data.get('aufnahme')[6])
        c.drawString(19.4*cm, 3.5*cm, data.get('aufnahme')[7])
       
       
    return c
    
def texttozeilen(blindtext):
    textneu= blindtext.split(' ')
    zeilen =[]
    zeile = ''
    for i in textneu:
        test = zeile + i
        if len(test)> 100:
            zeilen.append(zeile)
            zeile = ''
        elif len(test) == 100:
            zeile = zeile + ' ' + i
            zeilen.append(zeile)
            zeile = ''
        else:
            zeile = zeile + ' ' + i
    zeilen.append(zeile)
    return zeilen
    
def zeilentopdf(c, zeilen):
    
    x=2.6
    y=12.9
    diff=0.3
    for i in range(9):
        c.drawString(x*cm ,y*cm, zeilen[i])
        y=y-diff
        
    return c
   
def savepdf(c):

    # seitenumbruch
    c.showPage()
    #Dokument Speichern
    c.save()
	
if __name__=="__main__":
    c = createpdf()
    c = drawpdf(c)
    kunde = {'name':u'NOVARETO','anschrift':'Karolinenstraße 17','plz':'90763,','ort':u'Fürth'}
    uv = {'name':u'Kommunaler Unfallversicherungsträger Bayern','anschrift':u'Ungererstraße 71','plz':'80805,','ort':'München'}
    data = {'name':u'Paul','vorname':u'Pascal Daniel','tag':'02','monat':'11','jahr':'2000','strasse':'Poppenreuther Str.',
    'hausnummer':'13','plz':'90765','ort':'Fürth(Bay)','geschlecht':'m','staartangehoerigkeit':'Deutschland','leiarbeitnehmer':'n','geldanspruch':'06',
    'azubi':'j','versicherte':'unternehmer',
    'krankenkasse':'AOK, Pascal Paul, 90765, Fürth','unfalltod':'n','tag1':'12','monat1':'12','jahr1':'2018','stunde':'11','minute':'50',
    'versicherten Person':'geschuetzt','unfallort':'Karolinenstraße 17 90765 Fürth','koerperteile':'Rechter Arm','verlaetzung':'Knochenbruch',
    'unallzeuge':'Lars Walther Karolinenstraße 17','augenzeuge':'j','arzt':'Dr.Luga, Dr.Roming Erlanger Str. 34',
    'stunde1':'08','minute1':'30','stunde2':'12','minute2':'15','taetig':'Fachinformatiker',
    'monat2':'12','monat2':'12','jahr2':'2018','taetig1':'Fachinformatiker','einstellung':'sofort','aufnahme':'n'}
    c = kundetopdf(c, kunde)
    c = uvtopdf(c, uv)
    blindtext = u"""\
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.   

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam diam dolore dolores duo eirmod eos erat, et nonumy sed tempor et et invidunt justo labore Stet clita ea et gubergren, kasd magna no rebum. sanctus sea sed takimata ut vero voluptua. est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat.   

Consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus.   

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.   

Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.   

Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.   

Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo    
    """
    c = datatopdf(c, data)
    zeilen = texttozeilen(blindtext)
    print len(zeilen)
    c = zeilentopdf(c, zeilen)
    savepdf(c) 