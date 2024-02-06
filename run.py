from autoFillMaskWithCandy import(setTokenModel, 
                      show_mask_fill, 
                      mask_fill_replaced)

input_sentences = [
    "Pasensya heto lng ako, bobo sa pagaral",
    "Pasensya hito lng ako, bobo sa pagaral",
    "Pasensya heto lng ako, bubo sa pagaral",
    "Pasensya hito lng ako, bubo sa pagaral"
]

modelInput=("GKLMIP/bert-tagalog-base-uncased")

setTokenModel(modelInput)

show_mask_fill(input_sentences)

string = mask_fill_replaced(input_sentences)
print(string)
