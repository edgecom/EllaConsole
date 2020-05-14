import builtins

console_end = '\033[0m'
console_red = '\033[91m'
console_blue = '\033[94m'
console_warning = '\u001b[35m'


def print_err(self, *args):
    print(console_red, end = "")
    print(self, *args)
    print(console_end, end = "")


def print_warn(self, *args):
    print(console_warning, end = "")
    print(self, *args)
    print(console_end, end = "")


def print_debug(self, *args):
    print(console_blue, end = "")
    print(self, *args)
    print(console_end, end = "")


def print_info(self, *args):
    print(self, *args)

def expand_console_to_builtins():
    builtins.print_err = print_err
    builtins.print_warn = print_warn
    builtins.print_debug = print_debug
    builtins.print_info = print_info
    pass


end = '\033[0m'
red = '\033[91m'
blue = '\033[94m'
#warning = '\033[93m'
warning = '\u001b[35m' #je tu magenta, lebo zltu ze vidno v bielom skine


def Print(data):
    start = ""
    lineEnd = ""

    if (data.lower().find("[trace]:") != -1):
        pass
    elif (data.find("[error]:") != -1 or data.find("[fatal]:") != -1):
        start = red
        lineEnd = end
    elif (data.lower().find("[info]:") != -1):
        pass
    elif (data.lower().find("[debug]:") != -1):
        start = blue
        lineEnd = end
    elif (data.lower().find("[warning]:") != -1):
        start = warning
        lineEnd = end
    else:
        data = ""

    #data = data.split("\n")

    #for i in data: if (i != "\n"):
    if (data == ""):
        pass
    elif (data == "\n"):
        pass
    else:
        print(start, end = '')
        data = data.split('\\n')
        for i in data:
            print(i)
        print(end, end = '')
    pass
