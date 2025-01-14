"""
Extension for the Index skin
Creates a table for each directory in HTML_ROOT which contains index.html, or sguweewx.html
Sally Woolrich, Januaty 2025    shunracats<at>gmail.com
"""

import os
import weewx

# Logging
import weeutil.logger
import logging

log = logging.getLogger(__name__)

def logdbg(msg):
    log.debug(msg)

def loginf(msg):
    log.info(msg)

def logerr(msg):
    log.error(msg)

from weewx.cheetahgenerator import SearchList

# Print version in syslog for easier troubleshooting
VERSION = "2.4"

loginf("index.py Version %s" % VERSION)

class getData(SearchList):
    def __init__(self, generator):
        SearchList.__init__(self, generator)

    def get_extension_list(self, timespan, db_lookup):
        """
        Return a string that contains a table with links
        to each index.html or sguweewx.html in HTML_ROOT
        """
        index_debug = int(self.generator.skin_dict["Extras"].get( "index_debug", 0 ))
        if (index_debug):
            logerr( "index_debug = %s" % index_debug )

        skin_version = self.generator.skin_dict['SKIN_VERSION']
        if( index_debug) :
            logerr( "SKIN_VERSION %s" % skin_version )

# Find the right HTML ROOT
        if "HTML_ROOT" in self.generator.skin_dict:
            html_root = os.path.join(
                self.generator.config_dict["WEEWX_ROOT"],
                self.generator.skin_dict["HTML_ROOT"],
            )
        else:
            html_root = os.path.join(
                self.generator.config_dict["WEEWX_ROOT"],
                self.generator.config_dict["StdReport"]["HTML_ROOT"],
            )

        if (index_debug):
            logerr( "HTML_ROOT = %s" % html_root )

        os.chdir( html_root )

        skin_list = ""

# Iterate over files in directory
        items =  os.listdir(html_root)
        items.sort(key=str.lower)
        for dirname in items:
            if (index_debug):
                logerr( "dirname = %s" % dirname )
            if (dirname == "dokuwiki" ):
                skin_list = skin_list + os.linesep + "<h4><a href='dokuwiki/sguweewx.html'>SGC Weather Station</a></h4>"
            else:
                displayname = dirname
                if (dirname != "NewNeoWx" ):
                    displayname = displayname.capitalize()
                link = os.path.join(dirname, "index.html" )
                if os.path.isfile( link ):
                    skin_list = skin_list + os.linesep + "<h4><a href='" + dirname + "'>" + displayname + "</a></h4>"


        if (index_debug):
            logerr( "skin_list = %s" % skin_list )
        # Finally, return our extension
        search_list_extension = { 'skin_list' : skin_list }
        return [search_list_extension]
