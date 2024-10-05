import google.generativeai as genai
import os

def captcha_spin_ai():
    
    # def download_img(byte):
    #         with open("spin.png","wb") as f:
    #             f.write(byte)
    # download_img(byte)


    genai.configure(api_key="AIzaSyBiL7wsxewftNKKzZK_khOfUzRdvy7_coQ")

    myfile = genai.upload_file("/workspaces/codespaces-flask/spin.png")

    prompt = '''Are the images aligned or not. rethink your answer'''

    model = genai.GenerativeModel("gemini-1.5-flash")
    # model = genai.GenerativeModel("gemini-1.5-pro-exp-0827")
    # model = genai.GenerativeModel("gemini-1.5-pro",system_instruction=system_prompt)
    # model = genai.GenerativeModel("gemini-1.5-pro",system_instruction=system_prompt)

    result = model.generate_content(
        [myfile,prompt]
    )

    return str(result.text).lower().replace("\n",'')