#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: BER Simulation
# Author: Example
# Description: Adjust the noise and constellation... see what happens!
# Generated: Sat Mar 21 05:31:53 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_Canal_simple_cc import b_Canal_simple_cc  # grc-generated hier_block
from b_FLL_tunner import b_FLL_tunner  # grc-generated hier_block
from b_quantizer_fb import b_quantizer_fb  # grc-generated hier_block
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import E3TRadio
import coding  # embedded python module
import math
import numpy
import random
import sip
import wform  # embedded python module


class ber_simulation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "BER Simulation")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("BER Simulation")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((digital.constellation_qpsk().points()), (), 4, 1).base()
        self.Constelacion = Constelacion = MiconstellationObject.points()
        self.samp_rate_audio = samp_rate_audio = 11000
        self.NbpS = NbpS = 8
        self.M = M = len(Constelacion)
        self.samp_rate_usrp_rx = samp_rate_usrp_rx = 100e6
        self.Rb = Rb = NbpS*samp_rate_audio
        self.Bps = Bps = int(math.log(M,2))
        self.samp_rate_to_usrp = samp_rate_to_usrp = int(samp_rate_usrp_rx/512)
        self.Rs = Rs = Rb/Bps
        self.ntaps = ntaps = 128
        self.fc = fc = 50e6
        self.distancia_m = distancia_m = 0.5
        self.Sps = Sps = int(math.floor(samp_rate_to_usrp/Rs))
        self.Rolloff = Rolloff = 0.5
        self.samp_rate = samp_rate = Rs*Sps
        self.run_stop = run_stop = True
        self.nfilts = nfilts = 32
        self.mapinverse = mapinverse = coding.inverse_map(Constelacion)
        self.mapdirect = mapdirect = coding.direct_map(Constelacion)
        self.h_rrc = h_rrc = wform.rrcos(Sps,ntaps,Rolloff)
        self.Vp = Vp = 1.
        self.Toffset = Toffset = int(Sps/2)
        self.TimeAligment = TimeAligment = 2
        self.T_observacion_potencia = T_observacion_potencia = 5
        self.Retardo_propag = Retardo_propag = int(ntaps/Sps)+1
        self.Retardo_Timing = Retardo_Timing = 0
        self.Ph_correction = Ph_correction = 0.802851455917392
        self.NnivelesQ = NnivelesQ = math.pow(2,NbpS)
        self.Ch_Phoffset = Ch_Phoffset = (numpy.pi)*2/8
        self.Ch_Loss_dB = Ch_Loss_dB = 32.4 + 20*numpy.log10(fc*1e-6) + 20*numpy.log10(distancia_m*1e-3)
        self.Ch_Freq_Offset_Hz = Ch_Freq_Offset_Hz = 100
        self.Ch_Fluctuacion_por = Ch_Fluctuacion_por = 50
        self.Ch_AWGN_dB = Ch_AWGN_dB = -120
        self.BW = BW = (Rs/2)*(1+Rolloff)

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, "Constelation Timing")
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, "Senal MPAM")
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, "PSD en R1a")
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, "Potencia Recibida")
        self.menu_widget_4 = Qt.QWidget()
        self.menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_4)
        self.menu_grid_layout_4 = Qt.QGridLayout()
        self.menu_layout_4.addLayout(self.menu_grid_layout_4)
        self.menu.addTab(self.menu_widget_4, "histograma Potencia recibida")
        self.top_grid_layout.addWidget(self.menu, 2,0,1,4)
        self._Toffset_range = Range(0, Sps-1, 1, int(Sps/2), 200)
        self._Toffset_win = RangeWidget(self._Toffset_range, self.set_Toffset, "Offset del Periodo de la portadora", "counter_slider", float)
        self.top_layout.addWidget(self._Toffset_win)
        self._TimeAligment_range = Range(0, Sps*20, 1, 2, 200)
        self._TimeAligment_win = RangeWidget(self._TimeAligment_range, self.set_TimeAligment, "TimeAligment", "counter_slider", int)
        self.top_grid_layout.addWidget(self._TimeAligment_win, 0,3,1,1)
        _run_stop_check_box = Qt.QCheckBox("Pause")
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate,
                decimation=samp_rate_to_usrp,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_to_usrp,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	int(samp_rate*T_observacion_potencia), #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Nivel de RF (dB)", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["Pr(dB)", "", "", "", "",
                  "", "", "", "", ""]
        units = ["dB", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -200)
            self.qtgui_number_sink_0.set_max(i, 200)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_number_sink_0_win, 0,0,1,1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	1024,
        	1024,
                -20,
                0,
        	"histograma de potencia recibida (en dB en el eje horizontal)",
        	1
        )
        
        self.qtgui_histogram_sink_x_0.set_update_time(1)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_4.addWidget(self._qtgui_histogram_sink_x_0_win, 0,0,1,1)
          
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["T1", "R1", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_0.addWidget(self._qtgui_const_sink_x_0_win, 1,0,1,1)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(Sps, (h_rrc))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self._distancia_m_range = Range(0.5, 10, 0.5, 0.5, 200)
        self._distancia_m_win = RangeWidget(self._distancia_m_range, self.set_distancia_m, "Distancia recorrida en metros", "counter_slider", float)
        self.top_layout.addWidget(self._distancia_m_win)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(Sps, 2*math.pi/100.0, (firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(Sps), Rolloff, ntaps*nfilts)), nfilts, nfilts/2, 1.5, 1)
        self.digital_map_bb_0_0 = digital.map_bb((mapinverse))
        self.digital_map_bb_0 = digital.map_bb((mapdirect))
        self.digital_diff_encoder_bb_0 = digital.diff_encoder_bb(M)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(M)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((MiconstellationObject.points()), 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/alexmantilla97/Documents/B1A.G6_LAB_COMU2/Fase3/Lab1/pract_Canal_Inalambrico/bush-clinton_debate_waffle.wav", True)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/alexmantilla97/Documents/B1A.G6_LAB_COMU2/Fase3/Lab1/pract_Canal_Inalambrico/bush-clinton_debate_waffle_recieved.wav", 1, samp_rate_audio, NbpS)
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_rms_xx_0 = blocks.rms_cf(0.1)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(Bps, gr.GR_LSB_FIRST)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((Vp/(NnivelesQ/2)/2, ))
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_char*1, TimeAligment)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.b_quantizer_fb_0 = b_quantizer_fb(
            NivelesQ=NnivelesQ,
            Vmax=Vp,
        )
        self.b_FLL_tunner_0 = b_FLL_tunner(
            ConstellationObject=MiconstellationObject,
        )
        self.b_Canal_simple_cc_0 = b_Canal_simple_cc(
            Ch_Loss_dB=Ch_Loss_dB,
            Ch_NodB=Ch_AWGN_dB,
            Ch_Phoffset=Ch_Phoffset,
            Ch_Toffset=Toffset,
            Fluctuacion=Ch_Fluctuacion_por,
            Foffset=Ch_Freq_Offset_Hz,
            T_fluct=M*1024,
            samp_rate=samp_rate_to_usrp,
        )
        self.audio_sink_0 = audio.sink(samp_rate_audio, "", True)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self._Retardo_propag_range = Range(0, Sps*200, 1, int(ntaps/Sps)+1, 200)
        self._Retardo_propag_win = RangeWidget(self._Retardo_propag_range, self.set_Retardo_propag, "Propagation delay compensation", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_propag_win, 1,0,1,1)
        self._Retardo_Timing_range = Range(0, Sps-1, 1, 0, 200)
        self._Retardo_Timing_win = RangeWidget(self._Retardo_Timing_range, self.set_Retardo_Timing, "Timing", "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_Timing_win, 0,1,1,1)
        self._Ph_correction_range = Range(-numpy.pi, numpy.pi, 2*numpy.pi/720., 0.802851455917392, 200)
        self._Ph_correction_win = RangeWidget(self._Ph_correction_range, self.set_Ph_correction, "PLL Phase", "counter_slider", float)
        self.top_grid_layout.addWidget(self._Ph_correction_win, 0,2,1,1)
        self.E3TRadio_mean_meter_0 = E3TRadio.mean_meter(0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_mean_meter_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.b_Canal_simple_cc_0, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.b_FLL_tunner_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.b_FLL_tunner_0, 0), (self.qtgui_const_sink_x_0, 1))    
        self.connect((self.b_quantizer_fb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.E3TRadio_mean_meter_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_histogram_sink_x_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_diff_encoder_bb_0, 0))    
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.b_quantizer_fb_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.interp_fir_filter_xxx_0_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_map_bb_0_0, 0))    
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.digital_diff_encoder_bb_0, 0), (self.digital_map_bb_0, 0))    
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx, 0))    
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_diff_decoder_bb_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.b_FLL_tunner_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.b_Canal_simple_cc_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_rms_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ber_simulation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject
        self.set_Constelacion(self.MiconstellationObject.points())
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.MiconstellationObject.points()))
        self.b_FLL_tunner_0.set_ConstellationObject(self.MiconstellationObject)

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))
        self.set_mapdirect(coding.direct_map(self.Constelacion))
        self.set_mapinverse(coding.inverse_map(self.Constelacion))

    def get_samp_rate_audio(self):
        return self.samp_rate_audio

    def set_samp_rate_audio(self, samp_rate_audio):
        self.samp_rate_audio = samp_rate_audio
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_NbpS(self):
        return self.NbpS

    def set_NbpS(self, NbpS):
        self.NbpS = NbpS
        self.set_NnivelesQ(math.pow(2,self.NbpS))
        self.set_Rb(self.NbpS*self.samp_rate_audio)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))
        self.b_Canal_simple_cc_0.set_T_fluct(self.M*1024)

    def get_samp_rate_usrp_rx(self):
        return self.samp_rate_usrp_rx

    def set_samp_rate_usrp_rx(self, samp_rate_usrp_rx):
        self.samp_rate_usrp_rx = samp_rate_usrp_rx
        self.set_samp_rate_to_usrp(int(self.samp_rate_usrp_rx/512))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_Rs(self.Rb/self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rs(self.Rb/self.Bps)

    def get_samp_rate_to_usrp(self):
        return self.samp_rate_to_usrp

    def set_samp_rate_to_usrp(self, samp_rate_to_usrp):
        self.samp_rate_to_usrp = samp_rate_to_usrp
        self.set_Sps(int(math.floor(self.samp_rate_to_usrp/self.Rs)))
        self.b_Canal_simple_cc_0.set_samp_rate(self.samp_rate_to_usrp)

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_BW((self.Rs/2)*(1+self.Rolloff))
        self.set_Sps(int(math.floor(self.samp_rate_to_usrp/self.Rs)))
        self.set_samp_rate(self.Rs*self.Sps)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_Retardo_propag(int(self.ntaps/self.Sps)+1)
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.Rolloff, self.ntaps*self.nfilts)))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.set_Ch_Loss_dB(32.4 + 20*numpy.log10(self.fc*1e-6) + 20*numpy.log10(self.distancia_m*1e-3))

    def get_distancia_m(self):
        return self.distancia_m

    def set_distancia_m(self, distancia_m):
        self.distancia_m = distancia_m
        self.set_Ch_Loss_dB(32.4 + 20*numpy.log10(self.fc*1e-6) + 20*numpy.log10(self.distancia_m*1e-3))

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_samp_rate(self.Rs*self.Sps)
        self.set_Retardo_propag(int(self.ntaps/self.Sps)+1)
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.Rolloff, self.ntaps*self.nfilts)))
        self.set_Toffset(int(self.Sps/2))

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff
        self.set_BW((self.Rs/2)*(1+self.Rolloff))
        self.set_h_rrc(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.Rolloff, self.ntaps*self.nfilts)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.update_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.Sps), self.Rolloff, self.ntaps*self.nfilts)))

    def get_mapinverse(self):
        return self.mapinverse

    def set_mapinverse(self, mapinverse):
        self.mapinverse = mapinverse

    def get_mapdirect(self):
        return self.mapdirect

    def set_mapdirect(self, mapdirect):
        self.mapdirect = mapdirect

    def get_h_rrc(self):
        return self.h_rrc

    def set_h_rrc(self, h_rrc):
        self.h_rrc = h_rrc
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.h_rrc))

    def get_Vp(self):
        return self.Vp

    def set_Vp(self, Vp):
        self.Vp = Vp
        self.b_quantizer_fb_0.set_Vmax(self.Vp)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2)/2, ))

    def get_Toffset(self):
        return self.Toffset

    def set_Toffset(self, Toffset):
        self.Toffset = Toffset
        self.b_Canal_simple_cc_0.set_Ch_Toffset(self.Toffset)

    def get_TimeAligment(self):
        return self.TimeAligment

    def set_TimeAligment(self, TimeAligment):
        self.TimeAligment = TimeAligment
        self.blocks_delay_0_0_0.set_dly(self.TimeAligment)

    def get_T_observacion_potencia(self):
        return self.T_observacion_potencia

    def set_T_observacion_potencia(self, T_observacion_potencia):
        self.T_observacion_potencia = T_observacion_potencia

    def get_Retardo_propag(self):
        return self.Retardo_propag

    def set_Retardo_propag(self, Retardo_propag):
        self.Retardo_propag = Retardo_propag

    def get_Retardo_Timing(self):
        return self.Retardo_Timing

    def set_Retardo_Timing(self, Retardo_Timing):
        self.Retardo_Timing = Retardo_Timing

    def get_Ph_correction(self):
        return self.Ph_correction

    def set_Ph_correction(self, Ph_correction):
        self.Ph_correction = Ph_correction

    def get_NnivelesQ(self):
        return self.NnivelesQ

    def set_NnivelesQ(self, NnivelesQ):
        self.NnivelesQ = NnivelesQ
        self.b_quantizer_fb_0.set_NivelesQ(self.NnivelesQ)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.Vp/(self.NnivelesQ/2)/2, ))

    def get_Ch_Phoffset(self):
        return self.Ch_Phoffset

    def set_Ch_Phoffset(self, Ch_Phoffset):
        self.Ch_Phoffset = Ch_Phoffset
        self.b_Canal_simple_cc_0.set_Ch_Phoffset(self.Ch_Phoffset)

    def get_Ch_Loss_dB(self):
        return self.Ch_Loss_dB

    def set_Ch_Loss_dB(self, Ch_Loss_dB):
        self.Ch_Loss_dB = Ch_Loss_dB
        self.b_Canal_simple_cc_0.set_Ch_Loss_dB(self.Ch_Loss_dB)

    def get_Ch_Freq_Offset_Hz(self):
        return self.Ch_Freq_Offset_Hz

    def set_Ch_Freq_Offset_Hz(self, Ch_Freq_Offset_Hz):
        self.Ch_Freq_Offset_Hz = Ch_Freq_Offset_Hz
        self.b_Canal_simple_cc_0.set_Foffset(self.Ch_Freq_Offset_Hz)

    def get_Ch_Fluctuacion_por(self):
        return self.Ch_Fluctuacion_por

    def set_Ch_Fluctuacion_por(self, Ch_Fluctuacion_por):
        self.Ch_Fluctuacion_por = Ch_Fluctuacion_por
        self.b_Canal_simple_cc_0.set_Fluctuacion(self.Ch_Fluctuacion_por)

    def get_Ch_AWGN_dB(self):
        return self.Ch_AWGN_dB

    def set_Ch_AWGN_dB(self, Ch_AWGN_dB):
        self.Ch_AWGN_dB = Ch_AWGN_dB
        self.b_Canal_simple_cc_0.set_Ch_NodB(self.Ch_AWGN_dB)

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW


def main(top_block_cls=ber_simulation, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
