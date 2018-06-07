import TextToPictures as TTP

if __name__ == "__main__":

    ttp = TTP.TextToPictures((750, 1334))
    ttp.load_text('demo.txt')
    print(ttp.text)
    pages_text = ttp.format_text((40, 40, 40, 40), font='msyh.ttc', font_size=35, spacing=12)
    for k, v in pages_text.items():
        print(k)
        print(v)

    ttp.render()
    ttp.save('demo')
