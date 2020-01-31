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

class acumulador_truncado_ff(gr.sync_block):
    """ Es un acumulador que se resetea cada Nstop muestras
        Este bloque es hecho en la E3T de la UIS
    """
    def __init__(self, N):
        self.accum=0
        self.count=N    
        self.N=N
        gr.sync_block.__init__(self,
            name="acumulador_truncado_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        NN=len(in0)
        # <+signal processing here+>
#        print("vector de:  ", NN)
        for i in range (0,NN):
            self.count += 1 
            self.accum += in0[i]
            if self.count > self.N:
                self.count=1
                self.accum=in0[i]
            out[i]=self.accum

        return len(output_items[0])

