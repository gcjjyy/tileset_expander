import sys
from PIL import Image

tileset_expand_table = [
    [ 0,  1,  4,  5], [16, 19, 20, 23], [10, 11, 22, 23], [ 2, 19, 22, 23],
    [ 0, 19, 22, 23], [ 8,  9, 20, 21], [16,  3, 20, 21], [16, 17, 20, 21],
    [10,  9, 22, 21], [ 2,  3, 22, 21], [ 0,  3, 22, 21], [ 2,  1, 22, 21],
    [ 0,  1, 22, 21], [ 8, 11, 12, 15], [16, 19, 12, 15], [10, 11,  6, 15],
    [ 2, 19,  6, 15], [ 0, 19,  6, 15], [ 8,  9, 12,  7], [16,  3, 12,  7],
    [16,  1, 12,  7], [10,  9,  6,  7], [ 2,  3,  6,  7], [ 0,  3,  6,  7],
    [ 2,  1,  6,  7], [ 0,  1,  6,  7], [10, 11, 14, 15], [ 2, 19,  4, 15],
    [ 0, 19,  4, 15], [10,  9,  4,  7], [ 2,  3,  4,  7], [ 0,  3,  4,  7],
    [ 2,  1,  4,  7], [ 0,  1,  4,  7], [ 8,  9, 12, 13], [16,  3, 12,  5],
    [16,  1, 12,  5], [10,  9,  6,  5], [ 2,  3,  6,  5], [ 0,  3,  6,  5],
    [ 2,  1,  6,  5], [ 0,  1,  6,  5], [10,  9,  4,  5], [ 2,  3,  4,  5],
    [ 0,  3,  4,  5], [ 2,  1,  4,  5], [ 0,  1,  4,  5], [ 8, 11, 20, 23]
]

if len(sys.argv) < 3:
    print('Usage: %s <input filename> <output filename> [margin]' % (sys.argv[0]))
    exit()

margin = 0
if len(sys.argv) >= 4:
    margin = int(sys.argv[3])

original = Image.open(sys.argv[1])

# Crop original tileset to 8x8 unit tiles
unitTiles = []
for i in range(0, 6):
    for j in range(0, 4):
        unitTile = original.crop((j * 8, i * 8, (j + 1) * 8, (i + 1) * 8))
        unitTiles.append(unitTile)

tileset = Image.new('RGB', (16 * 8 + (margin * 7), 16 * 6 + (margin * 5)))

posx = 0
posy = 0

for tile_table in tileset_expand_table:
    tileset.paste(unitTiles[tile_table[0]], (posx, posy, posx + 8, posy + 8))
    tileset.paste(unitTiles[tile_table[1]], (posx + 8, posy, posx + 16, posy + 8))
    tileset.paste(unitTiles[tile_table[2]], (posx, posy + 8, posx + 8, posy + 16))
    tileset.paste(unitTiles[tile_table[3]], (posx + 8, posy + 8, posx + 16, posy + 16))

    posx += 16 + margin
    if posx >= 16 * 8 + (margin * 7):
        posx = 0
        posy += 16 + margin

tileset.save(sys.argv[2])
