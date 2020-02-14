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

class vector_average_hob(gr.sync_block):
    """
    docstring for block
    """

    def __init__(self, N, Nensayos):
        self.N=N
        self.Nensayos=Nensayos
        self.med=numpy.empty(N)
        self.count=0
    
        gr.sync_block.__init__(self, name="vector_average_hob", in_sig=[(numpy.float32, N)], out_sig=[(numpy.float32, N)])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        if self.count < self.Nensayos:
            self.count += 1	
        for i in range(0,self.N):
            self.med[i] = self.med[i]*(self.count-1)/self.count+in0[i]/self.count
        out[:]=self.med

        return len(output_items[0])

