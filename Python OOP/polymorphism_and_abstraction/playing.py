def start_playing(obj):
    return obj.play()


class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))