# python3 -m venv .venv
# source .venv/bin/activate
# pip install azure-storage-blob
# deactivate
import io
import pyPdf
import PIL.Image

infile_name = 'my.pdf'

with open(infile_name, 'rb') as in_f:
    in_pdf = pyPdf.PdfFileReader(in_f)
    for page_no in range(in_pdf.getNumPages()):
        page = in_pdf.getPage(page_no)

        # Images are part of a page's `/Resources/XObject`
        r = page['/Resources']
        if '/XObject' not in r:
            continue
        for k, v in r['/XObject'].items():
            vobj = v.getObject()
            # We are only interested in images...
            if vobj['/Subtype'] != '/Image' or '/Filter' not in vobj:
                continue
            if vobj['/Filter'] == '/FlateDecode':
                # A raw bitmap
                buf = vobj.getData()
                # Notice that we need metadata from the object
                # so we can make sense of the image data
                size = tuple(map(int, (vobj['/Width'], vobj['/Height'])))
                img = PIL.Image.frombytes('RGB', size, buf,
                                          decoder_name='raw')
                # Obviously we can't really yield here, do something with `img`...
                yield img
            elif vobj['/Filter'] == '/DCTDecode':
                # A compressed image
                img = PIL.Image.open(io.BytesIO(vobj._data))
                yield img


# xargs -n 1 curl -O < descarga.txt
# create data.txt name cod
# remove https
# replace blanks by %20
# filter .heic and generate compatible file
# filter .pdf and extrac img

