import sys, zlib

with open('assets/fonts/dejavu/DejaVuSansMono.ttf', 'rb') as f:
    data = f.read()

# Write as raw C array (uncompressed)
with open('src/DejaVuSansMono_embedded.h', 'w') as out:
    out.write('// DejaVu Sans Mono - Embedded font data\n')
    out.write('// Auto-generated from DejaVuSansMono.ttf (%d bytes)\n' % len(data))
    out.write('// License: Bitstream Vera / DejaVu Fonts License (free/open)\n')
    out.write('#pragma once\n\n')
    out.write('static const unsigned int DejaVuSansMono_ttf_size = %d;\n' % len(data))
    out.write('static const unsigned char DejaVuSansMono_ttf_data[%d] = {\n' % len(data))
    
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        line = ', '.join('0x%02x' % b for b in chunk)
        if i + 16 < len(data):
            out.write('    %s,\n' % line)
        else:
            out.write('    %s\n' % line)
    
    out.write('};\n')

print('Generated src/DejaVuSansMono_embedded.h (%d bytes font data)' % len(data))
