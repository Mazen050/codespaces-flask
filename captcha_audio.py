import google.generativeai as genai
import os
import requests

def captcha_audio_ai(url):
    genai.configure(api_key="AIzaSyBiL7wsxewftNKKzZK_khOfUzRdvy7_coQ")

    def download_audio(url):
        doc = requests.get(url)
        with open("audio.mp3","wb") as f:
            f.write(doc.content)
    download_audio(url)
    myfile = genai.upload_file("/workspaces/codespaces-flask/audio.mp3")

    prompt = '''Return only the letters you hear'''

    # model = genai.GenerativeModel("gemini-1.5-flash")
    model = genai.GenerativeModel("gemini-1.5-pro-exp-0827") 
    # model = genai.GenerativeModel("gemini-1.5-pro")
    # model = genai.GenerativeModel("gemini-1.5-pro-exp-0827",system_instruction=system_prompt)
    # model = genai.GenerativeModel("gemini-1.5-pro",system_instruction=system_prompt)

    result = model.generate_content(
        [myfile,prompt]
    )
    return str(result.text).lower()

# print(captcha_audio_ai("https://sf-rc-verification.tiktokcdn-us.com/obj/captcha-dl-tx/voice_2385_b69d93ef9a2af8d128e34f8d7009e82023991fdd.mp3"))
