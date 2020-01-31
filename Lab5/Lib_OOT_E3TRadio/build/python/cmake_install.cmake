# Install script for directory: /home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python

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

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/__init__.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/sumador.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/sum_vectors_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/amplificador_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/max_xx.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/diezmador_cc.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/Zero_Order_Hold.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/unipolar_to_bipolar_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/FFT_SDRCol_triangular.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/Averager_onate.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/time_averager_jesus.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/fft_jesus.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/averager.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/vector_average_hob.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/ej_amplificador_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/acumulador_truncado_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/decisor_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/decisor_fb.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/decisor_fi.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/delay_hob_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/v_delay.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/diezmoppenh3_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/diezma_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/usrp2usrp1_cc.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/zero_order_hold2_cc.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/zero_order_hold_bb.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/ifft_jesus.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/retrazo_ff.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/retrazo_cc.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/e_canal_BER.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/e_BERtool.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/mean_meter.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/power_meter.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/vec_diagrama_ojo2_f.py"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/python/vec_diagrama_ojo_f.py"
    )
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/__init__.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/sumador.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/sum_vectors_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/amplificador_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/max_xx.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezmador_cc.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/Zero_Order_Hold.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/unipolar_to_bipolar_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/FFT_SDRCol_triangular.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/Averager_onate.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/time_averager_jesus.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/fft_jesus.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/averager.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vector_average_hob.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/ej_amplificador_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/acumulador_truncado_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_fb.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_fi.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/delay_hob_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/v_delay.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezmoppenh3_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezma_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/usrp2usrp1_cc.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/zero_order_hold2_cc.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/zero_order_hold_bb.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/ifft_jesus.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/retrazo_ff.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/retrazo_cc.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/e_canal_BER.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/e_BERtool.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/mean_meter.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/power_meter.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vec_diagrama_ojo2_f.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vec_diagrama_ojo_f.pyc"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/__init__.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/sumador.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/sum_vectors_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/amplificador_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/max_xx.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezmador_cc.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/Zero_Order_Hold.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/unipolar_to_bipolar_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/FFT_SDRCol_triangular.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/Averager_onate.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/time_averager_jesus.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/fft_jesus.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/averager.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vector_average_hob.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/ej_amplificador_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/acumulador_truncado_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_fb.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/decisor_fi.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/delay_hob_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/v_delay.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezmoppenh3_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/diezma_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/usrp2usrp1_cc.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/zero_order_hold2_cc.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/zero_order_hold_bb.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/ifft_jesus.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/retrazo_ff.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/retrazo_cc.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/e_canal_BER.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/e_BERtool.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/mean_meter.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/power_meter.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vec_diagrama_ojo2_f.pyo"
    "/home/onchip/Documents/Alex/2019-2/ComuII/B1A.G6_LAB_COMU2/Lab5/comdig_Lib_OOT_E3TRadio/build/python/vec_diagrama_ojo_f.pyo"
    )
endif()

