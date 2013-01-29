"""
Tools for manipulating documentation
"""

def build_typealong(rstfile, outfile):
    """extract indented code sample sections along with slide headers 
    
    builds a type-along file that provides cut-and-paste for all code samples
    in a slide presentation.
    """
    in_lines = rstfile.readlines()
    type_buffer = []
    prev_line = ''
    
    def get_header(cur, prev):
        if cur.startswith('----'):
            return (prev, cur, '\n')
        return ()
    
    for line in in_lines:
        header = get_header(line, prev_line)
        if header:
            print "outputting a slide header"
            outfile.writelines(header)
        else:
            if line.startswith('    '):
                # omit `    :class: blah' type lines
                if not line[4] == ':':
                    type_buffer.append(line)
            elif line.startswith('\n'):
                if type_buffer:
                    print "outputting a typeable section"
                    type_buffer.extend(['\n', '\n'])
                    outfile.writelines(type_buffer)
                    type_buffer = []
        prev_line = line