from PIL import Image
from typing import Optional


def add_margin(original_image: Image) -> Image:
    width, height = original_image.size
    if width == height:
        return original_image
    new_width_and_height = width if width > height else height
    new_image = Image.new(original_image.mode, (new_width_and_height, new_width_and_height), (0, 0, 255))
    if width > height:
        new_image.paste(original_image, (0, (width - height) // 2))
    else:
        new_image.paste(original_image, ((height - width) // 2, 0))
    return new_image

def will_overwrite(original_image: Image) -> bool:
    width, height = original_image.size
    return width != height


def write_file(original_path: str, write_path: Optional[str] = None) -> None:
        """
        余白を加えた画像を指定したパスへ書き出す
        :param original_path: ファイルの存在するオリジナルのパス
        :param write_path: 書き出し先　Noneであればオリジナルへ上書き
        :return:
        """
        result_path = original_path if write_path is None else write_path
        print("load", original_path)
        original_image = Image.open(original_path)
        if will_overwrite(original_image) is False:
            return
        added_image = add_margin(original_image)
        print("write", result_path)
        added_image.save(result_path, quality=95)
