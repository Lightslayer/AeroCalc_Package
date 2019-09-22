#!/usr/bin/env python
# -*- coding: utf-8 -*-

# version 0.20, 30 Jun 09

# % coverage.py -x test_std_atm.py
# % coverage.py -r -m ../std_atm.py
# Name         Stmts   Exec  Cover   Missing
# ------------------------------------------
# ../std_atm     286     88    30%   114-125, 128-130, 133, 140, 147, 155, 160, 166, 173, 181, 189-200, 253, 259-369, 372, 392-544, 546-564, 568-599, 637-638, 697, 702-710, 713-871, 873-875, 883-884, 932, 937-938, 963-966, 970-1033, 1052-1079, 1082, 1097, 1101-1121, 1132-1267

""" Test cases for std_atm module.
Run this script directly to do all the tests.
"""

# Done    1. 29 Jun 2009 - Ran 2to3 tool and fixed errors
#         2. 30 Jun 2009 - Manually fixed remaining python3.0 errors.  Works with python2.5, 2.6 and 3.0

import unittest
import sys

import aerocalc.std_atm as SA

# These tests require that default_units.py contain the following defaults:
# default_area_units = 'ft**2'
# default_power_units = 'hp'
# default_speed_units = 'kt'
# default_temp_units = 'C'
# default_weight_units = 'lb'
# default_press_units = 'in HG'
# default_density_units = 'lb/ft**3'
# default_length_units = 'ft'
# default_alt_units = default_length_units
# default_avgas_units = 'lb'


def RE(value, truth):
    """ Returns the absolute value of the relative error.
    """

    return abs((value - truth) / truth)


class Test_alt2temp(unittest.TestCase):

    def test_01(self):

        # check at -1000 ft

        T = round(SA.alt2temp(-1000), 2)
        self.assertEqual(T, 16.98)

    def test_02(self):

        # check deg K at 10 km

        T = round(SA.alt2temp(10, alt_units='km', temp_units='K'), 2)
        self.assertEqual(T, 223.15)

    def test_03(self):

        # check deg R at 19 km

        T = round(SA.alt2temp(19, alt_units='km', temp_units='R'), 2)
        self.assertEqual(T, 389.97)

    def test_04(self):

        # check deg F at 25,000 m
        # change order of units specifications

        T = round(SA.alt2temp(25000, temp_units='F', alt_units='m'), 2)
        self.assertEqual(T, -60.7)

    def test_05(self):

        # check at 40 km

        T = round(SA.alt2temp(40, alt_units='km'), 2)
        self.assertEqual(T, -22.1)

    def test_06(self):

        # check at 50 km

        T = round(SA.alt2temp(50, alt_units='km'), 2)
        self.assertEqual(T, -2.5)

    def test_07(self):

        # check at 60 km

        T = round(SA.alt2temp(60, alt_units='km'), 2)
        self.assertEqual(T, -27.7)

    def test_08(self):

        # check at 80 km

        T = round(SA.alt2temp(80, alt_units='km'), 2)
        self.assertEqual(T, -76.5)

    def test_09(self):

        # confirm out of range error

        self.assertRaises(ValueError, SA.alt2temp, 90, alt_units='km')


class Test_alt2temp_ratio(unittest.TestCase):

    def test_01(self):
        TR = SA.alt2temp_ratio(0)
        self.assertEqual(TR, 1)

    def test_02(self):
        TR = SA.alt2temp_ratio(10000)
        Truth = 268.338 / 288.15
        self.assertEqual(round(TR, 9), round(Truth, 9))

    def test_03(self):

        # test with different units

        TR = SA.alt2temp_ratio(71, alt_units='km')
        Truth = 214.65 / 288.15
        self.assertEqual(round(TR, 9), round(Truth, 9))


