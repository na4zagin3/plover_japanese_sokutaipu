# YTHKSAIOtk*inOIASKHTY
KEYS = (
    '#',
    'Y-', 'T-', 'H-', 'K-', 'S-', 'A-', 'I-', 'O-',
    't', 'k',
    '*',
    'i', 'n',
    '-O', '-I', '-A', '-S', '-K', '-H', '-T', '-Y',
)

IMPLICIT_HYPHEN_KEYS = ('t', 'k', '5-', '0-', 'i', 'n', '*')

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

# ToDo: How to type numbers?
NUMBERS = {
    'Y-': '1-',
    'H-': '2-',
    'S-': '3-',
    'I-': '4-',
    't':  '5-',
    'k':  '0-',
    '-I': '-6',
    '-S': '-7',
    '-H': '-8',
    '-Y': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
]

ORTHOGRAPHY_RULES_ALIASES = {
}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'Y-'   : ('a', 'q'),
        'T-'   : 'w',
        'H-'   : 's',
        'K-'   : 'e',
        'S-'   : 'd',
        'A-'   : 'r',
        'I-'   : 'f',
        'O-'   : ('t', 'g'),
        't'    : 'c',
        'k'    : 'v',
        '*'    : 'b',
        'i'    : 'n',
        'n'    : 'm',
        '-O'   : ('y', 'h'),
        '-I'   : 'u',
        '-A'   : 'j',
        '-S'   : 'i',
        '-K'   : 'k',
        '-H'   : 'o',
        '-T'   : 'l',
        '-Y'   : ('p', ';'),
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', ',', '.', '/', '[', ']', '\'', '\\'),
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'Y-'   : ('X1-', 'X2-'),
        'T-'   : 'S2-',
        'H-'   : 'S1-',
        'K-'   : 'K-',
        'S-'   : 'T-',
        'A-'   : 'W-',
        'I-'   : 'P-',
        'O-'   : ('H-', 'R-'),
        't'    : 'A-',
        'k'    : 'O-',
        '*'    : ('X3', '*1', '*2'),
        'i'    : '-E',
        'n'    : '-U',
        '-O'   : ('-F', '-R'),
        '-I'   : '-P',
        '-A'   : '-B',
        '-S'   : '-L',
        '-K'   : '-G',
        '-H'   : '-T',
        '-T'   : '-S',
        '-Y'   : ('-D', '-Z'),
    },
}

DICTIONARIES_ROOT = 'asset:plover_japanese_sokutaipu:assets'
DEFAULT_DICTIONARIES = (
    'user.json',
    'commands.json',
    'syllables.json'
)
