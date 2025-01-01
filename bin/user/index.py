"""
Extension for the Index skin
Creates a table for each directory in HTML_ROOT which contains index.html, or sguweewx.html
Sally Woolrich, Januaty 2025    shunracats<at>gmail.com
"""

import os
import glob
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
VERSION = "2.0"
loginf("index.py Version %s" % VERSION)

class getData(SearchList):
    def __init__(self, generator):
        SearchList.__init__(self, generator)

    def get_extension_list(self, timespan, db_lookup):
        """
        Return a string that contains a table with links
        to each index.html or sguweewx.html in HTML_ROOT
        """
        index_debug = self.generator.skin_dict["Extras"].get( "index_debug", 0 )
        if (index_debug):
            logdbg( "index_debug = %s" % index_debug )

        try:
            html_root = self.skin_dict['HTML_ROOT']
        except:
            html_root = "/var/www/html/weewx"

        if (index_debug):
            logdbg( "HTML_ROOT = %s" % html_root )

        os.chdir( html_root )

        skin_list = ""
        
# Iterate over files in directory
        for dirname in os.listdir(html_root):
            logdbg( "dirname = %s" % dirname )
            if (dirname == "dokuwiki" ):
                skin_list = os.linesep + skin_list + "<h4><a href='dokuwiki/sguweewx.html'>SGC Weather Station</a></h4>"
            else:
                link = os.path.join(dirname, "index.html" )
                if os.path.isfile( link ):
                    skin_list = os.linesep + skin_list + "<h4><a href='" + dirname + "'>" + dirname.capitalize() + "</a></h4>"

        # Finally, return our extension
        search_list_extension = { 'skin_list' : skin_list }
        return [search_list_extension]
