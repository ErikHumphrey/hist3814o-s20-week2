# install only the first time
install.packages('magick')
install.packages('tesseract')

# tell R which packages you need
library(magick)
library(magrittr)
library(tesseract)

# now let's create a variable called 'text'
# and read the image into it
# and we'll modify the image to give us
# the best chance of reading the text
# the final line, image_ocr() does the text extraction

# remember to set your working directory to whatever folder
# contains the stuff you want to work on.
text <- image_read("e001518030.jpg") %>%
  image_resize("2000") %>%
  image_convert(colorspace = 'gray') %>%
  image_trim() %>%
  image_ocr()

write.table(text, "output.txt")
