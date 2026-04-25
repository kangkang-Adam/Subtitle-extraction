import os
import json
def get_all_file_paths(directory):
    """
    获取目录下所有文件的完整路径
    
    Args:
        directory (str): 要遍历的目录路径
    
    Returns:
        list: 包含所有文件完整路径的列表
    """
    file_paths = []
    
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    
    return file_paths

if __name__ == '__main__':
    paths = get_all_file_paths("Subtitle_json")
 
    for path in paths:
        with open(path,'r',encoding="utf-8") as f:
            data = json.load(f)
        text = ''
        for i in data:
            text  += ''.join(i['text']) + '，'

        with open(path.replace('json','txt') ,'w', encoding="utf-8") as f:
            f.write(text)