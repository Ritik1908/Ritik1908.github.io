#[cv2.IMWRITE_JPEG_QUALITY, 0]
#[cv2.IMWRITE_PNG_COMPRESSION, 0]
import cv2
import numpy
import os
import time

height = int(input("Enter height of images after processing : "))
width = int(input("Enter width of images after processing : "))
png_compression = int(input("Enter Quality factor for .png image -> (0 - 9), 0 means high : "))
jpg_compression = int(input("Enter Quality factor for .jpg image -> (0 - 95), 95 means high : "))

#To get the current working directory of the ImageProcessing
cwd = os.getcwd()
print("\ncurrent Working Directory : "+cwd)

#To get the path from where images will be read
raw_image_path = cwd+"//Images"

#To get list of all images in that directory
images = os.listdir(raw_image_path)
raw_image_path = raw_image_path+"//"

print("\nImages will be read from the path : "+raw_image_path)

#Destination to keep processed images
processed_image_path = cwd+"//ResizedImages//"
print("\nProcessed Images will be saved to : "+processed_image_path)

print("\nStarting script to process this images : ")
print(images)

#Loop to iterate over all images
for img in images : 
	print("Processing : "+img)
	#To read image from file path
	img_read = cv2.imread(raw_image_path+img)
	#To show unprocessed image to user
	cv2.imshow("Before Processing",img_read)
	#wait until user presses a key
	cv2.waitKey(1000)
	cv2.destroyAllWindows()

	#To resize image to specific width and height
	resized_image = cv2.resize(img_read, (width, height))
	#cv2.imshow("After resize", resized_image)
	#cv2.waitKey(0)

	#saving the image to designated path
	if ".jpg" in img :
		cv2.imwrite(processed_image_path+img, resized_image, [cv2.IMWRITE_JPEG_QUALITY, jpg_compression])
	elif ".png" in img :
		cv2.imwrite(processed_image_path+img, resized_image, [cv2.IMWRITE_PNG_COMPRESSION, png_compression])
	else :
		cv2.imwrite(processed_image_path+img, resized_image)

	#To display processed image to user
	
	#processed_image = cv2.imread(processed_image_path+img)
	#cv2.imshow("Image After Processing", processed_image)
	#cv2.waitKey(1000)
	#cv2.destroyAllWindows()
