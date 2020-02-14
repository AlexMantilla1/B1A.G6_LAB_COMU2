#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class diezmoppenh3_ff(gr.sync_block):
    """
    Realiza un diezmado al estilo Oppenheim. 
    N: es la distancia entre las muestras que no resultan diezmadas. De modo que son diezmadas N-1 muestras
    M: es la muestra donde inicia el diezmado. Puede ser visto como un retrazo.

    """
    def __init__(self, N,M):
        gr.sync_block.__init__(self,
            name="diezmoppenh3_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.N=N
        self.M=M
        self.count=N-M-1

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        for i in range(0,len(in0)):
            self.count +=1
            if self.count == self.N:
                out[i]=in0[i]
                self.count=0
            else:        
                out[i]=0.0
        return len(output_items[0])
    def set_ka(self, M):
        self.M=M



