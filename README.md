# KLImageEditor

There are 8 functions connected by buttons.
- open_image
This asks the user to pick the file with "filedialog.askopenfilename".
Then it opens the file with Image.open.
Then it resizes the image to fit on the page with image.resize().
Then adds it to the page with canvas.create_image.
- flip_image
This opens the image with Image.open.
Then flips it with .transpose()
- rotate_image
This opens then rotates the image.
- apply_filter
This changes the theme on the image.
- draw
This allows the user to draw on the page.
- change_color
This asks the user to pick the color.
- erase_lines
This allows the user to erase drawings.
- save_image
This saves the image.