# Install script for directory: /home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python

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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/__init__.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/sumador.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/sum_vectors_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/amplificador_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/max_xx.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/diezmador_cc.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/Zero_Order_Hold.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/unipolar_to_bipolar_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/FFT_SDRCol_triangular.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/Averager_onate.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/time_averager_jesus.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/fft_jesus.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/averager.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/vector_average_hob.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/ej_amplificador_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/acumulador_truncado_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/decisor_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/decisor_fb.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/decisor_fi.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/delay_hob_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/v_delay.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/diezmoppenh3_ff.py"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/diezma_ff.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/E3TRadio" TYPE FILE FILES
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/__init__.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/sumador.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/sum_vectors_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/amplificador_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/max_xx.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezmador_cc.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/Zero_Order_Hold.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/unipolar_to_bipolar_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/FFT_SDRCol_triangular.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/Averager_onate.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/time_averager_jesus.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/fft_jesus.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/averager.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/vector_average_hob.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/ej_amplificador_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/acumulador_truncado_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_fb.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_fi.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/delay_hob_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/v_delay.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezmoppenh3_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezma_ff.pyc"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/__init__.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/sumador.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/sum_vectors_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/amplificador_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/max_xx.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezmador_cc.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/Zero_Order_Hold.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/unipolar_to_bipolar_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/FFT_SDRCol_triangular.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/Averager_onate.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/time_averager_jesus.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/fft_jesus.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/averager.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/vector_average_hob.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/ej_amplificador_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/acumulador_truncado_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_fb.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/decisor_fi.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/delay_hob_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/v_delay.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezmoppenh3_ff.pyo"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/python/python/diezma_ff.pyo"
    )
endif()

