import math
import random
from PIL import Image, ImageStat

def scramble_pixels(img, cell_rows, cell_columns):

	'''
	Description:
		This function will split the image into a grid
		of length cell_rows and width of cell_columns
		and randomly shuffle the cells in the grid 
		

	Args: 
		img(Image): the base image
		cell_rows(int): the number of cells in each row
		cell_columns(int): the number of cells in each column

	Output: 
		This function outputs a new image
	'''

	image_width = img.size[0] # width of the base image
	image_height = img.size[1] # height of the base image
	
	# displays warning about inputed cell_rows and cell_column values
	if image_width % cell_rows != 0 or image_height % cell_columns != 0: 
		print('WARNING: for best results the number of rows and number of columns should evenly divide into the width and height of the image.')
	
	cell_width = math.ceil(image_width / cell_rows) # width of each cell for the base image
	cell_height = math.ceil(image_height / cell_columns) # height of each cell for the base image

	# coordinates to crop the image (left top (x, y) and right bottom (x, y))
	left = 0
	top = -cell_height
	right = cell_width
	bottom = 0

	new_image = Image.new('RGB', img.size, color = 'red' )
	
	cropped_image_list = []
	image_coordinate_list = []


	for column in range(0, cell_columns):

		top += cell_height
		bottom += cell_height
		left = 0
		right = cell_width

		for row in range(0, cell_rows):

			image_coordinate_list.append([left, top, right, bottom])
			cropped_image_list.append(img.crop((left, top, right, bottom)))
			right += cell_width 
			left += cell_width

	random.shuffle(cropped_image_list)
	for index, coord in enumerate(image_coordinate_list):
		new_image.paste(cropped_image_list[index], coord)



	new_image.show()
	


iphone8_resolution = [750, 1334]
laptop_resolution = [1920, 1080]

image1 = Image.open(r'C:\Users\img.PNG') # The image's file path


scramble_pixels(image8, 50, 50)
#image6.show() # shows the original image


