#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 

# from gnuradio import gr
from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import cmath
import math
import numpy
import random
import sys

class usrp2usrp1_cc(gr.hier_block2):
    """
    Este bloque permite imitar la conexion entre conexion inalambrica entre dos usrp, lo cual equivale a un un canal inalambrico con parametros de filtrado, offset de tiempo (Toffset, dado en tiempo discreto), offset de frecuencia (Foffset, dado en Hz), offset de fase (Phoffset, dado en radianes), ancho de banda (BW, dado en Hz), nivel de ruido (Vruido, dado en volts), atenuacion (Katt)  
    """
    def __init__(self, samp_rate, Am, Toffset,Foffset, Vruido, Katt, Phoffset, BW):
        gr.hier_block2.__init__(self,
            "usrp2usrp1_cc",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature

            # Define blocks and connect them
#            self.connect()
        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate
        self.Vruido = Vruido
        self.Toffset = Toffset
        self.Phoffset = Phoffset
        self.Katt = Katt
        self.Foffset = Foffset
        self.BW = BW
        self.Am = Am

        ##################################################
        # Blocks
        ##################################################
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, BW, BW/4, firdes.WIN_HAMMING, 6.76))
#        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
#        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1./Katt+0j, ))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, Toffset)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Foffset, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, Vruido, 42)
        self.analog_const_source_x_1_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cmath.exp(1j * Phoffset))
#        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, -Am/2.+0j)
        self.analog_const_source_x_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 0.+0j)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.analog_const_source_x_1_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 0)) 
   
#        self.connect((self.blocks_add_xx_0, 0), (self.blocks_null_sink_0, 0)) 
        self.connect((self.blocks_add_xx_0, 0), self) 
   
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1)) 
   
#        self.connect((self.blocks_null_source_0, 0), (self.blocks_delay_0, 0))    
        self.connect(self, (self.blocks_delay_0, 0))    

        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OOK_Decisor_vhi")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_BW((self.samp_rate/2)/1.5)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW/4, firdes.WIN_HAMMING, 6.76))

    def get_Vruido(self):
        return self.Vruido

    def set_Vruido(self, Vruido):
        self.Vruido = Vruido
        self.analog_noise_source_x_0.set_amplitude(self.Vruido)

    def get_Toffset(self):
        return self.Toffset

    def set_Toffset(self, Toffset):
        self.Toffset = Toffset
        self.blocks_delay_0.set_dly(self.Toffset)

    def get_Phoffset(self):
        return self.Phoffset

    def set_Phoffset(self, Phoffset):
        self.Phoffset = Phoffset
        self.analog_const_source_x_1_0.set_offset(cmath.exp(1j * self.Phoffset))

    def get_Katt(self):
        return self.Katt

    def set_Katt(self, Katt):
        self.Katt = Katt
        self.blocks_multiply_const_vxx_0.set_k((1./self.Katt+0j, ))

    def get_Foffset(self):
        return self.Foffset

    def set_Foffset(self, Foffset):
        self.Foffset = Foffset
        self.analog_sig_source_x_0.set_frequency(self.Foffset)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.BW, self.BW/4, firdes.WIN_HAMMING, 6.76))

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
#        self.analog_const_source_x_0_0.set_offset(-self.Am/2.+0j)
        self.analog_const_source_x_0_0.set_offset(0.+0j)

