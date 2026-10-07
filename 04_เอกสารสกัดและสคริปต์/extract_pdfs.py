import os

try:
    from pdfminer.high_level import extract_text
    lib = 'pdfminer'
except ImportError:
    try:
        import PyPDF2
        lib = 'pypdf2'
    except ImportError:
        lib = None

if lib is None:
    print('No PDF library available, trying pip install')
    os.system('pip install pdfminer.six')
    from pdfminer.high_level import extract_text
    lib = 'pdfminer'

base = r'c:\Users\chinj\OneDrive\ปี3\COM2703-เครือข่าย'

for ch in ['chapter5.pdf', 'chapter6.pdf', 'chapter7.pdf']:
    path = os.path.join(base, ch)
    outpath = os.path.join(base, ch.replace('.pdf', '_extracted.txt'))
    if lib == 'pdfminer':
        text = extract_text(path)
    else:
        import PyPDF2
        reader = PyPDF2.PdfReader(path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'{ch}: extracted {len(text)} chars')
