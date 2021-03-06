#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", "%s -fPIC -fno-strict-aliasing" % get.CFLAGS())
shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--with-openldap=yes \
                         --enable-smime=yes \
                         --enable-gnome-keyring=yes \
                         --with-krb5=/usr \
                         --disable-uoa \
                         --with-libdb=/usr \
                         --enable-calendar=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "MAINTAINERS", "NEWS", "README", "TODO")
