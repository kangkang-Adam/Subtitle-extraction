from to_json import get_all_file_paths, srt_to_json
import json
def main():


    print("Hello from subtitle-extraction!")

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
    
    paths = get_all_file_paths("Subtitle_json")
 
    for path in paths:
        with open(path,'r',encoding="utf-8") as f:
            data = json.load(f)
        text = ''
        for i in data:
            text  += ''.join(i['text']) + '，'

        with open(path.replace('json','txt') ,'w', encoding="utf-8") as f:
            f.write(text)