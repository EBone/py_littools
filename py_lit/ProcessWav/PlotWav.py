import  matplotlib.pyplot as plt


def draw_wav(data):
    data_len=len(data)
    x=[i for i in range(data_len)]
    plt.plot(x,data)
    plt.show()

