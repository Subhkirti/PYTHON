def outer():
    def inner():
        print("go to outer")
        print("go to inner")
    inner()
outer()
