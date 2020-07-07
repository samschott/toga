##########################################################################
# System/Library/Frameworks/Foundation.framework
##########################################################################
from ctypes import c_bool, cdll, util

from rubicon.objc import NSPoint, NSRect, ObjCClass

######################################################################
foundation = cdll.LoadLibrary(util.find_library('Foundation'))
######################################################################

foundation.NSMouseInRect.restype = c_bool
foundation.NSMouseInRect.argtypes = [NSPoint, NSRect, c_bool]

######################################################################
# NSBundle.h
NSBundle = ObjCClass('NSBundle')
NSBundle.declare_class_property('mainBundle')
NSBundle.declare_property('bundlePath')

######################################################################
# NSFileWrapper.h
NSFileWrapper = ObjCClass('NSFileWrapper')

######################################################################
# NSNotification.h
NSNotificationCenter = ObjCClass('NSNotificationCenter')

######################################################################
NSNotification = ObjCClass('NSNotification')
NSNotification.declare_property('object')

######################################################################
# NSURL.h
NSURL = ObjCClass('NSURL')

######################################################################
# NSURLRequest.h
NSURLRequest = ObjCClass('NSURLRequest')

######################################################################
# NSValue.h
NSNumber = ObjCClass('NSNumber')

######################################################################
# NSMutableAttributedString.h
NSMutableAttributedString = ObjCClass('NSMutableAttributedString')


######################################################################
# NSString.h

NSASCIIStringEncoding = 1
NSNEXTSTEPStringEncoding = 2
NSJapaneseEUCStringEncoding = 3
NSUTF8StringEncoding = 4
NSISOLatin1StringEncoding = 5
NSSymbolStringEncoding = 6
NSNonLossyASCIIStringEncoding = 7
NSISOLatin2StringEncoding = 9
NSUTF16StringEncoding = 10
NSUnicodeStringEncoding = 10
NSWindowsCP1251StringEncoding = 11
NSWindowsCP1252StringEncoding = 12
NSWindowsCP1253StringEncoding = 13
NSWindowsCP1254StringEncoding = 14
NSWindowsCP1250StringEncoding = 15
NSISO2022JPStringEncoding = 21
NSMacOSRomanStringEncoding = 30
