"""
the instruction is now available in Markdown format in WIKI.md

the example below is Gruvbox, a really nice color scheme which inspired this project
"""
palette = [
  {'file_name': 'test-png'},
  [
    ('282828', 'bg',     '235', '0'),
    ('CC241D', 'red',    '124', '1'),
    ('98971A', 'green',  '106', '2'),
    ('D79921', 'yellow', '172', '3'),
    ('458588', 'blue',   '66',  '4'),
    ('B16286', 'purple', '132', '5'),
    ('689D6A', 'aqua',   '72',  '6'),
    ('A89984', 'gray',   '246', '7'),
  ],
  [
    ('928374', 'gray',   '245', '8'),
    ('FB4934', 'red',    '167', '9'),
    ('B8BB26', 'green',  '142', '10'),
    ('FABD2F', 'yellow', '214', '11'),
    ('83A598', 'blue',   '109', '12'),
    ('D3869B', 'purple', '175', '13'),
    ('8EC07C', 'aqua',   '108', '14'),
    ('EBDBB2', 'fg',     '223', '15'),
  ],
  [
    ('1D2021', 'bg0_h',  '234', '0'),
    ('282828', 'bg0',    '235', '0'),
    ('3C3836', 'bg1',    '237', '-'),
    ('504945', 'bg2',    '239', '-'),
    ('665C54', 'bg3',    '241', '-'),
    ('7C6f64', 'bg4',    '243', '-'),
    ('928374', 'gray',   '245', '8'),
    ('D65D0E', 'orange', '166', '-'),
  ],
  [
    ('0000',),
    ('32302F', 'bg0_s',  '236', '0'),
    ('A89984', 'fg4',    '246', '7'),
    ('BDAE93', 'fg3',    '248', '-'),
    ('D5C4A1', 'fg2',    '250', '-'),
    ('EBDBB2', 'fg1',    '223', '15'),
    ('FBF1C7', 'fg0',    '229', '-'),
    ('FE8019', 'orange', '208', '-'),
  ],
]

if __name__ == '__main__':
    from prev_gen import Previewer
    Previewer(palette)
