#!/usr/bin/env python
#
# This work is licensed under the Creative Attribution-NonCommercial-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.

from __future__ import print_function
from bitarray import bitarray

# Does anybody read this stuff? There's a PEP somewhere that says I should do this.
__author__     = 'Cortney T. Buffington, N0MJS'
__copyright__  = 'Copyright (c) 2016 Cortney T. Buffington, N0MJS and the K0USY Group'
__credits__    = 'Jonathan Naylor, G4KLX who many parts of this were thankfully borrowed from'
__license__    = 'Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported'
__maintainer__ = 'Cort Buffington, N0MJS'
__email__      = 'n0mjs@me.com'


ENCODE_1676 = (
	0x0000, 0x0273, 0x04E5, 0x0696, 0x09C9, 0x0BBA, 0x0D2C, 0x0F5F, 0x11E2, 0x1391, 0x1507, 0x1774,
	0x182B, 0x1A58, 0x1CCE, 0x1EBD, 0x21B7, 0x23C4, 0x2552, 0x2721, 0x287E, 0x2A0D, 0x2C9B, 0x2EE8,
	0x3055, 0x3226, 0x34B0, 0x36C3, 0x399C, 0x3BEF, 0x3D79, 0x3F0A, 0x411E, 0x436D, 0x45FB, 0x4788,
	0x48D7, 0x4AA4, 0x4C32, 0x4E41, 0x50FC, 0x528F, 0x5419, 0x566A, 0x5935, 0x5B46, 0x5DD0, 0x5FA3,
	0x60A9, 0x62DA, 0x644C, 0x663F, 0x6960, 0x6B13, 0x6D85, 0x6FF6, 0x714B, 0x7338, 0x75AE, 0x77DD,
	0x7882, 0x7AF1, 0x7C67, 0x7E14, 0x804F, 0x823C, 0x84AA, 0x86D9, 0x8986, 0x8BF5, 0x8D63, 0x8F10,
	0x91AD, 0x93DE, 0x9548, 0x973B, 0x9864, 0x9A17, 0x9C81, 0x9EF2, 0xA1F8, 0xA38B, 0xA51D, 0xA76E,
	0xA831, 0xAA42, 0xACD4, 0xAEA7, 0xB01A, 0xB269, 0xB4FF, 0xB68C, 0xB9D3, 0xBBA0, 0xBD36, 0xBF45,
	0xC151, 0xC322, 0xC5B4, 0xC7C7, 0xC898, 0xCAEB, 0xCC7D, 0xCE0E, 0xD0B3, 0xD2C0, 0xD456, 0xD625,
	0xD97A, 0xDB09, 0xDD9F, 0xDFEC, 0xE0E6, 0xE295, 0xE403, 0xE670, 0xE92F, 0xEB5C, 0xEDCA, 0xEFB9,
	0xF104, 0xF377, 0xF5E1, 0xF792, 0xF8CD, 0xFABE, 0xFC28, 0xFE5B)

