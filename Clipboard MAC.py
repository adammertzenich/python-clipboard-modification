from AppKit import NSPasteboard, NSArray
# Requires https://pythonhosted.org/pyobjc/

pb = NSPasteboard.generalPasteboard()
pb.clearContents()
a = NSArray.arrayWithObject_("This is the string that will be copied to your clipboard.")
pb.writeObjects_(a)