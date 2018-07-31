# color-detection
### Detection of a specific colour intensity in a given image.

Pre requisites: python 3, opencv library 

Python used for scripting the code.

Opencv library is a building block of computer vision and here it is used for reading image in python script.

Images are multidimensional array of pixels and each pixel contains 3 values of colour intensity that are blue,green,red. With help of opencv library we can get that array.
	Each pixel = [blue intensity, red intensity, green intensity]

Conversion of RGB to HSV(Hue Saturation Value) values:
In RGB mode every colour depends upon the all three value but in HSV mode hue is the colour portion of the colour model, saturation is the amount of grey in colour in 0 to 100 percent and value works with saturation to and describe the brightness of colour from 0 to 100 percent .

## Hue range for choosing colour

|HUE|Angle|Value|
|------|-------|--------|
|Red|0-60|0-30|
|Yellow|60-120|30-60|
|Green|120-180|60-90|
|Cyan|180-240|90-120|
|Blue|240-300|120-150|
|Magenta|300-360|150-180|

Range of Saturation and brightness value 0 to 255.

Selecting hue values from H-10 to H+10, saturation and brightness 100-255 will give best result

For the red colour, range determination was a problem. For that purpose two ranges were taken one from 170 to 180 and one from 0 to 10 and both output was added and this provide us better result.

Example:

Input image
![alt text](https://github.com/nikarora1111/color-detection/blob/master/input.jpg)

Output Image:

![alt text](https://github.com/nikarora1111/color-detection/blob/master/output.JPG)
