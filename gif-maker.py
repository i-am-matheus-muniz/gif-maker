import imageio.v3 as iio

filenames = ['sung-jinwoo-1.jpg', 'sung-jinwoo-2.jpg', 'sung-jinwoo-3.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('sung-jinwoo.gif', images, duration = 500, loop = 0)