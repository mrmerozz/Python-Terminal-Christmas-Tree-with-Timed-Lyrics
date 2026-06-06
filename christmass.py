import time
import random
import sys

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
pink = '\033[35m'
cyan = '\033[36m'
white = '\033[97m'
brown = '\033[33m'
reset = '\033[0m'

lights = [red, yellow, blue, pink, cyan]
star = '★'
delay = 0.05
speed = 15

tree = [
    "         * ",
    "         * ",
    "        *** ",
    "       ***** ",
    "      ******* ",
    "     ********* ",
    "    *********** ",
    "   ************* ",
    "  *************** ",
    " ***************** ",
    "*******************",
    "        |||         ",
    "        |||         ",
    "        |||         ",
]

lyrics = [
    (0.0, "Last Christmas, I gave you my heart,"),
    (3.5, "But the very next day, you gave it away."),
    (7.0, "This year, to save me from tears,"),
    (10.5, "I'll give it to someone special."),
    (14.0, "Once bitten and twice shy,"),
    (17.5, "I keep my distance, but you still catch my eye."),
    (21.0, "Tell me, baby, do you recognize me?"),
    (24.5, "Well, it's been a year, it doesn't surprise me."),
    (28.0, "(Happy Christmas) I wrapped it up and sent it"),
    (31.5, "With a note saying 'I love you,' I meant it"),
    (35.0, "Now I know what a fool I've been"),
    (38.5, "But if you kissed me now, I know you'd fool me again."),
    (42.0, "Last Christmas..."),
]

song_len = lyrics[-1][0]


def get_lyric(elapsed):
    loop_time = elapsed % song_len
    current_text = ""
    lyric_start = 0.0

    for i in range(len(lyrics)):
        start = lyrics[i][0]
        text = lyrics[i][1]
        end = lyrics[i + 1][0] if i + 1 < len(lyrics) else song_len

        if start <= loop_time < end:
            current_text = text
            lyric_start = start
            break

    loops_done = int(elapsed / song_len)
    abs_start = loops_done * song_len + lyric_start
    return current_text, abs_start


def color_line(line):
    result = ""
    c1 = random.choice(lights)
    c2 = random.choice(lights)
    for ch in line:
        if ch == '*':
            r = random.random()
            if r < 0.25:
                result += c1 + '*' + reset
            elif r < 0.50:
                result += c2 + '*' + reset
            elif r < 0.70:
                result += random.choice(lights) + '*' + reset
            else:
                result += green + '*' + reset
        else:
            result += ch
    return result


def draw(elapsed):
    sys.stdout.write('\033[H\033[J')

    text, start = get_lyric(elapsed)
    chars_visible = int((elapsed - start) * speed)
    typed = text[:chars_visible]
    lyric_display = white + typed + reset

    for i, row in enumerate(tree):
        col = ""

        if i == 0:
            col = ' ' * 9 + random.choice(lights) + star + reset + ' ' * 9
        elif '|||' in row:
            col = row.replace('|', brown + '|' + reset)
        else:
            col = color_line(row)

        side = lyric_display if i == 5 else ""
        print(f"{col.ljust(50)} {side}")

    sys.stdout.flush()


def main():
    print("--- Ctrl+C to stop ---")
    time.sleep(1)
    start = time.time()
    try:
        while True:
            draw(time.time() - start)
            time.sleep(delay)
    except KeyboardInterrupt:
        sys.stdout.write('\033[H\033[J')
        print("Merry Christmas!")
        print(reset)

main()
