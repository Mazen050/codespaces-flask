import google.generativeai as genai
import os
import requests
from tiktok import format_text 

def captchaai_img(url):
    genai.configure(api_key="AIzaSyBiL7wsxewftNKKzZK_khOfUzRdvy7_coQ")

    def download_img(url):
            doc = requests.get(url)
            with open("img.jpg","wb") as f:
                f.write(doc.content)
    download_img(url)
    myfile = genai.upload_file("/workspaces/codespaces-flask/img.jpg")

    prompt = '''Return a bounding box for the duplicated objects(2). \n [ymin, xmin, ymax, xmax] REPLY FORMAT: [ymin, xmin, ymax, xmax] FOR EACH'''

    model = genai.GenerativeModel("gemini-1.5-flash")
    # model = genai.GenerativeModel("gemini-1.5-pro-exp-0827",system_instruction=system_prompt)
    # model = genai.GenerativeModel("gemini-1.5-pro",system_instruction=system_prompt)

    result = model.generate_content(
        [myfile,prompt]
    )
    return format_text(result.text)

