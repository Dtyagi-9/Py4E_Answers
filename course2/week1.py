text = "X-DSPAM-Confidence:    0.8475";
pos=text.find(' ')
ans=text[pos+1:]
ans=float(ans)
print(ans)