#!/usr/bin/env python3

import argparse
import time
import utils.unifieddiff as udiff
import os
from markdown_processor import MarkdownProcessor
from ollama_engine import OllamaEngine
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".md"):
            # print(f"{event.src_path}")
            return None  # Needed to research why this was failing
        else:
            print(f"File {event.src_path} {event.event_type} at: {time.ctime()}")
            process_file(event.src_path,False)

def process_file(filename,dry_run):
    global ollama
    print('Processing file:',filename)
    with open(filename,'r') as f:
        text = f.read()
        
        engine = OllamaEngine(ollama)
        processor = MarkdownProcessor(engine, os.path.dirname(filename))    
        patch = processor.process(text)
        print('Patch:\n',patch)
        if not dry_run and patch:
            with open(filename,'w') as f:
                print('Writing to file:',filename)
                result = udiff.apply_patch(text,patch)
                f.write(result)


def watch_directory(src_dir,recursive):
    observer = Observer()
    observer.schedule(MyHandler(), path=src_dir, recursive=recursive)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def process_now(src,recursive,dry_run):
    md_files = []
    if os.path.isdir(src):
        if recursive:
            for root, dirs, files in os.walk(src):
                for file in files:
                    if file.endswith('.md'):
                        md_files.append(os.path.join(root, file))
        else:
            for item in os.listdir(src):
                # Check if the item is a file and its extension is .md
                if os.path.isfile(os.path.join(src, item)) and item.endswith('.md'):
                    # If it's an .md file, add it to the list of md_files
                    md_files.append(item)
    elif os.path.isfile(src) and src.endswith('.md'):
        md_files.append(src)
        
    for md_file in md_files:
        process_file(md_file,dry_run)

def main():
    global ollama
    
    parser = argparse.ArgumentParser(description='LLM Ghost writer')
    parser.add_argument('src', help='Source directory')
    parser.add_argument('-r','--recursive', action='store_true',help='Recursively search for markdown files in the specified source directory.')
    exclusive_group = parser.add_mutually_exclusive_group()
    exclusive_group.add_argument('--dry-run',action='store_true' ,help='Run without making changes')
    exclusive_group.add_argument('-w', '--watch', action='store_true', help='Watch the specified source directory for changes and re-process Markdown files as needed.') 
    parser.add_argument('--ollama', type=str, help='URL of Ollama server to use.')

    args = parser.parse_args()
    print(args)
    ollama=args.ollama

    if args.watch:
        watch_directory(args.src,args.recursive)
    else:
        process_now(args.src,args.recursive,args.dry_run)


    # Process the input and output here...

    return 0

if __name__ == "__main__":
    main()

