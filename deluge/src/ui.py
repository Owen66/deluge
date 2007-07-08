#
# ui.py
#
# Copyright (C) Andrew Resch  2007 <andrewresch@gmail.com> 
# 
# Deluge is free software.
# 
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 2 of the License, or (at your option)
# any later version.
# 
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with deluge.  If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#  In addition, as a special exception, the copyright holders give
#  permission to link the code of portions of this program with the OpenSSL
#  library.
#  You must obey the GNU General Public License in all respects for all of
#  the code used other than OpenSSL. If you modify file(s) with this
#  exception, you may extend this exception to your version of the file(s),
#  but you are not obligated to do so. If you do not wish to do so, delete
#  this exception statement from your version. If you delete this exception
#  statement from all source files in the program, then also delete it here.

import logging

try:
	import dbus, dbus.service
	dbus_version = getattr(dbus, "version", (0,0,0))
	if dbus_version >= (0,41,0) and dbus_version < (0,80,0):
		import dbus.glib
	elif dbus_version >= (0,80,0):
		from dbus.mainloop.glib import DBusGMainLoop
		DBusGMainLoop(set_as_default=True)
	else:
		pass
except: dbus_imported = False
else: dbus_imported = True

# Get the logger
log = logging.getLogger("deluge")

class Ui:
  def __init__(self):
    log.debug("Ui init..")
    log.debug("Getting core proxy object from DBUS..")
    # Get the proxy object from DBUS
    bus = dbus.SessionBus()
    proxy = bus.get_object("org.deluge_torrent.Deluge", 
                           "/org/deluge_torrent/Core")
    self.core = dbus.Interface(proxy, "org.deluge_torrent.Deluge")
    log.debug("Got core proxy object..")      
    # Test the interface.. this calls test() in Core
    self.core.test()
