from transformers import GPT2Tokenizer, GPT2LMHeadModel
from peft import PeftModel, PeftConfig
import torch
import os

class TextGenerator:
    def __init__(self, model_path="gpt2-finetuned"):
        try:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            
            # Verify model files exist
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model directory '{model_path}' not found")
                
            required_files = [
                'tokenizer_config.json',
                'vocab.json',
                'special_tokens_map.json',
                'adapter_config.json',
                'adapter_model.safetensors'
            ]
            
            for file in required_files:
                if not os.path.exists(os.path.join(model_path, file)):
                    raise FileNotFoundError(f"Required file {file} not found in {model_path}")
            
            # Load tokenizer and model
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
            # Load base model
            base_model = GPT2LMHeadModel.from_pretrained("gpt2").to(self.device)
            
            # Load fine-tuned adapter
            self.model = PeftModel.from_pretrained(base_model, model_path)
            self.model.eval()
            
            print("Model and tokenizer loaded successfully!")
            
        except Exception as e:
            print(f"Error loading model: {str(e)}")
            raise
    
    def generate_text(self, prompt, max_length=100, temperature=0.7, top_k=50, top_p=0.9):
        try:
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_length=max_length,
                    temperature=temperature,
                    top_k=top_k,
                    top_p=top_p,
                    repetition_penalty=1.2,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id
                )
            
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Error during text generation: {str(e)}")
            return f"Error generating text: {str(e)}"