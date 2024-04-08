from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer,  AutoModelForSeq2SeqLM


class MoonDream:
    model_id = "vikhyatk/moondream2"
    model = None
    tokenizer = None

    def __new__(cls):
        if cls.model is None:
            cls.model = AutoModelForCausalLM.from_pretrained(cls.model_id, trust_remote_code=True)
            cls.tokenizer = AutoTokenizer.from_pretrained(cls.model_id)
        return cls

    @classmethod
    def generate(cls, image_path: str):
        image = Image.open(image_path)
        enc_image = cls.model.encode_image(image)
        return cls.model.answer_question(enc_image, "Describe this image.", cls.tokenizer)


class Bart:
    model_id = "Mr-Vicky-01/Bart-Finetuned-conversational-summarization"
    model = None
    tokenizer = None

    def __new__(cls):
        if cls.model is None or cls.tokenizer is None:
            cls.model = AutoModelForSeq2SeqLM.from_pretrained(cls.model_id)
            cls.tokenizer = AutoTokenizer.from_pretrained(cls.model_id)
        return cls

    @classmethod
    def generate_summary(cls, text):
        inputs = cls.tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
        summary_ids = cls.model.generate(inputs['input_ids'], max_new_tokens=100, do_sample=False)
        summary = cls.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary


MoonDream()
Bart()
