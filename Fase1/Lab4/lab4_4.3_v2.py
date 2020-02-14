#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Lo de arriba es para que los IDE conozcan en que esta escrito este codigo 
###########################################################
# Puedes encontrar este codigo como objeto_ej4.py en:    ##
# https://sites.google.com/saber.uis.edu.co/comdig/sw    ##
###########################################################
###           IMPORTACION DE LIBRERIAS                  ###
###########################################################
# Libreria obligatoria
from gnuradio import gr

# Librerias particulares
from gnuradio import analog
from gnuradio import blocks
from gnuradio.filter import firdes

# Librerias para poder incluir graficas tipo QT
from gnuradio import qtgui
from PyQt4 import Qt # si no se acepta PyQt4 cambie PyQt4 por PyQt5
import sys, sip

# Ahora debes importar tu libreria. A continuacion suponemos que tu libreria ha sido
# guardada en un archivo llamado lib_comdig_code.py
import Library_GNU as misbloques


###########################################################
###           LA CLASE DEL FLUJOGRAMA                   ###
###########################################################
class flujograma(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)

        ################################################
        ###   EL FLUJOGRAMA                          ###
        ################################################

        # Las variables usadas en el flujograma
        samp_rate = 32000
        f = 4500
        N = 512
        # Los bloques
        self.src = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f, 1, 0)
        self.src2 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 2*f, 1, 0)
        self.nse = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1)
        self.nse2 = analog.noise_source_f(analog.GR_GAUSSIAN, 0.12)
        self.add = misbloques.e_add_ff(1.0)
        self.add2 = misbloques.e_add_ff(1.0)
        self.snk = qtgui.time_sink_f(
            N, # numero de muestras en la ventana del osciloscopio
            samp_rate,
            "senal con Ruido", # nombre que aparece en la grafica
            2 # Nuemero de entradas del osciloscopio
        )
        self.str2vec = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.str2vec2 = blocks.stream_to_vector(gr.sizeof_float*1, N)
        self.e_fft = misbloques.e_vector_fft_ff(N)
        self.e_fft2 = misbloques.e_vector_fft_ff(N)
        self.vsnk = qtgui.vector_sink_f(
            N,
            -samp_rate/2.,
            samp_rate/N,
            "Frecuencia [Hz]",
            "Magnitud",
            "FT en Magnitud",
            2 # Number of inputs
        )
        self.vsnk.enable_autoscale(True)
        # Las conexiones
        self.connect(self.src, (self.add, 0))
        self.connect(self.nse, (self.add, 1))
        self.connect(self.src2, (self.add2, 0))
        self.connect(self.nse2, (self.add2, 1))
        self.connect(self.add, (self.snk,0))
        self.connect(self.add, self.str2vec)
        self.connect(self.add2, (self.snk,1))
        self.connect(self.add2, self.str2vec2)
        self.connect(self.str2vec, self.e_fft)
        self.connect(self.str2vec2, self.e_fft2)
        self.connect(self.e_fft, (self.vsnk,0))
        self.connect(self.e_fft2, (self.vsnk,1))

        # La configuracion para graficar
        self.pyobj = sip.wrapinstance(self.vsnk.pyqwidget(), Qt.QWidget)
        #self.pyobj = sip.wrapinstance(self.snk.pyqwidget(), Qt.QWidget)
        self.pyobj.show()

###########################################################
###                LA CLASE PRINCIPAL                   ###
###########################################################
def main():
    # Para que lo nuestro sea considerado una aplicación tipo QT GUI
    qapp = Qt.QApplication(sys.argv)
    simulador_de_la_envolvente_compleja = flujograma()
    simulador_de_la_envolvente_compleja.start()
    # Para arranque la parte grafica
    qapp.exec_()
    simulador_de_la_envolvente_compleja.stop()

# como el main lo hemos puesto como una funcion, ahora hay que llamarla
# podriamos escibir simplemete main(), pero es mas profesional asi:
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass