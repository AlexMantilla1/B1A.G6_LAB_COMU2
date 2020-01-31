# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    sumador.py
    sum_vectors_ff.py
    amplificador_ff.py
    max_xx.py
    diezmador_cc.py
    Zero_Order_Hold.py
    unipolar_to_bipolar_ff.py
    FFT_SDRCol_triangular.py
    Averager_onate.py
    time_averager_jesus.py
    fft_jesus.py
    averager.py
    vector_average_hob.py
    ej_amplificador_ff.py
    acumulador_truncado_ff.py
    decisor_ff.py
    decisor_fb.py
    decisor_fi.py
    delay_hob_ff.py
    v_delay.py
    diezmoppenh3_ff.py
    diezma_ff.py
    usrp2usrp1_cc.py
    zero_order_hold2_cc.py
    zero_order_hold_bb.py
    ifft_jesus.py
    retrazo_ff.py
    retrazo_cc.py
    e_canal_BER.py
    e_BERtool.py
    mean_meter.py
    power_meter.py
    vec_diagrama_ojo2_f.py
    vec_diagrama_ojo_f.py DESTINATION ${GR_PYTHON_DIR}/E3TRadio
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-E3TRadio)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_vector_average_hob ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_vector_average_hob.py)
GR_ADD_TEST(qa_ej_amplificador_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_ej_amplificador_ff.py)
GR_ADD_TEST(qa_acumulador_truncado_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_acumulador_truncado_ff.py)
GR_ADD_TEST(qa_decisor_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_decisor_ff.py)
GR_ADD_TEST(qa_decisor_fb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_decisor_fb.py)
GR_ADD_TEST(qa_decisor_fi ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_decisor_fi.py)
GR_ADD_TEST(qa_delay_hob_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_delay_hob_ff.py)
GR_ADD_TEST(qa_v_delay ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_v_delay.py)
GR_ADD_TEST(qa_diezmoppenh3_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_diezmoppenh3_ff.py)
GR_ADD_TEST(qa_diezma_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_diezma_ff.py)
GR_ADD_TEST(qa_usrp2usrp1_cc ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_usrp2usrp1_cc.py)
GR_ADD_TEST(qa_zero_order_hold2_cc ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_zero_order_hold2_cc.py)
GR_ADD_TEST(qa_zero_order_hold_bb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_zero_order_hold_bb.py)
GR_ADD_TEST(qa_ifft_jesus ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_ifft_jesus.py)
GR_ADD_TEST(qa_retrazo_ff ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_retrazo_ff.py)
GR_ADD_TEST(qa_retrazo_cc ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_retrazo_cc.py)
GR_ADD_TEST(qa_e_canal_BER ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_e_canal_BER.py)
GR_ADD_TEST(qa_e_BERtool ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_e_BERtool.py)
