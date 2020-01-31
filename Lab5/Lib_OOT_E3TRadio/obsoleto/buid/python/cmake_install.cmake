# Install script for directory: /home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/__init__.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/sumador.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/sum_vectors_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/amplificador_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/max_xx.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/diezmador_cc.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/Zero_Order_Hold.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/unipolar_to_bipolar_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/FFT_SDRCol_triangular.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/Averager_onate.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/time_averager_jesus.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/fft_jesus.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/averager.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/vector_average_hob.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/ej_amplificador_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/acumulador_truncado_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/decisor_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/decisor_fb.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/decisor_fi.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/delay_hob_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/v_delay.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/diezmoppenh3_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/diezma_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/usrp2usrp1_cc.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/zero_order_hold2_cc.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/zero_order_hold_bb.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/ifft_jesus.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/retrazo_ff.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/retrazo_cc.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/e_canal_BER.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/e_BERtool.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/mean_meter.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/power_meter.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/vec_diagrama_ojo2_f.py"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/python/vec_diagrama_ojo_f.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/__init__.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/sumador.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/sum_vectors_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/amplificador_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/max_xx.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezmador_cc.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/Zero_Order_Hold.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/unipolar_to_bipolar_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/FFT_SDRCol_triangular.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/Averager_onate.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/time_averager_jesus.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/fft_jesus.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/averager.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vector_average_hob.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/ej_amplificador_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/acumulador_truncado_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_fb.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_fi.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/delay_hob_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/v_delay.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezmoppenh3_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezma_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/usrp2usrp1_cc.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/zero_order_hold2_cc.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/zero_order_hold_bb.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/ifft_jesus.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/retrazo_ff.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/retrazo_cc.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/e_canal_BER.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/e_BERtool.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/mean_meter.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/power_meter.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vec_diagrama_ojo2_f.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vec_diagrama_ojo_f.pyc"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/__init__.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/sumador.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/sum_vectors_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/amplificador_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/max_xx.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezmador_cc.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/Zero_Order_Hold.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/unipolar_to_bipolar_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/FFT_SDRCol_triangular.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/Averager_onate.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/time_averager_jesus.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/fft_jesus.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/averager.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vector_average_hob.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/ej_amplificador_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/acumulador_truncado_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_fb.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/decisor_fi.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/delay_hob_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/v_delay.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezmoppenh3_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/diezma_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/usrp2usrp1_cc.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/zero_order_hold2_cc.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/zero_order_hold_bb.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/ifft_jesus.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/retrazo_ff.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/retrazo_cc.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/e_canal_BER.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/e_BERtool.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/mean_meter.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/power_meter.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vec_diagrama_ojo2_f.pyo"
    "/home/uis-e3t/MisGits/comdig_Lib_OOT_E3TRadio/buid/python/vec_diagrama_ojo_f.pyo"
    )
endif()

