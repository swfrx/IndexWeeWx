# installer for the 'Index' skin
# January 2025, Sally Woolrich

from weecfg.extension import ExtensionInstaller

#-------- extension info -----------

VERSION      = "2.4"
NAME         = 'Index'
DESCRIPTION  = 'Generates a basic index.html for my live & test systems based on directoris in HTML_ROOT containing index.html. At present DokuWiki is an exception.'
AUTHOR       = "Sally Woolrich"
AUTHOR_EMAIL = "shunracats <at> gmail.com"

#-------- main loader -----------

def loader():
    return IndexInstaller()

class IndexInstaller(ExtensionInstaller):
    def __init__(self):
        super(IndexInstaller, self).__init__(
            version=VERSION,
            name=NAME,
            description=DESCRIPTION,
            author=AUTHOR,
            author_email=AUTHOR_EMAIL,
            config={
                'StdReport': {
                    'Index': {
                        'skin': 'Index',
                        'enable' : 'True',
                        'lang': 'en',
                    },
                },
            },
            files=[('bin/user', ['bin/user/index.py']),
                ('skins/Index',
                 ['skins/Index/lang/en.conf',
                  'skins/Index/index.html.tmpl',
                  'skins/Index/skin.conf',
                  ]),
            ]
        )
