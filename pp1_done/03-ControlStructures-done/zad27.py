fb = input("Do you have Facebook? (True/False): ")
tw = input("Do you have Twitter? (True/False): ")
ig = input("Do you have Instagram? (True/False): ")

l_fb = fb.lower()
l_tw = tw.lower()
l_ig = ig.lower()

count = 0

for i in range(1):
    if(l_fb == "true"):
        count += 1
    else:
        count = count
    if(l_tw == "true"):
        count += 1
    else:
        count = count
    if(l_ig == "true"):
        count += 1
    else:
        count = count

if(count >= 2):
    print("Facebook =", fb)
    print("Twitter =", tw)
    print("Instagram =", ig)
    print("A person can be a good influencer")
else:
    print("Facebook =", fb)
    print("Twitter =", tw)
    print("Instagram =", ig)
    print("A person can't be a good influencer")