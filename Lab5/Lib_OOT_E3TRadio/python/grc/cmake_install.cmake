# Install script for directory: /home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gnuradio/grc/blocks" TYPE FILE FILES
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_sumador.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_sum_vectors_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_amplificador_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_max_xx.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_diezmador_cc.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_Zero_Order_Hold.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_unipolar_to_bipolar_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_FFT_SDRCol_triangular.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_Averager_onate.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_time_averager_jesus.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_fft_jesus.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_averager.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_vector_average_hob.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_ej_amplificador_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_acumulador_truncado_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_decisor_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_decisor_fb.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_decisor_fi.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_delay_hob_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_v_delay.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_diezmoppenh3_ff.xml"
    "/home/hob/Dropbox/EnUbuntuFull/gr-E3TRadio/grc/E3TRadio_diezma_ff.xml"
    )
endif()