DECODE_1576 = (
	0x0000, 0x0001, 0x0002, 0x0003, 0x0004, 0x0005, 0x0006, 0x4020, 0x0008, 0x0009, 0x000A, 0x000B, 
	0x000C, 0x000D, 0x2081, 0x2080, 0x0010, 0x0011, 0x0012, 0x0013, 0x0014, 0x0C00, 0x0016, 0x0C02, 
	0x0018, 0x0120, 0x001A, 0x0122, 0x4102, 0x0124, 0x4100, 0x4101, 0x0020, 0x0021, 0x0022, 0x4004, 
	0x0024, 0x4002, 0x4001, 0x4000, 0x0028, 0x0110, 0x1800, 0x1801, 0x002C, 0x400A, 0x4009, 0x4008, 
	0x0030, 0x0108, 0x0240, 0x0241, 0x0034, 0x4012, 0x4011, 0x4010, 0x0101, 0x0100, 0x0103, 0x0102, 
	0x0105, 0x0104, 0x1401, 0x1400, 0x0040, 0x0041, 0x0042, 0x0043, 0x0044, 0x0045, 0x0046, 0x4060, 
	0x0048, 0x0049, 0x0301, 0x0300, 0x004C, 0x1600, 0x0305, 0x0304, 0x0050, 0x0051, 0x0220, 0x0221, 
	0x3000, 0x4200, 0x3002, 0x4202, 0x0058, 0x1082, 0x1081, 0x1080, 0x3008, 0x4208, 0x2820, 0x1084, 
	0x0060, 0x0061, 0x0210, 0x0211, 0x0480, 0x0481, 0x4041, 0x4040, 0x0068, 0x2402, 0x2401, 0x2400, 
	0x0488, 0x3100, 0x2810, 0x2404, 0x0202, 0x0880, 0x0200, 0x0201, 0x0206, 0x0884, 0x0204, 0x0205, 
	0x0141, 0x0140, 0x0208, 0x0209, 0x2802, 0x0144, 0x2800, 0x2801, 0x0080, 0x0081, 0x0082, 0x0A00, 
	0x0084, 0x0085, 0x2009, 0x2008, 0x0088, 0x0089, 0x2005, 0x2004, 0x2003, 0x2002, 0x2001, 0x2000, 
	0x0090, 0x0091, 0x0092, 0x1048, 0x0602, 0x0C80, 0x0600, 0x0601, 0x0098, 0x1042, 0x1041, 0x1040, 
	0x2013, 0x2012, 0x2011, 0x2010, 0x00A0, 0x00A1, 0x00A2, 0x4084, 0x0440, 0x0441, 0x4081, 0x4080, 
	0x6000, 0x1200, 0x6002, 0x1202, 0x6004, 0x2022, 0x2021, 0x2020, 0x0841, 0x0840, 0x2104, 0x0842, 
	0x2102, 0x0844, 0x2100, 0x2101, 0x0181, 0x0180, 0x0B00, 0x0182, 0x5040, 0x0184, 0x2108, 0x2030, 
	0x00C0, 0x00C1, 0x4401, 0x4400, 0x0420, 0x0421, 0x0422, 0x4404, 0x0900, 0x0901, 0x1011, 0x1010, 
	0x0904, 0x2042, 0x2041, 0x2040, 0x0821, 0x0820, 0x1009, 0x1008, 0x4802, 0x0824, 0x4800, 0x4801, 
	0x1003, 0x1002, 0x1001, 0x1000, 0x0501, 0x0500, 0x1005, 0x1004, 0x0404, 0x0810, 0x1100, 0x1101, 
	0x0400, 0x0401, 0x0402, 0x0403, 0x040C, 0x0818, 0x1108, 0x1030, 0x0408, 0x0409, 0x040A, 0x2060, 
	0x0801, 0x0800, 0x0280, 0x0802, 0x0410, 0x0804, 0x0412, 0x0806, 0x0809, 0x0808, 0x1021, 0x1020, 
	0x5000, 0x2200, 0x5002, 0x2202)

X14     = 0x00004000   # vector representation of X^14
X8      = 0x00000100   # vector representation of X^8
MASK7   = 0xffffff00   # auxiliary vector for testing
GENPOL  = 0x00000139   # generator polinomial, g(x)

def get_synd_1576(_pattern):
	aux = X14;
	if _pattern >= X8:
		while _pattern & MASK7:
			while not (aux & _pattern):
				aux = aux >> 1
			_pattern ^= (aux / X8) * GENPOL
	return _pattern

def encode(_data):
    value = (_data[0] >> 1) & 0x7F
    cksum = ENCODE_1676[value]
    _data[0] = cksum >> 8
    _data[1] = cksum & 0xFF
    return _data

def decode(_data):
	code = (_data[0] << 7) + (_data[1] >> 1)
	syndrome = get_synd_1576(code)
	error_pattern = DECODE_1576[syndrome]
	code ^= error_pattern
	return code >> 7


#------------------------------------------------------------------------------
# Used to execute the module directly to run built-in tests
#------------------------------------------------------------------------------

if __name__ == '__main__':
    
    from binascii import b2a_hex as h
    from time import time