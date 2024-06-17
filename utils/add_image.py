from PIL import Image, ImageTk
import os


def add_image_obj(image_name, width, height):
    
    # カレントディレクトリのパスを取得(実行中のPythonスクリプトファイルの絶対パスを取得します。)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 画像ファイルへの絶対パス
    image_path = os.path.join(current_dir, '..', 'resources', 'images', image_name)
    
    # 画像ファイルを読み込む
    image = Image.open(image_path)

    # 画像のサイズを変更
    new_width, new_height = width, height # 新しいサイズ
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Tkinter用の画像オブジェクトを作成
    photo = ImageTk.PhotoImage(image)
    
    return photo


