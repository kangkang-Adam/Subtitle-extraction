import json
import re
import os
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

def srt_to_json(srt_content):
    blocks = re.split(r'\n\s*\n', srt_content.strip())
    result = []
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            index = int(lines[0])
            time_line = lines[1]
            start_end = re.match(r'(\S+)\s*-->\s*(\S+)', time_line)
            if start_end:
                start, end = start_end.groups()
                text = ' '.join(lines[2:])
                result.append({
                    "index": index,
                    "start": start,
                    "end": end,
                    "text": text
                })
    return result



if __name__ == '__main__':
    paths = get_all_file_paths("Subtitle")
 
    for path in paths:
        if 'Zone.Identifier' in path:
            continue
        with open(path, 'r', encoding='utf-8') as f:
            srt_data = f.read()
            json_output = srt_to_json(srt_data)
        
        with open( path.replace('srt','json').replace('Subtitle', 'Subtitle_json'),'w',encoding='utf-8') as f:
            temps = json.dump(json_output,fp = f,indent=4, ensure_ascii=False)


    