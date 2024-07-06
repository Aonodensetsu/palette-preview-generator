from typing import TypeAlias, Literal

image_format: TypeAlias = Literal[
    'png',
    'svg'
]

config_format: TypeAlias = Literal[
    'py',
    'yml',
    'json',
    'toml'
]

# generate static list of color formats
# from colour.graph.conversion import CONVERSION_SPECIFICATIONS_DATA
# print(',\n'.join(set(f'    \'{x[0].lower()}\'' for x in CONVERSION_SPECIFICATIONS_DATA)))

color_format: TypeAlias = Literal[
    'cmy',
    'din99',
    'ycocg',
    'cam16',
    'jzch',
    'output-referred rgb',
    'ichpt ragoo 2021',
    'munsell colour',
    'cam02ucs',
    'hunter rdab',
    'ihls',
    'scene-referred rgb',
    'itch',
    'zcam',
    'ycbcr',
    'mired',
    'cam16 jmh',
    'hunter lchab',
    'cam16scd',
    'ciecam02',
    'icacb',
    'spectral distribution',
    'ciecam02 jmh',
    'igch',
    'osa ucs',
    'hunter rdchab',
    'prolab',
    'cie uvw',
    'cie xyy',
    'cie 1960 ucs',
    'rgb luminance',
    'cie 1931',
    'cie luv uv',
    'css color 3',
    'cam16ucs',
    'oklab',
    'izazbz',
    'luminance',
    'cmyk',
    'lightness',
    'kim 2009',
    'hellwig 2022 jmh',
    'wavelength',
    'cie lab',
    'ich',
    'hdr-ich',
    'ciecam16 jmh',
    'hunter lab',
    'hdr-ipt',
    'cie xy',
    'yrg',
    'munsell value',
    'cct',
    'hexadecimal',
    'rgb',
    'cie xyz',
    'hdr-cielchab',
    'cam02lcd',
    'srgb',
    'ipt',
    'cie ucs uv',
    'hellwig 2022',
    'cie 1976 ucs',
    'iach',
    'cie lchuv',
    'hsv',
    'cie lchab',
    'ictcp',
    'cie luv',
    'yccbccrc',
    'prolchab',
    'jzazbz',
    'oklch',
    'cam02scd',
    'igpgtg',
    'ciecam16',
    'izch',
    'cie ucs',
    'hdr-cielab',
    'hcl',
    'cam16lcd',
    'hsl',
    'ipt ragoo 2021',
    'prismatic'
]
