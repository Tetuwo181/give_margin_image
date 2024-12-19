import os
from typing import Callable
from mergin_giver import margin_giver as mg
import shutil


def is_image(file_path:str) -> bool:
    """
    拡張子から画像ファイルかどうか判定
    :param file_path:
    :return:
    """
    root, ext = os.path.splitext(file_path)
    return (ext == ".jpg") or (ext == ".jpeg") or (ext == ".JPG") or (ext == ".JPEG") or (ext == ".jfif")


def margin_giver_writer_builder(original_dir: str) -> Callable[[str], None]:
    """
    画像をリサイズし、書き出す関数を呼び出す
    :param original_dir: オリジナルのディレクトリ
    :return:
    """
    def write_resize_image(resize_dir: str) -> None:
        if original_dir != resize_dir:
            shutil.copytree(original_dir, resize_dir)
        return give_margin_images_dir(resize_dir)

    return write_resize_image


def give_margin_images_dir(original_dir: str) -> None:
    """
    指定したディレクトリ以下の画像をリサイズする
    :param original_dir: リサイズしたい画像が存在するディレクトリ
    :return:
    """
    file_name_set = os.listdir(original_dir)
    for name in file_name_set:
        file_path = os.path.join(original_dir, name)
        if os.path.isdir(file_path):
            print(file_path, "is dir")
            give_margin_images_dir(file_path)
        if is_image(file_path):
            print("add_margin", file_path)
            mg.write_file(file_path)
