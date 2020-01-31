#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan 31 17:06:06 2020
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
from b_Canal_AWGN_ff import b_Canal_AWGN_ff  # grc-generated hier_block
from b_PCM_Encoder_Bb import b_PCM_Encoder_Bb  # grc-generated hier_block
from b_PSD import b_PSD  # grc-generated hier_block
from b_unipolar2bipolar_ff import b_unipolar2bipolar_ff  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import E3TRadio
import math
import sip
import wform  # embedded python module


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.Sps = Sps = 8
        self.Rb = Rb = 12000
        self.samp_rate = samp_rate = Rb*Sps
        self.ntaps = ntaps = Sps*32
        self.Rolloff = Rolloff = 1.0
        self.run_stop = run_stop = True
        self.h = h = wform.rrcos(Sps,ntaps,Rolloff)
        self.W = W = Rb/2
        self.Retardo_ojo = Retardo_ojo = 6
        self.Retardo_bits = Retardo_bits = 36
        self.Retardo_Timing = Retardo_Timing = 2
        self.Retardo_T4 = Retardo_T4 = 0
        self.Retardo_T3 = Retardo_T3 = 0
        self.No_dB = No_dB = -50
        self.Channel_BW = Channel_BW = samp_rate/2.
        self.Ab = Ab = 1.

        ##################################################
        # Blocks
        ##################################################
        self.menu = Qt.QTabWidget()
        self.menu_widget_0 = Qt.QWidget()
        self.menu_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_0)
        self.menu_grid_layout_0 = Qt.QGridLayout()
        self.menu_layout_0.addLayout(self.menu_grid_layout_0)
        self.menu.addTab(self.menu_widget_0, 'Eye Diagramm')
        self.menu_widget_1 = Qt.QWidget()
        self.menu_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_1)
        self.menu_grid_layout_1 = Qt.QGridLayout()
        self.menu_layout_1.addLayout(self.menu_grid_layout_1)
        self.menu.addTab(self.menu_widget_1, 'Bit Error')
        self.menu_widget_2 = Qt.QWidget()
        self.menu_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_2)
        self.menu_grid_layout_2 = Qt.QGridLayout()
        self.menu_layout_2.addLayout(self.menu_grid_layout_2)
        self.menu.addTab(self.menu_widget_2, 'PSD')
        self.menu_widget_3 = Qt.QWidget()
        self.menu_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_3)
        self.menu_grid_layout_3 = Qt.QGridLayout()
        self.menu_layout_3.addLayout(self.menu_grid_layout_3)
        self.menu.addTab(self.menu_widget_3, 'Time Scope in  Channel')
        self.menu_widget_4 = Qt.QWidget()
        self.menu_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.menu_widget_4)
        self.menu_grid_layout_4 = Qt.QGridLayout()
        self.menu_layout_4.addLayout(self.menu_grid_layout_4)
        self.menu.addTab(self.menu_widget_4, 'T4 versus T3 in time')
        self.top_grid_layout.addWidget(self.menu, 2,0,1,2)
        self._Retardo_bits_range = Range(0, Sps*10, 1, 36, 200)
        self._Retardo_bits_win = RangeWidget(self._Retardo_bits_range, self.set_Retardo_bits, 'Delay transmited signal to match with the received signal', "counter_slider", int)
        self.menu_grid_layout_1.addWidget(self._Retardo_bits_win, 0,0,1,1)
        self._Retardo_Timing_range = Range(0, Sps-1, 1, 2, 200)
        self._Retardo_Timing_win = RangeWidget(self._Retardo_Timing_range, self.set_Retardo_Timing, 'Timing', "counter_slider", int)
        self.menu_grid_layout_0.addWidget(self._Retardo_Timing_win, 0,0,1,1)
        self._Retardo_T4_range = Range(0, Sps, 1, 0, 200)
        self._Retardo_T4_win = RangeWidget(self._Retardo_T4_range, self.set_Retardo_T4, 'Delay to T4', "counter_slider", int)
        self.menu_grid_layout_4.addWidget(self._Retardo_T4_win, 0,0,1,1)
        self._Retardo_T3_range = Range(0, Sps, 1, 0, 200)
        self._Retardo_T3_win = RangeWidget(self._Retardo_T3_range, self.set_Retardo_T3, 'Delay to T3', "counter_slider", int)
        self.menu_grid_layout_4.addWidget(self._Retardo_T3_win, 0,1,1,1)
        self._No_dB_range = Range(-300, 0, 300/100., -50, 200)
        self._No_dB_win = RangeWidget(self._No_dB_range, self.set_No_dB, 'No (dB)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._No_dB_win, 1,1,1,1)
        self._Channel_BW_range = Range(0., samp_rate/2., (samp_rate/2)/100., samp_rate/2., 200)
        self._Channel_BW_win = RangeWidget(self._Channel_BW_range, self.set_Channel_BW, 'Channel_BW', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Channel_BW_win, 1,0,1,1)
        _run_stop_check_box = Qt.QCheckBox('Pause')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0,0,1,1)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
        	64, #size
        	Rb, #samp_rate
        	"Binary signal", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-0.1, 1.1)
        
        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()
        
        labels = ['in  T2', 'in R2', '', '', '',
                  '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_2_win, 3,0,1,2)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	8*Sps, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0_1_0.set_y_label('output of  waveform filter', "")
        
        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0.disable_legend()
        
        labels = ['', 'Info Received', '', '', '',
                  '', '', '', '', '']
        widths = [3, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [3, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_0_win, 2,0,1,2)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	8, #size
        	Rb, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0_1.set_y_label('input of the waveform filter', "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
        labels = ['', 'Info Received', '', '', '',
                  '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_win, 1,0,1,2)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
        	64/8, #size
        	Rb/8, #samp_rate
        	"Source Signal", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-128, 128)
        
        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()
        
        labels = ['in  T1 ', 'in  R1', '', '', '',
                  '', '', '', '', '']
        widths = [3, 3, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win, 2,0,1,2)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	10*Sps, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
        labels = ['Received Signal', '', '', '', '',
                  '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_0_win, 1,0,1,1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	10*Sps, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['Transmitted signal', '', '', '', '',
                  '', '', '', '', '']
        widths = [4, 1, 1, 1, 1,
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.menu_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_win, 0,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	60, #size
        	Rb, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1.5, 1.5)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['Info transmitted', 'Info Received', '', '', '',
                  '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
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
        self.menu_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,1)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(1, (h))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(Sps, (h))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 32e3,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1./Sps, ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab7/batman.jpg', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab7/batman_recieved.jpg', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, 20)
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_float*1, Retardo_T4)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, Retardo_T3)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, Retardo_bits)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='0101100110111011000101010111111010010011100010110100011010100011',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.b_unipolar2bipolar_ff_0_0 = b_unipolar2bipolar_ff()
        self.b_PSD_0_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='PSD in  R3',
            Ymax=1e-5,
            samp_rate=samp_rate,
        )
        self.menu_grid_layout_2.addWidget(self.b_PSD_0_0_0, 1,0,1,1)
        self.b_PSD_0_0 = b_PSD(
            Ensayos=1000000,
            N=1024,
            Titulo='PSD in T3',
            Ymax=1e-5,
            samp_rate=samp_rate,
        )
        self.menu_grid_layout_2.addWidget(self.b_PSD_0_0, 0,0,1,1)
        self.b_PCM_Encoder_Bb_0 = b_PCM_Encoder_Bb(
            code='0101100110111011000101010111111010010011100010110100011010100011',
            payload=128,
        )
        self.b_Canal_AWGN_ff_0 = b_Canal_AWGN_ff(
            BW=Channel_BW,
            Ch_NodB=No_dB,
            Ch_Toffset=0,
            samp_rate=samp_rate,
        )
        self._Retardo_ojo_range = Range(0, Sps*2, 1, 6, 200)
        self._Retardo_ojo_win = RangeWidget(self._Retardo_ojo_range, self.set_Retardo_ojo, 'Center the Eye by a delay', "counter_slider", int)
        self.top_grid_layout.addWidget(self._Retardo_ojo_win, 0,1,1,1)
        self.E3TRadio_diezma_ff_0 = E3TRadio.diezma_ff(Sps, Retardo_Timing)
        self.E3TRadio_decisor_ff_0 = E3TRadio.decisor_ff(0.)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.E3TRadio_decisor_ff_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.E3TRadio_decisor_ff_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.E3TRadio_diezma_ff_0, 0), (self.E3TRadio_decisor_ff_0, 0))    
        self.connect((self.b_Canal_AWGN_ff_0, 0), (self.interp_fir_filter_xxx_0_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.b_PCM_Encoder_Bb_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.b_unipolar2bipolar_ff_0_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.b_unipolar2bipolar_ff_0_0, 0), (self.blocks_delay_0_1_0, 0))    
        self.connect((self.b_unipolar2bipolar_ff_0_0, 0), (self.interp_fir_filter_xxx_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_char_to_float_0_0_0, 0))    
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_2, 0))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_2, 1))    
        self.connect((self.blocks_char_to_float_0_0_0, 0), (self.qtgui_time_sink_x_0_0_1, 1))    
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_0_0_1, 0))    
        self.connect((self.blocks_char_to_float_1, 0), (self.b_unipolar2bipolar_ff_0_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))    
        self.connect((self.blocks_delay_0_1_0, 0), (self.qtgui_time_sink_x_0_1, 0))    
        self.connect((self.blocks_delay_1, 0), (self.b_Canal_AWGN_ff_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.b_PCM_Encoder_Bb_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_char_to_float_0_1, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blks2_packet_decoder_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.E3TRadio_diezma_ff_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.b_PSD_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_char_to_float_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.b_PSD_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_delay_0_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.blocks_delay_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_samp_rate(self.Rb*self.Sps)
        self.set_h(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))
        self.set_ntaps(self.Sps*32)
        self.blocks_multiply_const_vxx_0.set_k((1./self.Sps, ))

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb
        self.set_samp_rate(self.Rb*self.Sps)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.Rb)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.Rb/8)
        self.qtgui_time_sink_x_0.set_samp_rate(self.Rb)
        self.set_W(self.Rb/2)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_Channel_BW(self.samp_rate/2.)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.b_PSD_0_0_0.set_samp_rate(self.samp_rate)
        self.b_PSD_0_0.set_samp_rate(self.samp_rate)
        self.b_Canal_AWGN_ff_0.set_samp_rate(self.samp_rate)

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_h(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))

    def get_Rolloff(self):
        return self.Rolloff

    def set_Rolloff(self, Rolloff):
        self.Rolloff = Rolloff
        self.set_h(wform.rrcos(self.Sps,self.ntaps,self.Rolloff))

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        if self.run_stop: self.start()
        else: self.stop(); self.wait()
        self._run_stop_callback(self.run_stop)

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.interp_fir_filter_xxx_0_0.set_taps((self.h))
        self.interp_fir_filter_xxx_0.set_taps((self.h))

    def get_W(self):
        return self.W

    def set_W(self, W):
        self.W = W

    def get_Retardo_ojo(self):
        return self.Retardo_ojo

    def set_Retardo_ojo(self, Retardo_ojo):
        self.Retardo_ojo = Retardo_ojo

    def get_Retardo_bits(self):
        return self.Retardo_bits

    def set_Retardo_bits(self, Retardo_bits):
        self.Retardo_bits = Retardo_bits
        self.blocks_delay_0.set_dly(self.Retardo_bits)

    def get_Retardo_Timing(self):
        return self.Retardo_Timing

    def set_Retardo_Timing(self, Retardo_Timing):
        self.Retardo_Timing = Retardo_Timing
        self.E3TRadio_diezma_ff_0.set_ka(self.Retardo_Timing)

    def get_Retardo_T4(self):
        return self.Retardo_T4

    def set_Retardo_T4(self, Retardo_T4):
        self.Retardo_T4 = Retardo_T4
        self.blocks_delay_0_1_0.set_dly(self.Retardo_T4)

    def get_Retardo_T3(self):
        return self.Retardo_T3

    def set_Retardo_T3(self, Retardo_T3):
        self.Retardo_T3 = Retardo_T3
        self.blocks_delay_0_1.set_dly(self.Retardo_T3)

    def get_No_dB(self):
        return self.No_dB

    def set_No_dB(self, No_dB):
        self.No_dB = No_dB
        self.b_Canal_AWGN_ff_0.set_Ch_NodB(self.No_dB)

    def get_Channel_BW(self):
        return self.Channel_BW

    def set_Channel_BW(self, Channel_BW):
        self.Channel_BW = Channel_BW
        self.b_Canal_AWGN_ff_0.set_BW(self.Channel_BW)

    def get_Ab(self):
        return self.Ab

    def set_Ab(self, Ab):
        self.Ab = Ab


def main(top_block_cls=top_block, options=None):

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
