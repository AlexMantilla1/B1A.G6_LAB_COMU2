#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: ej1
# Generated: Thu Sep 13 11:39:57 2018
##################################################

##################################################
# LO QUE HAY QUE IMPORTAR
##################################################
from gnuradio import gr, audio, analog, blocks
# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt4 import Qt # si no se acepta PyQt4 cambie PyQt4 por PyQt5
import sys, sip
#######################################################
# LA CLASE QUE DESCRIBE TODO EL FLUJOGRAMA
######################################################
class my_top_block(gr.top_block):        # hereda de gr.top_block
     def __init__(self): 
        gr.top_block.__init__(self)     # otra vez la herencia
        # Parámetros:
        ampl = 1
        size = 500
        sample_rate = 32000
        plotName = "Signals from src0 & src1 with AWGN"
        nconnections = 2
        fftsize = 512
        fc = 0
        bw = 1000
        plotFreqName = "adder0 & adder1 spectre"
        # Bloques:
        src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 800, ampl)  #Generador 0
        src1 = analog.sig_source_f(sample_rate, analog.GR_SQR_WAVE, 440, ampl*2, -ampl)  #Generador 1
        noise0 = analog.noise_source_f(analog.GR_GAUSSIAN,(ampl*0.1))           #Generador de ruido 0
        noise1 = analog.noise_source_f(analog.GR_GAUSSIAN,(ampl*0.1))           #Generador de ruido 1
        adder0 = blocks.add_ff()                                                #Sumador 0
        adder1 = blocks.add_ff()                                                #Sumador 1
        dst = audio.sink(sample_rate, "")                                       #Reproductor de audio
        self.snk = qtgui.time_sink_f(size,sample_rate,plotName,nconnections)    #Gracifa en tiempo
        self.snk.set_line_label(0,"Signal 0")                                           #Asignar nombre
        self.snk.set_line_label(1,"Signal 1")                                           #Asignar nombre
        self.fsnk = qtgui.freq_sink_f(fftsize,5,fc,bw,plotFreqName,nconnections)#Gracifa en frecuencia
        self.fsnk.set_line_label(0,"Signal 0")                                           #Asignar nombre
        self.fsnk.set_line_label(1,"Signal 1")                                           #Asignar nombre
        # Conecciones:
        self.connect(src0, (adder0, 0)); self.connect(noise0, (adder0, 1))     #src0 y noise0 a las entradas de adder0.
        self.connect(src1, (adder1, 0)); self.connect(noise1, (adder1, 1))     #src1 y noise1 a las entradas de adder1.
        self.connect(adder0, (dst, 0))                                          #adder0 al reproductor.
        self.connect(adder1, (dst, 1))                                          #adder1 al reproductor.
        self.connect(adder0, (self.snk, 0))                                     #adder0 al graficador de tiempo.
        self.connect(adder1, (self.snk, 1))                                     #adder1 al graficador de tiempo.
        self.connect(adder0, (self.fsnk, 0))                                    #adder0 al graficador de frecuencia.
        self.connect(adder1, (self.fsnk, 1))                                    #adder1 al graficador de frecuencia.
        # Para mostrar gráfica:
        pyWin = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        pyWin.show()
        pyWin2 = sip.wrapinstance(self.fsnk.pyqwidget(), Qt.QWidget)
        pyWin2.show()
#######################################################
# EL CÓDIGO PARA LLAMAR EL FLUJOGRAMA “my_top_block”
######################################################
def main():
    qapp = Qt.QApplication(sys.argv)
    myTop = my_top_block()
    myTop.start()
    qapp.exec_()
    myTop.stop()
if __name__ == "__main__":
    main()

#if __name__ == '__main__':
#    try:
#         my_top_block().run()
#    except [[KeyboardInterrupt]]:
#         pass
