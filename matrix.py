import js
from pyodide.ffi import create_proxy
import random

canvas = document.getElementById("canvas")
ctx = canvas.getContext("2d")

cw = js.window.innerWidth
ch = js.window.innerHeight

canvas.width = cw
canvas.height = ch

font_size = 13
max_colums = cw // font_size
char_arr = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "А",
  "В",
  "Г",
  "Д",
  "Є",
  "Ѕ",
  "З",
  "И",
  "Ѳ",
  "І",
  "К",
  "Л",
  "М",
  "Н",
  "Ѯ",
  "Ѻ",
  "П",
  "Ч",
  "Р",
  "С",
  "Т",
  "Ѵ",
  "Ф",
  "Х",
  "Ѱ",
  "Ѿ",
  "Ц",
]


def resize(event):
    global max_colums, canvas

    cw = js.window.innerWidth
    ch = js.window.innerHeight

    canvas.width = cw
    canvas.height = ch

    max_colums = cw // font_size


resize_proxy = create_proxy(resize)
js.window.addEventListener("resize", resize_proxy)

max_char_count = 300
falling_char_attr = []
frames = 0


class FallingChar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, ctx):
        self.value = char_arr[int(random.random() * len(char_arr))]
        self.speed = (random.random() * font_size * 3) / 4 + (font_size * 3) / 4

        ctx.fillStyle = "rgba(0, 255, 0)"
        ctx.font = str(font_size) + "px sans-serif"
        ctx.fillText(self.value, self.x, self.y)
        self.y += self.speed

        if self.y > ch:
            self.y = (random.random() * ch) / 2
            self.x = (random.random() * max_colums) * font_size
            self.speed = (random.random() * -1 * font_size * 3) / 4 + (font_size * 3) / 4


def update(e):
    global frames

    if len(falling_char_attr) < max_char_count:
        falling_char = FallingChar(
            random.random() * max_colums * font_size,
            (random.random() * ch) / 2
        )

        falling_char_attr.append(falling_char)

    ctx.fillStyle = "rgba(0, 0, 0, 0.05)"
    ctx.fillRect(0, 0, cw, ch)

    for i in range(len(falling_char_attr)):
        if frames % 2 == 0:
            falling_char_attr[i].draw(ctx)

    js.window.requestAnimationFrame(create_proxy(update))
    frames += 1

update(1)


