import data
data=data.get_data()

def ksw_to_eng(word:str):
    """Translate a Swahili word into to English word, Print and return the meaning"""
    meaning=""
    for dic in data:
        if word==dic["ksw"].replace(" ",""):
            meaning+=f"📚 {word} - {dic["eng"]}\n"
            for key,value in dic.items():
                if key =="id":
                    continue
                if key =="ksw" or key =="eng":
                    continue
                if key=="type":
                    meaning+=f"🤖 {key}: {value}\n"
                if key=="example":
                    meaning+="\nExample: ⚡\n"
                    for key,value in value.items():
                        meaning+=f"🟩 {key}: {value}\n"
            return meaning

def eng_to_ksw(word:str):
    """Translate a English word into to Swahili word, print and return the meaning"""
    meaning=""
    for dic in data:
        if word==dic["eng"].replace(" ",""):
            meaning+=f"📚 {word} - {dic["ksw"]}\n"
            for key,value in dic.items():
                if key =="id":
                    continue
                if key =="ksw" or key =="eng":
                    continue
                if key=="type":
                    meaning+=f"🤖 {key}: {value}\n"
                if key=="example":
                    meaning+="\nExample: ⚡\n"
                    for key,value in value.items():
                        meaning+=f"🟩 {key}: {value}\n"
            return meaning

# print(eng_to_ksw("able"))
# print(ksw_to_eng("uwezo"))