class Test_temp2isa(unittest.TestCase):

    def test_01(self):
        Value = SA.temp2isa(25, 0)
        Truth = 10
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):
        Value = SA.temp2isa(0, 10000, temp_units='F')
        Truth = -23.3384
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):
        Value = SA.temp2isa(233.15, 10000, temp_units='K', alt_units='m'
                            )
        Truth = 10
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_isa2temp(unittest.TestCase):

    def test_01(self):
        Value = SA.isa2temp(25, 0)
        Truth = 40
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):
        Value = SA.isa2temp(-10, 10000, temp_units='F')
        Truth = 13.3384
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):
        Value = SA.isa2temp(10, 10000, temp_units='K', alt_units='m')
        Truth = 233.15
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_alt2press_ratio(unittest.TestCase):

    def test_01(self):
        PR = SA.alt2press_ratio(0)
        self.assertEqual(PR, 1)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.alt2press_ratio(-1000)
        Truth = 2193.82 / 2116.22
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Truth values from NASA RP 1046

        Value = SA.alt2press_ratio(20000, alt_units='m')
        Truth = 5474.87 / 101325
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_alt2press(unittest.TestCase):

    def test_01(self):

        # Truth values from NASA RP 1046

        Value = SA.alt2press(5000)
        Truth = 24.8959
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        # test psf
        # Truth values from NASA RP 1046

        Value = SA.alt2press(49000, press_units='psf')
        Truth = 254.139
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # test pa and m
        # Truth values from NASA RP 1046

        Value = SA.alt2press(25000, alt_units='m', press_units='pa')
        Truth = 2511.01
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_04(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2press(39750, press_units='pa', alt_units='m')
        Truth = 287.14
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_05(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2press(49610, press_units='pa', alt_units='m')
        Truth = 79.779
        self.assertLessEqual(RE(Value, Truth), 3e-5)

    def test_06(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2press(65322, press_units='pa', alt_units='m')
        Truth = 9.4609
        self.assertLessEqual(RE(Value, Truth), 5e-5)

    def test_07(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2press(80956, press_units='pa', alt_units='m')
        Truth = 0.75009
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_08(self):

        # confirm out of range error

        self.assertRaises(ValueError, SA.alt2press, 90, alt_units='km')


class Test_alt2density_ratio(unittest.TestCase):

    def test_01(self):
        PR = SA.alt2density_ratio(0)
        self.assertEqual(PR, 1)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.alt2density_ratio(8000)
        Truth = 0.06011 / 0.076474
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2density_ratio(1999, alt_units='m')
        Truth = .82168
        self.assertLessEqual(RE(Value, Truth), 5e-5)


class Test_alt_temp2density_ratio(unittest.TestCase):

    def test_01(self):
        PR = SA.alt_temp2density_ratio(0, 59, temp_units='F')
        self.assertEqual(PR, 1)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.alt_temp2density_ratio(8000, -0.8496)
        Truth = 0.06011 / 0.076474
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt_temp2density_ratio(1999, 275.1565, alt_units='m', temp_units='K')
        Truth = .82168
        self.assertLessEqual(RE(Value, Truth), 5e-5)


class Test_alt2density(unittest.TestCase):

    def test_01(self):

        # Truth values from NASA RP 1046

        Value = SA.alt2density(8000)
        Truth = 0.06011
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        # test psf
        # Truth values from NASA RP 1046

        Value = SA.alt2density(49000)
        Truth = 0.012215
        self.assertLessEqual(RE(Value, Truth), 2e-5)

    def test_03(self):

        # test pa and m
        # Truth values from NASA RP 1046

        Value = SA.alt2density(25000, alt_units='m',
                               density_units='kg/m**3')
        Truth = 0.039466
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_04(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2density(39750, density_units='kg/m**3',
                               alt_units='m')

        Truth = 3.9957e-3
        self.assertLessEqual(RE(Value, Truth), 3e-5)

    def test_05(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2density(49610, density_units='kg/m**3',
                               alt_units='m')
        Truth = 1.0269e-3
        self.assertLessEqual(RE(Value, Truth), 5e-5)

    def test_06(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2density(65322, density_units='kg/m**3',
                               alt_units='m')
        Truth = 1.4296e-4
        self.assertLessEqual(RE(Value, Truth), 5e-5)

    def test_07(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.alt2density(80956, density_units='kg/m**3',
                               alt_units='m')
        Truth = 1.3418e-5
        self.assertLessEqual(RE(Value, Truth), 3e-5)

    def test_08(self):

        # confirm out of range error

        self.assertRaises(ValueError, SA.alt2density, 90, alt_units='km'
                          )


class Test_press2alt(unittest.TestCase):

    def test_01(self):

        # Truth values from NASA RP 1046

        Value = SA.press2alt(24.8959)
        Truth = 5000
        self.assertLessEqual(RE(Value, Truth), 2e-5)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.press2alt(254.139, press_units='psf')
        Truth = 49000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Truth values from NASA RP 1046

        Value = SA.press2alt(2511.01, alt_units='m', press_units='pa')
        Truth = 25000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_04(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.press2alt(287.14, press_units='pa', alt_units='m')
        Truth = 39750
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_05(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.press2alt(79.779, press_units='pa', alt_units='m')
        Truth = 49610
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_06(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.press2alt(9.4609, press_units='pa', alt_units='m')
        Truth = 65322
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_07(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.press2alt(0.75009, press_units='pa', alt_units='m')
        Truth = 80956
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_08(self):

        # check for out of range
        # http://www.sworld.com.au/steven/space/atmosphere/

        self.assertRaises(ValueError, SA.press2alt, 0.00011025)


class Test_press_ratio2alt(unittest.TestCase):

    def test_01(self):
        PR = SA.press_ratio2alt(1)
        self.assertEqual(PR, 0)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.press_ratio2alt(22.225 / 29.9213)
        Truth = 8000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Truth values from NASA RP 1046

        Value = SA.press_ratio2alt(5474.87 / 101325, alt_units='m')
        Truth = 20000
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_density2alt(unittest.TestCase):

    def test_01(self):

        # Truth values from NASA RP 1046

        Value = SA.density2alt(0.06011)
        Truth = 8000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.density2alt(0.012215)
        Truth = 49000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Truth values from NASA RP 1046

        Value = SA.density2alt(0.039466, alt_units='m',
                               density_units='kg/m**3')
        Truth = 25000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_04(self):

        # test units in other order
        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.density2alt(5.36663e-3, density_units='kg/m**3',
                               alt_units='m')
        Truth = 37774
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_05(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.density2alt(1.0269e-3, density_units='kg/m**3',
                               alt_units='m')
        Truth = 49610
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_06(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.density2alt(1.4296e-4, density_units='kg/m**3',
                               alt_units='m')
        Truth = 65322
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_07(self):

        # truth value calculated from program at:
        # http://www.sworld.com.au/steven/space/atmosphere/

        Value = SA.density2alt(1.3418e-5, density_units='kg/m**3',
                               alt_units='m')
        Truth = 80956
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_08(self):

        # check for out of range
        # http://www.sworld.com.au/steven/space/atmosphere/

        self.assertRaises(ValueError, SA.density2alt, 4.3436e-07)


class Test_density_ratio2alt(unittest.TestCase):

    def test_01(self):
        PR = SA.density_ratio2alt(1)
        self.assertEqual(PR, 0)

    def test_02(self):

        # Truth values from NASA RP 1046

        Value = SA.density_ratio2alt(0.78601648829428272)
        Truth = 8000
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Truth values from NASA RP 1046

        Value = SA.density_ratio2alt(.088035 / 1.225, alt_units='m')
        Truth = 20000
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_density_alt(unittest.TestCase):

    def test_01(self):
        PR = SA.density_alt(0, 15)
        self.assertAlmostEqual(PR, 0, places=0)

    def test_02(self):
        Value = SA.density_alt(6000, 75, 29.8, temp_units='F')
        Truth = 8492
        self.assertLessEqual(RE(Value, Truth), 2e-5)

    def test_03(self):
        Value = SA.density_alt(9080, 13, 1024)
        Truth = 10554
        self.assertLessEqual(RE(Value, Truth), 5e-5)

    def test_04(self):
        Value = SA.density_alt(5000, 0, 29.5)
        Truth = 4875
        self.assertAlmostEqual(Value, Truth, places=0)

    def test_05(self):
        Value = SA.density_alt(9080, 13, 1024)
        Truth = 10554
        self.assertAlmostEqual(Value, Truth, places=0)

    def test_06(self):

        # test dew point out of order

        Value = SA.density_alt(7000, 75, 29.75, temp_units='F', DP=45)
        Truth = 9921
        self.assertLessEqual(RE(Value, Truth), 2e-4)

    def test_07(self):
        Value = SA.density_alt(2000, 20, 999, 10, alt_units='m')
        Truth = 2829
        self.assertLessEqual(RE(Value, Truth), 2e-4)

    def test_08(self):

        # test alt_setting out of order

        Value = SA.density_alt(7500, 85, temp_units='F', RH=.8,
                               alt_setting=29.8)
        Truth = 11418
        self.assertLessEqual(RE(Value, Truth), 5e-4)

    def test_09(self):

        # check out of range on altimeter setting low

        self.assertRaises(ValueError, SA.density_alt, 0, 0, 24.99)

    def test_10(self):

        # check out of range on altimeter setting high

        self.assertRaises(ValueError, SA.density_alt, 9080, 13, 1186)

    def test_11(self):

        # check out of range with DP greater than temperature

        self.assertRaises(ValueError, SA.density_alt, 5000, 0, DP=1e-2)


class Test_temp2speed_of_sound(unittest.TestCase):

    def test_01(self):

        # speed of sound at 5,000 ft
        # Truth value from NASA RP 1046

        Value = SA.temp2speed_of_sound(SA.alt2temp(5000))
        Truth = 650.01
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_02(self):

        # speed of sound in mph at 8,000 ft
        # Truth value from NASA RP 1046

        Value = SA.temp2speed_of_sound(SA.alt2temp(8000),
                speed_units='mph')
        Truth = 739.98
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # speed of sound in km/h at 2,000 m, with temp in deg R
        # Truth value from NASA RP 1046

        Value = SA.temp2speed_of_sound(SA.alt2temp(2000, alt_units='m',
                temp_units='R'), speed_units='km/h', temp_units='R')
        Truth = 1197.1
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_04(self):

        # speed of sound at 10,000 m
        # Truth value from NASA RP 1046

        Value = SA.temp2speed_of_sound(SA.alt2temp(10000, alt_units='m'
                ))
        Truth = 582.11
        self.assertLessEqual(RE(Value, Truth), 1e-5)


class Test_pressure_alt(unittest.TestCase):

    def test_01(self):

        # Truth value from Pitot-Statics presentation at SFTE Annual Symposium, Sept 1998

        Value = SA.pressure_alt(0, 29.82)
        Truth = 93
        self.assertLessEqual(RE(Value, Truth), 1e-2)

    def test_02(self):
        Value = SA.pressure_alt(1000, 996)
        Truth = 1474.38
        self.assertLessEqual(RE(Value, Truth), 1e-5)

    def test_03(self):

        # Check out of range altimeter setting high

        self.assertRaises(ValueError, SA.pressure_alt, 1000, 35.01)

    def test_04(self):

        # Check out of range altimeter setting low, value in mb

        self.assertRaises(ValueError, SA.pressure_alt, 1000, 846.5)


class Test_sat_press(unittest.TestCase):

    def test_01(self):

        # dew point greater than temperature

        self.assertRaises(ValueError, SA.sat_press, 15, DP=15.01)

    def test_02(self):

        # dew point and relative humidity both specified

        self.assertRaises(ValueError, SA.sat_press, 15, DP=16, RH=0.5)

    def test_03(self):

        # relative humidity out of range high

        self.assertRaises(ValueError, SA.sat_press, 15, RH=1.01)

    def test_04(self):

        # relative humidity out of range low

        self.assertRaises(ValueError, SA.sat_press, 15, RH=-1e-2)

    def test_05(self):

        # boiling point, deg F, pa

        Value = SA.sat_press(DP=212, temp_units='F', press_units='pa')
        Truth = 101325
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_06(self):

        # boiling point, deg K, psi

        Value = SA.sat_press(DP=373.15, temp_units='K',
                             press_units='psi')
        Truth = 14.696
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_07(self):

        # RH specified, but not temperature

        self.assertRaises(ValueError, SA.sat_press, RH=0.5)

    def test_08(self):

        # from http://www.engineeringtoolbox.com/water-vapor-saturation-pressure-d_599.html

        Value = SA.sat_press(DP=32, temp_units='F', press_units='psi')
        Truth = 0.0885
        self.assertLessEqual(RE(Value, Truth), 1e-3)

    def test_09(self):

        # http://hyperphysics.phy-astr.gsu.edu/hbase/kinetic/watvap.html

        Value = SA.sat_press(DP=20, temp_units='C', press_units='mm HG')
        Truth = 17.54
        self.assertLessEqual(RE(Value, Truth), 1e-3)


class Test_density_alt2temp(unittest.TestCase):

    def test_01(self):

        # from http://wahiduddin.net/calc/calc_da.htm

        Value = SA.density_alt2temp(5000, 3700, temp_units='F')
        Truth = 66.02
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_02(self):

        # from http://wahiduddin.net/calc/calc_da.htm

        Value = SA.density_alt2temp(450, 1500, alt_units='m')
        Truth = -22
        self.assertLessEqual(RE(Value, Truth), 1e-3)

class Test_temp2dynamic_viscosity(unittest.TestCase):

    def test_01(self):

        # from US Standard Atmosphere, 1976

        Value = SA.temp2dynamic_viscosity(15, temp_units='C')
        Truth = 1.7894e-5
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_02(self):

        # from http://wahiduddin.net/calc/calc_da.htm

        Value = SA.temp2dynamic_viscosity(59, temp_units='F')
        Truth = 1.7894e-5
        self.assertLessEqual(RE(Value, Truth), 1e-4)

class Test_alt2dynamic_viscosity(unittest.TestCase):

    def test_01(self):

        # from US Standard Atmosphere, 1976

        Value = SA.alt2dynamic_viscosity(-5000, alt_units='m')
        Truth = 1.9421e-5
        self.assertLessEqual(RE(Value, Truth), 1e-4)

    def test_02(self):

        # from http://wahiduddin.net/calc/calc_da.htm

        Value = SA.alt2dynamic_viscosity(84500, alt_units='m')
        Truth = 1.2575e-5
        self.assertLessEqual(RE(Value, Truth), 1e-4)


if __name__ == '__main__':
    unittest.main(verbosity=2)

