# LuLaRizer

Python script to add style, size, and price to clothing photos.

I was going to make this repository private but was surprised to find a few people were already following. I assume you are LuLaRoe husbands, so I consider you my brothers. In the spirit of shared adversity, I have added some reasonable command line arguments and this quick introduction.

## System Requirements

I am developing and running the script on OSX. It probably wouldn't be difficult to get it running on a Windows machine (probably just changing forward slashes to backward), but I don't have one at the moment for testing. It's on my to-do list.

You will need to install Python. I successfully tested the lularize.py script with both Python 2.7 and Python 3.5, so choose whichever you think is best.

This script relies heavily on PIL (the Python Image Library) so you will need to install that. I am using the Pillow fork which is easy to install if you have *pip*.

    pip install Pillow

If you don't have *pip*, you should be able to get it like so:

    python get-pip.py

## Usage

When the lularizer is pointed at a directory path, it will look for subdirectories that have the names of LuLaRoe styles. It will add that style name and its price to any photos found there. Then it will look for subdirectories of the style folder and assume they are sizes. It will then process all photos and add the name of the size directory as well.

Size directories can be named anything you like, but the style directories must named exactly one of these for the automatic price to be found. And to keep the script from failing.

- joy
- tween
- tall_&_curvy
- kids_s/m
- sloan
- sarah
- randy
- perfect_t
- patrick
- one_size
- nicole
- monroe
- maxi
- madison
- kids_l/xl
- lucy
- lola
- lindsay
- kids_azure
- julia
- jordan
- jill
- jade
- irma
- gracie
- dotdotsmile
- classic_t
- cassie
- azure
- ana
- amelia
- carly

The processed files will be saved as `style_size_i.jpg` in the same location as the source file (by default) where *i* is the first number not found in another file in the same directory, starting at 1. The lularize process checks the file name and won't reprocess any with that format.

## Recommended Setup

I made a folder on the desktop for copies of photos to be added to the appropriate subdirectories, then made a bash script to call the Python script with the desired parameters.

    #!/bin/bash
    # Change to directory where the script is
    cd /Users/Stacy/LuLaRoe/lularizer
    # Execute the script with parameters
    python3 lularize.py /Users/Stacy/Desktop/lularizer -w "LuLaRoe Stacy Leasure-Broski" -r

Don't forget to make the bash script executable.

    chmod 755 lularize.sh

## Options

You can get information about the command line options in the standard way:

    python lularize.py -h

And you'll get something like this:

    positional arguments:
      source                Parent directory of photos

    optional arguments:
      -h, --help            show this help message and exit
      --watermark WATERMARK, -w WATERMARK
                            Message embossed over bottom of photo
      --export EXPORT, -e EXPORT
                            Directory path where processed photos will be saved
      --detail DETAIL DETAIL, -d DETAIL DETAIL
                            Use a close-up centered at this % x, y position
                            instead of logo
      --remove, -r          Delete source photo once processed
      --upload, -u          Create symlinks in an upload folder by style only

### Upload Argument

This new feature was implemented because after everything is processed, the photos are in separate folders by size. This makes it inconvenient when uploading files by style. If the `-u` flag is present, a folder called *upload* is created in the export path. A style folder is created inside the upload folder only if at least one photo of that style exists. Then, a symlink for all photos of that style is created in that folder, without size folders.
