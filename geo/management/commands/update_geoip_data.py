"""
Copyright (c) 2010, Philipp Wassibauer
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of the author nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




Copyright (c) 2008 MaxMind, Inc.  All Rights Reserved.

All advertising materials and documentation mentioning features or use of
this database must display the following acknowledgment:
"This product includes GeoLite data created by MaxMind, available from
http://maxmind.com/"

Redistribution and use with or without modification, are permitted provided
that the following conditions are met:
1. Redistributions must retain the above copyright notice, this list of
conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution. 
2. All advertising materials and documentation mentioning features or use of
this database must display the following acknowledgement:
"This product includes GeoLite data created by MaxMind, available from
http://maxmind.com/"
3. "MaxMind" may not be used to endorse or promote products derived from this
database without specific prior written permission.

THIS DATABASE IS PROVIDED BY MAXMIND, INC ``AS IS'' AND ANY 
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL MAXMIND BE LIABLE FOR ANY 
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
DATABASE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copied from https://github.com/Gidsy/django-geoip-utils
"""

import os
import gzip
import urllib
import urlparse

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

download_folder = settings.GEOIP_PATH

class Command(BaseCommand):
    help = 'Updates GeoIP data in %s' % download_folder
    base_url = 'http://www.maxmind.com/download/geoip/database/'
    files = ['GeoLiteCity.dat.gz', 'GeoLiteCountry/GeoIP.dat.gz']

    def handle(self, *args, **options):
        for path in self.files:
            root, filepath = os.path.split(path)
            dowloadpath = os.path.join(download_folder, filepath)
            downloadurl = urlparse.urljoin(self.base_url, path)
            self.stdout.write('Downloading %s to %s\n' % (downloadurl, dowloadpath))
            urllib.urlretrieve(downloadurl, dowloadpath)
            outfilepath, ext = os.path.splitext(dowloadpath)
            if ext != '.gz':
                raise CommandError('Something went wrong while '
                                   'decompressing %s' % dowloadpath)
            self.stdout.write('Extracting %s to %s\n' % (dowloadpath, outfilepath))
            infile = gzip.open(dowloadpath, 'rb')
            outfile = open(outfilepath, 'wb')
            try:
                outfile.writelines(infile)
            finally:
                infile.close()
                outfile.close()
            self.stdout.write('Deleting %s\n' % dowloadpath)
            os.remove(dowloadpath)
            self.stdout.write('Done with %s' % path)
