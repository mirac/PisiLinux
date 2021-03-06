#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


KDIR = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("config.mk", "\$\(MAKE\) -C \$\(KLIB_BUILD\) kernelversion", "echo \"%s\"" % KDIR)
    pisitools.dosed("scripts/gen-compat-autoconf.sh", "make -C \$KLIB_BUILD kernelversion", "echo \"%s\"" % KDIR)

def build():
    autotools.make("MODPROBE=/bin/true KLIB=/lib/modules/%s" % KDIR)

def install():
    autotools.install("KLIB=/lib/modules/%s KMODPATH_ARG='INSTALL_MOD_PATH=%s' DEPMOD=/bin/true" % (KDIR, get.installDIR()))

    pisitools.dodoc("COPYRIGHT", "README")
