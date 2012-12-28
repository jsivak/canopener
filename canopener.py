# -*- coding: utf-8 -*-

import bz2
import gzip
import urllib2
import urlparse


class WithMixin(object):
    """Gives a file-like object `with` powers."""

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

class bz2file(bz2.BZ2File, WithMixin):
    """Wrapper around bz2.BZ2File that imparts `with` powers.

    Only required in Python <= 2.6.
    """
    pass

class gzfile(gzip.GzipFile, WithMixin):
    """Wrapper around gzip.GzipFile that imparts `with` powers.

    Only required in Python <= 2.6.
    """

    def close(self):
        super(gzfile, self).close()
        if self.fileobj is not None:
            self.fileobj.close()


class canopener(object):
    """Convenience opener. Seamlessly decompresses .gz and .bz2 URLs and files.
    """

    def __new__(cls, filename, mode='r'):
        # Open the base file stream.
        parse = urlparse.urlparse(filename)
        if parse.netloc:
            if mode[0] != 'r':
                raise ValueError("can't write to URLs")
            base_file = urllib2.urlopen(filename)
        else:
            base_file = open(filename, mode)

        # Now wrap it in any decompression.
        if filename.endswith('.gz'):
            return gzfile(fileobj=base_file, mode=mode)
        elif filename.endswith('.bz2'):
            return bz2file(base_file, mode)
        else:
            return base_file