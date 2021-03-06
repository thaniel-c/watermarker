# Watermarker
---

## Project Info

Automatic advanced watermark producing tool. This tool uses randomized image distortion and randomized placement in order to circumvent new machine learning approaches which automatically strip watermarks from images. This also prevents people from using simple image editors from editing out the watermarks without cropping or losing portions of the image. This tool will help to ensure security of your names, logos, symbols, etc. on your images.

## Usage Examples
---

To watermark an image, you need two images, a source image and the applied watermark image.

Source image.
<img src="https://github.com/thaniel-c/misc-tools-and-projects/blob/master/WatermarkerResources/nasa_original.jpg"
     alt="nasa_original"
     width ="400" height="400" />

Applied watermark image.
<img src="https://github.com/thaniel-c/misc-tools-and-projects/blob/master/WatermarkerResources/nasa_logo.png"
     alt="nasa_original"
     width ="60" height="50" />
     

When the images are given as inputs into Watermarker the resulting image will be saved as 'done.png' in its root directory. 
The following example is done with maximum distortion which can be tuned using the ui.

<img src="https://github.com/thaniel-c/misc-tools-and-projects/blob/master/WatermarkerResources/done.png"
     alt="nasa_original"
     width ="400" height="400" />

As you can see it would be pretty hard to seperate this watermark from the image without ruining it. However, this example is drastic as many parameters can be changed within the program to make the watermark more subtle.

This method of distortion was chosen because of its balance between discernability and function. The name 'NASA' is very easy to read and recognize, however with the distortion it makes it harder for a machine learning algorithm or a person to locate and remove the watermark from the image. 
