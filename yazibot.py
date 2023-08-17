import openai
import time

openai.api_key = "OPENAI-API-KEYINIZ"

print("Quartzz Yazı Bot\n Sürüm v1.0\n Created by quartzz.dll\n")
time.sleep(2)
prompt = input("Hangi Konu Hakkında Yazı Yazdırmak İstersiniz ? ")
user_prompt = (prompt,"Hakkında Bir Metin Yazmanı İstiyorum.")

def generate_creative_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=256  # Üretilen metnin uzunluğu
    )
    return response.choices[0].text.strip()

creative_text = generate_creative_text(user_prompt)

with open("istekMetin.txt", "w") as file:
    file.write(creative_text)
    print("Metin istekMetin.txt dosyasına yazıldı.")



