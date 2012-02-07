#!/usr/bin/env python

def file_to_data_uri(filepath, use_base64 = False, check_mimetypes = True,
                     force_mimetype = False, force_encoding = False):
    args = {}
    format = 'data:'

    args['data'] = open(filepath, 'r').read()

    if check_mimetypes:
        import mimetypes
        (args['mimetype'], args['encoding']) = mimetypes.MimeTypes().guess_type(filepath)

    if force_mimetype:
        args['mimetype'] = force_mimetype
    if force_encoding:
        args['encoding'] = force_encoding

    if 'mimetype' in args and args['mimetype']:
        format += '%(mimetype)s'
    if 'encoding' in args and args['encoding']:
        format += ';charset=%(encoding)s'

    if use_base64:
        import base64
        format += ';base64,%(b64data)s'
        args['b64data'] = base64.b64encode(args['data'])
    else:
        import urllib
        args['urldata'] = urllib.quote(args['data'])
        format += ',%(urldata)s'

    return format % args

if __name__ == "__main__":
    import sys
    print file_to_data_uri(sys.argv[1])



