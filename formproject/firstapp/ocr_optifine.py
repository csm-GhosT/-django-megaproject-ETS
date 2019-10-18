from PIL import Image
import pytesseract
import argparse
import cv2
import os

def main():


    IMAGES_DIR = os.path.join(os.getcwd(),"media")
    # print(IMAGES_DIR)
    for fileName in os.listdir(IMAGES_DIR):
     print("")

    im_dir=os.path.join(IMAGES_DIR, fileName)

    image = cv2.imread(im_dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    return text

    # show the output images
    # cv2.imshow("Image", image)
    # cv2.imshow("Output", gray)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
