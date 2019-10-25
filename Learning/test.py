st = 'Print only the words that start with s in this sentence'

for item in st.split():
    # print(item[0].upper())
    if item[0].upper()=="S":
        print(item)

#------------
print("---------------------")
st = 'Print every word in this sentence that has an even number of letters'
w_len = len("even")
for word in st.split():
    if len(word)==w_len:
        print(word)


lst =[x[0] for x in st.split()]
print(lst)