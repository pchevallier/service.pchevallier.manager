#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2016 Zomboided
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    Service module for VPN Manager for OpenVPN addon

import xbmc
import xbmcgui
import xbmcaddon
import xbmcvfs
import os
import time
import datetime
import urllib2
import re
import string
# Window property constants
last_addon = 'Last_Addon'


# Lists of primary VPNs and their friendly names (so we don't have to keep pattern matching it)

# Set the addon name for use in the dialogs
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')

accepting_changes = False

abort = False

stop_ids = []



if __name__ == '__main__':


    # Initialise some variables we'll be using repeatedly
    monitor = xbmc.Monitor()
    player = xbmc.Player()
    addon = xbmcaddon.Addon()
