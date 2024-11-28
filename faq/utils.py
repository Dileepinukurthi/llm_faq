# from llm_faq.settings import GEMINI_API_KEY
import google.generativeai as genai
from llm_faq.settings import GEMINI_API_KEY



genai.configure(api_key=GEMINI_API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash',system_instruction="you are faq answering assistant developed by dileep chowdary inukurthi")


def llm_response(query):
    return model.generate_content(query).text

if __name__ == "__main__":
    print(llm_response("who are you?"))
