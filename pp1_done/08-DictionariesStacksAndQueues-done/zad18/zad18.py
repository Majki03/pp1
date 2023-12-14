ICAO = {
  "A":"Alfa",
  "B":"Bravo",
  "C":"Charlie",
  "D":"Delta",
  "E":"Echo",
  "F":"Foctrot",
  "G":"Golf",
  "H":"Hotel",
  "I":"India",
  "J":"Juliett",
  "K":"Kilo",
  "L":"Lima",
  "M":"Mike",
  "N":"November",
  "O":"Oscar",
  "P":"Papa",
  "Q":"Quebec",
  "R":"Romeo",
  "S":"Sierra",
  "T":"Tango",
  "W":"Whiskey",
  "X":"Xray",
  "Y":"Yankee",
  "Z":"Zulu"
}

with open("ICAO.txt", "w") as copy:
  for key, value in ICAO.items():
    copy.write(key)
    copy.write(" ")
    copy.write(value + "\n")