import hashlib
import json
import logging
import ollama

logger = logging.getLogger(__name__)

class OllamaEngine:
    def __init__(self,server=None):
        self.current_seed = None
        self.current_model = None
        self.current_system = None
        self.current_conversation = "Default"
        self.model_stack = []
        self.system_stack = []
        self.conversation_stack = [self.current_conversation]
        self.conversation_history = {self.current_conversation: []}
        self.images = {self.current_conversation: []}
        print(f"Ollama: {server}")
        # client = ollama.Client('http://192.168.1.52:11434')
        self.client = ollama.Client(server)

    def seed(self, seed):
        self.current_seed = int(seed)  # convert seed to int
        return ""


    def system(self, system_name):
        system = self.client.systems.get(system_name)
        self.current_system = system
        return ""    
    
    def model(self, model):
        available_models = [m['name'] for m in self.client.list()['models']]

        if model in available_models:
            self.model_stack.append(self.current_model)
            self.current_model = model
            return ""
        else:
            logger.warning(f"Model not found. Model list: {available_models}")

            return "<!-- ERROR: Model not found -->\n"

    def close_model(self):
        #check if stack is empty
        if len(self.model_stack) > 0:
            self.current_model=self.model_stack.pop()
            return ""
        else:
            return "<!-- ERROR: No models in stack -->\n"

    def system(self, system):
        self.system_stack.append(self.current_system)
        self.current_system = system
        return ""
    
    def close_system(self):
        if len(self.system_stack) > 0:
            self.current_system = self.system_stack.pop()
            return ""
        else:
            return "<!-- ERROR: No systems in stack -->\n"

    def conversation(self, conversation):
        self.conversation_stack.append(self.current_conversation)
        self.current_conversation = conversation
        self.conversation_history[self.current_conversation] = []
        self.images[self.current_conversation] = []
        return ""
    
    def close_conversation(self):
        if len(self.conversation_stack) > 0:
            self.current_system = self.conversation_stack.pop()
            return ""
        else:
            return "<!-- ERROR: No conversations in stack -->\n"

    def compute_hash(self,text):
        messages = self.__getMessages()
        messages.append({'role': 'user', 'content': text, 'images': self.images[self.current_conversation]})
        # Convert messages to JSON string
        json_messages = json.dumps(messages, indent=4)
        return hashlib.sha256(json_messages.encode()).hexdigest()[-8:]

    def update_chat(self,text,response=None):
        self.conversation_history[self.current_conversation].append(("user",text,self.images[self.current_conversation]))
        self.images[self.current_conversation] = []
        if response:
            self.conversation_history[self.current_conversation].append(("assistant",response,[]))
        
    def update_image(self,image_src):
        self.images[self.current_conversation].append(image_src)

    def chat(self, text):
        self.conversation_history[self.current_conversation].append(("user",text,self.images[self.current_conversation]))
        self.images[self.current_conversation] = []
        messages=self.__getMessages()

        response = self.client.chat(model=self.current_model,messages=messages, options={'seed': self.current_seed})
        self.conversation_history[self.current_conversation].append(("assistant",response['message']['content']+'\n',[]))
        return response['message']['content']+'\n'
    
    def close_chat(self):
        return "<!-- ERROR: Closing chat that is not opened properly -->\n"
    
    def __getMessages(self):
        messages=[]
        if self.current_system:
            messages.append({'role': 'system', 'content': self.current_system})        
        for role,content,images in self.conversation_history[self.current_conversation]:
            messages.append({'role': role, 'content': content, 'images': images})
        return messages