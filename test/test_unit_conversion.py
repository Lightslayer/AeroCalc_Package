#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test cases for unit_conversion module.
Run this script directly to do all the tests.
"""
# To Do   1. Done
#
#         2. Done

# Done    1. 29 Jun 2009 - Ran 2to3 tool and fixed errors
#
#         2. Confirmed truth data for press_conv test 7

import unittest
import sys

import aerocalc.unit_conversion as U


def RE(value, truth):
    """ Return the absolute value of the relative error.
    """

    if truth == 0:
        return abs(value - truth)
    else:
        return abs((value - truth) / truth)


class Test_area_conv(unittest.TestCase):

    """Given that the conversion function works by converting units to or from
     a base unit, a complete check requires one calculation that converts too 
     and from each unit."""

    def test_01(self):
        Value = U.area_conv(10, from_units='ft**2', to_units='in**2')
        Truth = 1440
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_02(self):
        Value = U.area_conv(144, from_units='in**2', to_units='m**2')
        Truth = 0.3048 ** 2
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_03(self):
        Value = U.area_conv(1000, from_units='m**2', to_units='km**2')
        Truth = 0.001
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_04(self):
        Value = U.area_conv(1, from_units='km**2', to_units='sm**2')
        Truth = ((1000 / 0.3048) / 5280) ** 2
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_05(self):
        Value = U.area_conv(1, from_units='sm**2', to_units='nm**2')
        Truth = (5280 / (1852. / 0.3048)) ** 2
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_06(self):
        Value = U.area_conv(1, from_units='nm**2', to_units='ft**2')
        Truth = (1852. / 0.3048) ** 2
        self.failUnless(RE(Value, Truth) <= 1e-5)


class Test_density_conv(unittest.TestCase):

    def test_01(self):
        Value = U.density_conv(1, from_units='kg/m**3',
                               to_units='slug/ft**3')
        Truth = (3.6127292e-5 * 12 ** 3) / 32.174
        print(Value, Truth)
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_02(self):
        Value = U.density_conv(1, from_units='slug/ft**3',
                               to_units='lb/ft**3')
        Truth = 32.174
        print(Value, Truth)
        self.failUnless(RE(Value, Truth) <= 1e-5)


class Test_force_conv(unittest.TestCase):

    def test_01(self):
        Value = U.force_conv(100, from_units='lb', to_units='N')
        Truth = 444.82216
        self.failUnless(RE(Value, Truth) <= 1e-7)

    def test_02(self):
        Value = U.force_conv(444.82216, from_units='N', to_units='lb')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-7)


class Test_length_conv(unittest.TestCase):

    def test_01(self):
        Value = U.length_conv(120, from_units='in', to_units='ft')
        Truth = 10
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_02(self):
        Value = U.length_conv(10, from_units='ft', to_units='in')
        Truth = 120
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_03(self):
        Value = U.length_conv(10000, from_units='m', to_units='km')
        Truth = 10
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_04(self):
        Value = U.length_conv(10, from_units='km', to_units='m')
        Truth = 10000
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_05(self):
        Value = U.length_conv(1, from_units='sm', to_units='nm')
        Truth = 0.86897624
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_06(self):
        Value = U.length_conv(0.86897624, from_units='nm', to_units='sm')
        Truth = 1
        self.failUnless(RE(Value, Truth) <= 1e-5)


class Test_power_conv(unittest.TestCase):

    def test_01(self):
        Value = U.power_conv(1, from_units='hp', to_units='ft-lb/mn')
        Truth = 33000
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_02(self):
        Value = U.power_conv(33000, from_units='ft-lb/mn', to_units='hp'
                             )
        Truth = 1
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_03(self):
        Value = U.power_conv(550, from_units='ft-lb/s', to_units='kW')
        Truth = 0.74569987
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_04(self):
        Value = U.power_conv(0.74569987, from_units='kW',
                             to_units='ft-lb/s')
        Truth = 550
        self.failUnless(RE(Value, Truth) <= 1e-5)


    # def test_05(self):
    #     Value = U.power_conv(0.017584264, from_units='kW', to_units='BTU/hr')
    #     Truth = 60
    #     print Value, Truth
    #     self.failUnless(RE(Value, Truth) <= 1e-5)
    #
    # def test_06(self):
    #     Value = U.power_conv(60, from_units='BTU/hr', to_units='W')
    #     Truth = 17.584264
    #     self.failUnless(RE(Value, Truth) <= 1e-5)
    #
    # def test_07(self):
    #     Value = U.power_conv(0.017584264, from_units='kW', to_units='BTU/mn')
    #     Truth = 1
    #     self.failUnless(RE(Value, Truth) <= 1e-5)
    #
    # def test_08(self):
    #     Value = U.power_conv(1, from_units='BTU/mn', to_units='W')
    #     Truth = 17.584264
    #     self.failUnless(RE(Value, Truth) <= 1e-5)


class Test_press_conv(unittest.TestCase):

    def test_01(self):
        Value = U.press_conv(1, from_units='in HG', to_units='mm HG')
        Truth = 25.4
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_02(self):
        Value = U.press_conv(1, from_units='mm HG', to_units='psi')
        Truth = 0.01934543333
        self.failUnless(RE(Value, Truth) <= 5e-4)

    def test_03(self):
        Value = U.press_conv(1, from_units='psi', to_units='lb/ft**2')
        Truth = 144
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_04(self):
        Value = U.press_conv(1, from_units='lb/ft**2', to_units='mb')
        Truth = 0.4788
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_05(self):
        Value = U.press_conv(1, from_units='cm H2O', to_units='in H2O')
        Truth = 1/2.54
        self.failUnless(RE(Value, Truth) <= 4e-5)

    def test_06(self):
        Value = U.press_conv(1, from_units='in H2O', to_units='mm HG')
        Truth = 1.865
        print('Truth=%.8f, Value=%.8f' % (Truth, Value))
        self.failUnless(RE(Value, Truth) <= 1e-5)

    def test_07(self):
        Value = U.press_conv(1, from_units='psi', to_units='cm H2O')
        Truth = 1/.014198 # truth value from NASA RP 1046 Table A27. 
                          # Note that there is an inconsistency between 
                          # the stated conversions from psi to cm H2O 
                          # (70.376), and the conversion from cm H2O to 
                          # psi (.014198)
        print('Truth=%.8f, Value=%.8f' % (Truth, Value))
        self.failUnless(RE(Value, Truth) <= 5e-5)


class Test_speed_conv(unittest.TestCase):

    def test_01(self):
        Value = U.speed_conv(1, from_units='kt', to_units='mph')
        Truth = (1852. / 0.3048) / 5280
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_02(self):
        Value = U.speed_conv(1, from_units='mph', to_units='km/h')
        Truth = (5280 * 0.3048) / 1000
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_03(self):
        Value = U.speed_conv(1, from_units='km/h', to_units='m/s')
        Truth = 1000 / 3600.
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_04(self):
        Value = U.speed_conv(1, from_units='m/s', to_units='ft/s')
        Truth = 1 / 0.3048
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_05(self):
        Value = U.speed_conv(1, from_units='ft/s', to_units='kt')
        Truth = 3600. / (1852. / 0.3048)
        self.failUnless(RE(Value, Truth) <= 1e-8)


class Test_temp_conv(unittest.TestCase):

    def test_01(self):
        Value = U.temp_conv(0, from_units='C', to_units='F')
        Truth = 32
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_02(self):
        Value = U.temp_conv(100, from_units='C', to_units='F')
        Truth = 212
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_03(self):
        Value = U.temp_conv(32, from_units='F', to_units='C')
        Truth = 0
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_04(self):
        Value = U.temp_conv(212, from_units='F', to_units='C')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_05(self):
        Value = U.temp_conv(473.15, from_units='K', to_units='C')
        Truth = 200.
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_06(self):
        Value = U.temp_conv(-100, from_units='C', to_units='K')
        Truth = 173.15
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_07(self):
        Value = U.temp_conv(100, from_units='K', to_units='R')
        Truth = 180
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_08(self):
        Value = U.temp_conv(180, from_units='R', to_units='K')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_09(self):
        Value = U.temp_conv(32, from_units='F', to_units='R')
        Truth = 491.67
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_10(self):
        Value = U.temp_conv(671.67, from_units='R', to_units='F')
        Truth = 212
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_11(self):
        Value = U.temp_conv(671.67, from_units='R', to_units='C')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_12(self):
        Value = U.temp_conv(-100, from_units='C', to_units='R')
        Truth = 311.67
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_13(self):
        Value = U.temp_conv(373.15, from_units='K', to_units='F')
        Truth = 212
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_14(self):
        Value = U.temp_conv(-148, from_units='F', to_units='K')
        Truth = 173.15
        self.failUnless(RE(Value, Truth) <= 1e-8)


class Test_vol_conv(unittest.TestCase):

    def test_01(self):
        Value = U.vol_conv(1, from_units='ft**3', to_units='in**3')
        Truth = 12 ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_02(self):
        Value = U.vol_conv(1, to_units='m**3', from_units='in**3')
        Truth = (0.3048 / 12) ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_03(self):
        Value = U.vol_conv(1, from_units='m**3', to_units='km**3')
        Truth = 0.001 ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_04(self):
        Value = U.vol_conv(1, to_units='sm**3', from_units='km**3')
        Truth = ((1000 / 0.3048) / 5280) ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_05(self):
        Value = U.vol_conv(1, from_units='sm**3', to_units='nm**3')
        Truth = (5280 / (1852. / 0.3048)) ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_06(self):
        Value = U.vol_conv(1, to_units='USG', from_units='nm**3')
        Truth = 7.4805195 * (1852. / 0.3048) ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_07(self):
        Value = U.vol_conv(1, from_units='USG', to_units='ImpGal')
        Truth = 0.83267418
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_08(self):
        Value = U.vol_conv(1, to_units='l', from_units='ImpGal')
        Truth = 4.54609
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_09(self):
        Value = U.vol_conv(1, from_units='l', to_units='ft**3')
        Truth = (0.1 / 0.3048) ** 3
        self.failUnless(RE(Value, Truth) <= 1e-8)


class Test_wt_conv(unittest.TestCase):

    def test_01(self):
        Value = U.wt_conv(100, from_units='lb', to_units='kg')
        Truth = 45.359237
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_02(self):
        Value = U.wt_conv(45.359237, from_units='kg', to_units='lb')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_03(self):
        Value = U.wt_conv(100, from_units='lb', to_units='lb')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)


class Test_avgas_conv(unittest.TestCase):

    def test_01(self):

        # 10 USG of nominal fuel at nominal temperature to lbs
        # truth value from Canada Flight Supplement

        Value = U.avgas_conv(10, from_units='USG', to_units='lb')
        Truth = 60.1
        self.failUnless(RE(Value, Truth) <= 5e-4)

    def test_02(self):

        # 200 lb of nominal fuel at -40 deg C to USG
        # truth value from Canada Flight Supplement

        Value = U.avgas_conv(200., from_units='lb', to_units='USG',
                             temp=-40)
        Truth = 200. / 6.41
        self.failUnless(RE(Value, Truth) <= 5e-4)

    def test_03(self):

        # 200 lb of 100LL grade fuel at 15 deg C to Imperial Gallons
        # truth value from Air BP Handbook of Products - 715 kg/m**3

        Value = U.avgas_conv(200., from_units='lb', to_units='ImpGal',
                             grade='100LL')
        Truth = (((200. / 2.204622622) / 715) * 1000) / 4.54609
        self.failUnless(RE(Value, Truth) <= 5e-4)

    def test_04(self):

        # 200 kg of 100 grade fuel at 30 deg C to l
        # truth value from Air BP Handbook of Products - 695 kg/m**3 at 15 deg C

        Value = U.avgas_conv(200., from_units='kg', to_units='l',
                             grade='100', temp=30)
        Truth = (200. / 695) * 1000

        # correct for temperature, using ratio given in Canada Flight Supplement

        Truth *= 6.01 / 5.9
        self.failUnless(RE(Value, Truth) <= 5e-4)

    def test_05(self):

        # 200 l of 80 grade fuel at -40 deg C to kg
        # truth value from Air BP Handbook of Products - 690 kg/m**3 at 15 deg C

        Value = U.avgas_conv(200., from_units='l', to_units='kg',
                             grade='80', temp=-40)
        Truth = (200. / 1000) * 690

        # correct for temperature, using ratio given in Canada Flight Supplement

        Truth *= 6.41 / 6.01
        self.failUnless(RE(Value, Truth) <= 5e-4)

class Test_mass_conv(unittest.TestCase):

    def test_01(self):
        Value = U.mass_conv(100, from_units='lb', to_units='kg')
        Truth = 45.359237
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_02(self):
        Value = U.mass_conv(45.359237, from_units='kg', to_units='lb')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)

    def test_03(self):
        Value = U.mass_conv(100, from_units='lb', to_units='lb')
        Truth = 100
        self.failUnless(RE(Value, Truth) <= 1e-8)


if __name__ == '__main__':
    unittest.main(verbosity=5)
