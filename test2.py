text="orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
mijloc=len(text)//2
partea1=text[:mijloc]
partea2=text[mijloc:]
partea1=partea1.upper()
partea1=partea1.strip()
partea2=partea2[::-1]
partea2=partea2.title()
partea2=partea2.strip(".,?!")
rezultat= partea1 + partea2
print(rezultat)

