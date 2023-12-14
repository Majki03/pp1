ICAO = {
  "a":"Alfa",
  "b":"Bravo",
  "c":"Charlie",
  "d":"Delta",
  "e":"Echo",
  "f":"Foctrot",
  "g":"Golf",
  "h":"Hotel",
  "i":"India",
  "j":"Juliett",
  "k":"Kilo",
  "l":"Lima",
  "m":"Mike",
  "n":"November",
  "o":"Oscar",
  "p":"Papa",
  "q":"Quebec",
  "r":"Romeo",
  "s":"Sierra",
  "t":"Tango",
  "w":"Whiskey",
  "x":"Xray",
  "y":"Yankee",
  "z":"Zulu"
}

def spelled(text):
  spelled_text = " ".join(ICAO.get(char.lower(), char) for char in text)
  return spelled_text

inpu = input("Enter text: ")

spelled_text = spelled(inpu)

print(f"Spelled text: {spelled_text}")