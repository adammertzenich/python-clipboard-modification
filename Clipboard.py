from AppKit import NSPasteboard, NSArray

pb = NSPasteboard.generalPasteboard()
pb.clearContents()
a = NSArray.arrayWithObject_("7")
pb.writeObjects_(a)