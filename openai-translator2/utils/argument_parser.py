import argparse
import os

class ArgumentParser:
    def __init__(self):
        # 构建相对于当前脚本的上级目录的路径  
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
        
        # 指定 config.yaml 文件的路径  
        config_path = os.path.join(base_dir, 'config.yaml')

        self.parser = argparse.ArgumentParser(description='A translation tool that supports translations in any language pair.')
        self.parser.add_argument('--config_file', type=str, default=config_path, help='Configuration file with model and API settings.')
        self.parser.add_argument('--model_name', type=str, help='Name of the Large Language Model.')
        self.parser.add_argument('--input_file', type=str, help='PDF file to translate.')
        self.parser.add_argument('--output_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
        self.parser.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
        self.parser.add_argument('--target_language', type=str, help='The target language for translating the original book.')

    def parse_arguments(self):
        args = self.parser.parse_args()
        return args
