class StarCookie:
    def __init__(self, color) -> None:
        print("The cookie is ready ....")
        self.color = color


cookie1 = StarCookie("red")
cookie2 = StarCookie("blue")


print(cookie2.color)
print(cookie1.color)
print(cookie2.__dict__)

# Updates this as a new attribute and puts this as a default value for all the objects
StarCookie.milk = 0.2
