from JavavaPi.ImagePicker import ImagePicker
import os
import time
import sys


path = "./image_picker_test_dir"

if not os.path.exists(path):
    os.mkdir(path)
picker = ImagePicker(path, 5, 2)

counter = 0
#sys.stdout=open('log.txt','w')
#sys.stderr=open('log_error.txt','w')
while True:

    num_str = "%02d" % counter
    num_str = num_str[-2:]
    filename = path + "/test_%s.jpg" % num_str

    filewritter = open(filename, "w")
    filewritter.write(str(counter))
    filewritter.close()
    print(os.stat(filename).st_ctime)
    counter += 1

    print("counter {}, file: ".format(counter))
    print(picker.get_newest_image())

    time.sleep(0.3)

