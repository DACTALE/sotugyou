import os

def output_file_structure(dir_path, output_file):
    """
    ディレクトリ内のファイル構成をテキストファイルに出力する
    
    Args:
        dir_path (str): 出力対象のディレクトリパス
        output_file (str): 出力先のテキストファイルパス
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(dir_path):
            # ディレクトリ階層に応じたインデントを付与
            indent = '  ' * root.count(os.sep)
            f.write(f"{indent}[{os.path.basename(root)}]\n")
            
            for file in files:
                f.write(f"{indent}  - {file}\n")

# 使用例
output_file_structure('.', 'file_structure.txt')
