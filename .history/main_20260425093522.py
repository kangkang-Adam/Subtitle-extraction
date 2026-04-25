from to_json import get_all_file_paths, srt_to_json
import json
import os

def main():
    print("Hello from subtitle-extraction!")

    # 第一步：将 .srt 转换为 .json
    srt_paths = get_all_file_paths("Subtitle")
    for path in srt_paths:
        if 'Zone.Identifier' in path:
            continue
        
        # 生成目标 json 文件路径
        json_path = path.replace('.srt', '.json').replace('Subtitle', 'Subtitle_json')
        
        # 防重复：如果 json 文件已存在，则跳过
        if os.path.exists(json_path):
            #print(f"跳过已存在的文件：{json_path}")
            continue
        
        with open(path, 'r', encoding='utf-8') as f:
            srt_data = f.read()
            json_output = srt_to_json(srt_data)
        
        # 确保输出目录存在（如果目录不存在则创建）
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=4, ensure_ascii=False)
        print(f"已生成：{json_path}")
    
    # 第二步：将 .json 转换为 .txt（合并文本）
    json_paths = get_all_file_paths("Subtitle_json")
    for path in json_paths:
        # 生成目标 txt 文件路径
        txt_path = path.replace('.json', '.txt')
        
        # 防重复：如果 txt 文件已存在，则跳过
        if os.path.exists(txt_path):
            #print(f"跳过已存在的文件：{txt_path}")
            continue
        
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
        text = ''
        for i in data:
            text += ''.join(i['text']) + '，'
        
        with open(txt_path, 'w', encoding="utf-8") as f:
            f.write(text)
        print(f"已生成：{txt_path}")

if __name__ == '__main__':
    main()