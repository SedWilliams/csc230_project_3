import src.data as data

# character representation for shaded/blank cells
SHADED = "#"
BLANK = " "


for row in data.features:
    row_id = row[0] #element 1 (index -1) is ID
    feats = row[1:16] #elements 2-16 (inclusive, index -1) are features
    output = row[16] #element 17 (index -1) is output

    grid = feats.reshape(5, 3) # use numpy to create the required 5x3 grid from the features
    print(f"Row {row_id} (output: {output})")

    for row in grid:
        # Shaded if value is 1, blank if value is 0
        print("".join(SHADED if cell else BLANK for cell in row))

    # print a blank line after each grid
    print()
