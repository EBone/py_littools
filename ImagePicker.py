import threading
import os
import re
import time
import sys

class ImagePicker():
    def __init__(self, path, num_keep, file_name_digits):
        self._path = path

        self._worker = ImagePickerWorker(path, num_keep, file_name_digits)
        self._worker.start()

    def get_newest_image(self):
        if self._worker._newest_image:
            image_path = os.path.join(self._path, self._worker._newest_image)
            b_data = open(image_path, "rb").read()
            return b_data
        else:
            return None

    def __del__(self):
        self._worker._should_exit = True
        self._worker.join()


class ImagePickerWorker(threading.Thread):
    path_pattern = re.compile(r"_(\d+)\.\w+$")

    def __init__(self, path, num_keep, file_name_digits):
        threading.Thread.__init__(self)
        self._path = path
        self._num_keep = num_keep
        self._max_file_id = 10 ** file_name_digits - 1

        self._should_exit = False
        self._newest_image = None

    def run(self):
        while True:
            if self._should_exit == True:
                break

            files = os.listdir(self._path)
            if len(files) >= 2:

                file_compare_list = []
                for curr_file in files:
                    try:
                        ctime = os.stat(os.path.join(self._path, curr_file)).st_ctime
                    except:
                        ctime = 0
                    id = self.path_pattern.search(curr_file).groups()[0]
                    file_compare_list.append( [curr_file, ctime, int(id)] )

                    file_compare_list =sorted(file_compare_list, cmp=self._compare)

                # check for ID loop back
                if file_compare_list[-1][2] == self._max_file_id :
                    for item in file_compare_list:
                        if item[2] < self._max_file_id / 2:
                            item[2] += self._max_file_id + 1
                    #print(file_compare_list)
                    #print(file_compare_list)
                    file_compare_list=sorted(file_compare_list, cmp=self._compare)
                    #print(file_compare_list)
                templist=[i[2] for i in file_compare_list]
                print(templist)

                self._newest_image = file_compare_list[-2][0]
                num = len(files)
                if num > self._num_keep:
                    for item in file_compare_list[:num - self._num_keep]:
                        try:
                            os.remove(os.path.join(self._path, item[0]))
                        except OSError as err:
                            print(os.strerror(err.errno))
                            print("__________________" + item[0] + "_________________")
                            sys.exit(-1)
            time.sleep(0.001)

    def _compare(self, x, y):
        if x[1] == y[1]:
            return x[2] - y[2]
        elif x[1]>y[1]:
            return 1
        else:
            return -1
