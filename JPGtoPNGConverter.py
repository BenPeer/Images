import sys
import os
from PIL import Image

if __name__ == '__main__':
    # grab the first and second argument for usage: JPGtoPNGConverter "Pokemon\" "new\"
    pokemon_folder = sys.argv[1]
    new_folder = sys.argv[2]

    # check if "new" folder exist, if not create it
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # loop through Pokemon folder ; # convert images to png ; # save ot new folder

    for jpg_file in os.listdir(pokemon_folder)
        full_path_file = pokemon_folder + jpg_file
        img = Image.open(full_path_file)
        if 'JPEG' == img.format:
            png_file = full_path_file.replace(".jpg", ".png")
            png_file = png_file.replace(pokemon_folder, new_folder)
            img.save(png_file, 'png')
        else:
            print(f'invalid file format: {full_path_file}')
