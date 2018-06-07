from PIL import ImageFont, Image, ImageDraw


class TextToPictures:
    def __init__(self, size):
        """
        size: width and height of pictures.
        """
        self.picture_size = size
        self.text = ''
        self.images = dict()
        self.draws = dict()
        self.pages_text = dict()
        self.spacing = 4
        self.position = (0, 0)

    def load_text(self, file_name: str):
        with open(file_name, 'r') as f:
            self.text = f.read()
        return self.text

    def format_text(self, padding: tuple, font: str = 'msyh.ttc', font_size: int = 35, spacing: int = 10):
        """
        padding: padding of top, bottom, left and right
        """
        self.spacing = spacing
        top, bottom, left, right = padding
        self.position = (left, top)
        picture_width, picture_height = self.picture_size
        height = picture_height - top - bottom
        width = picture_width - left - right

        self.font = ImageFont.truetype(font, font_size)
        font_width, font_height = self.font.getsize('永')
        chars_per_line = int(width / font_width)
        lines_per_page = int(height / (self.font.font.ascent + spacing))
        text_len = len(self.text)
        chars_index = 0
        lines_index = 0
        pages_index = 0
        page_text = ''
        while chars_index < text_len:
            chars_end = chars_index + chars_per_line
            if chars_end >= text_len:
                chars_end = text_len
            line_text = self.text[chars_index:chars_end]
            # 处理换行问题。
            enter_index = line_text.find('\n')
            if enter_index != -1:
                chars_end = chars_index + enter_index
                line_text = self.text[chars_index:chars_end]
                chars_end += 1
            # 处理下一行行首标点问题。
            punctuation = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
            ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
            々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
            ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…''')
            if chars_end < text_len and self.text[chars_end] in punctuation:
                chars_end -= 1
                line_text = self.text[chars_index:chars_end]
            chars_index = chars_end
            if line_text != '':
                page_text += u'{}\n'.format(line_text)
                lines_index += 1
            if lines_index == lines_per_page:
                self.pages_text[pages_index] = page_text[:-1] # 去掉最后的换行符
                lines_index = 0
                page_text = ''
                pages_index += 1
        if page_text[:-1] != '':
            self.pages_text[pages_index] = page_text[:-1] # 去掉最后的换行符
        return self.pages_text

    def render(self):
        for index, text in self.pages_text.items():
            self.images[index] = Image.new('RGB', self.picture_size, (255, 255, 255))
            draw = ImageDraw.Draw(self.images[index])
            draw.text(self.position, text, font=self.font, fill=(0, 0, 0), spacing=self.spacing)

    def save(self, file_name: str):
        for index, image in self.images.items():
            fn = '{}-{}.jpg'.format(file_name, index)
            image.save(fn, 'jpeg')
