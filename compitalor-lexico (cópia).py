
fluxo_tokens = ""
posicao = 1
fluxo_caracteres = input("Digite uma expressao: ")

for t in fluxo_caracteres:
    if t.isalpha():
        fluxo_tokens += "<id,{}>".format(posicao)
        posicao += 1
        print("<id,1>", end="")
    elif t == "#":
        pass
    elif t.isdigit():
        print("<{}>" .format(t), end="")
    elif t == "=" or t == "+" or t == "*":
        print("<{}>" .format(t), end="")
    elif t.isspace():
        pass
    else:
        print("<Error>", end="")