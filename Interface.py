from __future__ import division
from asciimatics.effects import Scroll, Mirage, Wipe, Cycle, RandomNoise, Matrix, \
    BannerText, Stars, Print
from asciimatics.particles import DropScreen, Explosion, RingFirework
from asciimatics.renderers import FigletText, SpeechBubble, Rainbow, Fire, ColourImageFile, ImageFile
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from pyfiglet import Figlet
import asciimatics
import sys


def _credits(screen):
    scenes = []

    text = Figlet(font="banner", width=200).renderText("JPT-x7")
    width = max([len(x) for x in text.split("\n")])

#    effects = [
#        Print(screen,
#             FigletText("JPT-x7", "banner"),
#              screen.height - 9, x=(screen.width - width) // 2 + 1,
#              colour=Screen.COLOUR_BLACK,
#              bg=Screen.COLOUR_BLACK,
#              speed=1),
#        Print(screen,
#              FigletText("JPT-x7", "banner"),
#              screen.height - 9,
#              colour=Screen.COLOUR_WHITE,
#              bg=Screen.COLOUR_WHITE,
#              speed=1),
#    ]
#    scenes.append(Scene(effects, 100))

    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            Rainbow(screen, FigletText("JPT-x7")),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("JPT-x7"),
            screen.height // 2 - 3,
            start_frame=200),
#        Print(screen,ColourImageFile(screen, "Dancin.gif", screen.height-2,uni=screen.unicode_aware),0,stop_frame=200)
          ]
    scenes.append(Scene(effects, 250, clear=False))

    effects = [
     #   BannerText(
      #      screen,
       #     Rainbow(screen, FigletText(
        #        "Twitter Scrapers, Username Generators, and More!", font='slant')),
         #   screen.height // 2 - 3,
          #  Screen.COLOUR_GREEN)
          Scroll(screen, 3),
          Mirage(screen, Rainbow(screen, FigletText("Twitter Scrapers")),screen.height+8, Screen.COLOUR_GREEN),
          Mirage(screen, Rainbow(screen, FigletText("Username Generators")),screen.height+16, Screen.COLOUR_GREEN),
          Mirage(screen, Rainbow(screen, FigletText("And More!")),screen.height+24, Screen.COLOUR_GREEN),
          Print(screen,ColourImageFile(screen, "pai.gif", screen.height ,uni=True, dither=False),0,stop_frame=200)
    ]
    scenes.append(Scene(effects))

    effects = [
        Scroll(screen, 3),
        Mirage(
            screen,
            FigletText("Conceived and"),
            screen.height,
            Screen.COLOUR_GREEN),
        Mirage(
            screen,
            FigletText("written by:"),
            screen.height + 8,
            Screen.COLOUR_GREEN),
        Mirage(
            screen,
            Rainbow(screen,FigletText("ef1500")),
            screen.height + 16,
            Screen.COLOUR_GREEN)
    ]
    scenes.append(Scene(effects, (screen.height + 24) * 3))

    effects=[
        Scroll(screen, 4),
        Mirage(
            screen,
            Rainbow(screen, FigletText("The Semi-Automatic")),
            screen.height,
            Screen.COLOUR_GREEN),
        Mirage(
            screen,
            Rainbow(screen, FigletText("Lean")),
            screen.height+8,
            Screen.COLOUR_GREEN),
        Cycle(
            screen,
            FigletText("Mean"),
            screen.height+16),
        Mirage(
            screen,
            Rainbow(screen, FigletText("Scraping Machine")),
            screen.height+24,
            Screen.COLOUR_GREEN),
        RingFirework(screen, screen.width/2, screen.height/2, life_time=100),
        RingFirework(screen, (screen.width/2)-10, (screen.height/2)+6, life_time=100),
        RingFirework(screen, (screen.width/2)+10, (screen.height/2)+6, life_time=100)
    ]
    scenes.append(Scene(effects, (screen.height + 24) * 3))

    effects = [
        Cycle(
            screen,
            FigletText("JPT-x7", font='doh'),
            screen.height // 2 - 8,
            stop_frame=100),
        Cycle(
            screen,
            FigletText('By: ef1500'),
            screen.height // 2 + 3,
            stop_frame=100),
        Stars(screen, (screen.width + screen.height) // 2, stop_frame=100),
        DropScreen(screen, 100, start_frame=100)
    ]
    scenes.append(Scene(effects, 200))

    effects=[
        Matrix(screen, stop_frame=200),
         Mirage(
            screen,
            Rainbow(screen, FigletText("JPT-x7")),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("JPT-x7"),
            screen.height // 2 - 3,
            start_frame=200),
        Mirage(
            screen,
            Rainbow(screen, FigletText("JPT-x7")),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200)
    ]
    scenes.append(Scene(effects))

    effects = [
     Print(screen,
              SpeechBubble("Press 'X' to exit."), screen.height // 2 - 1, attr=Screen.A_BOLD)
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(_credits)
            sys.exit(0)
        except ResizeScreenError:
            pass