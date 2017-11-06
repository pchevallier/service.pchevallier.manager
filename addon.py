#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright (C) 2017 pchevallier
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
#

import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import os

def ifDebug():
    return True;

def debugTrace(data):
    if ifDebug():
        log = "Pchevallier Mgr Debug: " + data
        xbmc.log(msg=log, level=xbmc.LOGNONE)
    else:
        log = "Pchevallier Mgr : " + data
        xbmc.log(msg=log, level=xbmc.LOGDEBUG)


debugTrace("-- Entered addon.py " + sys.argv[0] + " " + sys.argv[1] + " " + sys.argv[2] + " --")

# Set the addon name for use in the dialogs
addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo("name")

# Get the arguments passed in
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = sys.argv[2].split("?", )
action = ""
params = ""
# If an argument has been passed in, the first character will be a ?, so the first list element is empty
inc = 0
for token in args:
    if inc == 1 : action = token
    if inc > 1 : params = params + token
    inc = inc + 1

# Don't seem to need to do this on *nix platforms as the filename will be different
#if getPlatform() == platforms.WINDOWS: params = params.replace("/", "\\")

debugTrace("Parsed arguments to action=" + action + " params=" + params)


def topLevel():
    # Build the top level menu with URL callbacks to this plugin
    debugTrace("Displaying the top level menu")
    url = base_url + "?settings"
    li = xbmcgui.ListItem("Add-on Settings", iconImage=getIconPath()+"settings.png")
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = base_url + "?display"
    li = xbmcgui.ListItem("Display status", iconImage=getIconPath()+"display.png")
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    url = base_url + "?list"
    li = xbmcgui.ListItem("list option", iconImage=getIconPath()+"locked.png")
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)
    return

def getIconPath():
    return getAddonPath(True, "/resources/")

def listSystem(addon):
    lines = getSystemData(addon, True, True, True, True)
    for line in lines:
        url = base_url + "?back"
        li = xbmcgui.ListItem(line, iconImage=getIconPath()+"enhanced.png")
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
    xbmcplugin.endOfDirectory(addon_handle)
    return


def back():
    xbmc.executebuiltin("Action(ParentDir)")
    return


def displayStatus():
    debugTrace("displayStatus")
    return

def getAddonPath(this_addon, path):
    # Return the URL of the addon directory, plus any addition path/file name.
    if this_addon:
        return xbmc.translatePath("special://home/addons/service.pchevallier.manager/" + path)
    else:
        return xbmc.translatePath("special://home/addons/" + path)


if action == "display":
    # Display the network status
    displayStatus()
elif action == "system":
    listSystem(addon)
elif action == "back" :
    back()
    #listSystem()
else: topLevel()

debugTrace("-- Exit addon.py --")
