import pyocr
from PIL import ImageGrab

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#ocrをTesseractに指定する
tools = pyocr.get_available_tools()
tool = tools[0]

# 画像を取り込む
img = ImageGrab.grabclipboard()

# 画像から文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

print(text)