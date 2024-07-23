from transformers import pipeline

# GPT-Neo
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# Cerință a clientului
client_request = """
Clientul solicită dezvoltarea unei aplicații de tip Glovo. Specifică următoarele secțiuni:
- Sistem de logistică a rider-ului.
- Înregistrarea restaurantelor în aplicație
- Primirea comenzilor de către clienți.
- Posibilitatea de a adăuga sau elimina produse din meniul restaurantului.
- Plata cu cardul.

Task-uri Adiționale Ne-meneționate de Client, dar Necesare:
- Secțiunea financiară: cum restaurantele solicită bani de la administratorii aplicației.
- Modalități de plată pentru rideri.
- Generarea automată a facturilor și posibilitatea clientului de a descărca factura generată.
"""

# Generarea ofertei
offer = generator(client_request, max_length=500, do_sample=True, temperature=0.7)
print(offer[0]['generated_text'])
