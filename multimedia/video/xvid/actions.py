#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xvidcore/build/generic"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Fixup libs and remove static one
    pisitools.dosym("libxvidcore.so.4",  "/usr/lib/libxvidcore.so")
    pisitools.dosym("libxvidcore.so.4.3",  "/usr/lib/libxvidcore.so.4")
    pisitools.remove("/usr/lib/libxvidcore.a")

    shelltools.cd("../..")
    pisitools.insinto("/usr/share/doc/xvid/examples", "examples/*")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "README", "LICENSE", "TODO")
