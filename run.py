from autoFillMaskWithCandi import(setTokenModel, 
                      show_mask_fill, 
                      mask_fill_replaced)

input_sentences = [
    "maling hindi maligo",
    "maling hindi malego"
]

modelInput=("GKLMIP/electra-tagalog-base-uncased")

setTokenModel(modelInput)
print("__________________________")
show_mask_fill(input_sentences)
print("__________________________")
print(f"{mask_fill_replaced(input_sentences)}")
print("__________________________ as is")
string = mask_fill_replaced(input_sentences)
print(string)