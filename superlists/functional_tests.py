from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title

# Ela é convidada a inserir um item de tarefa imediatamente

# Ela digita "Buy peacock feathers" (Comprar penas de pavão) em una caixa
# de texto (o hobby de Edith é fazer iscas para pesca com fly)

# Quando ela tecla enter, a página é atualizada, e agora a página list
# "1: Buy peacock feathers" como um item em uma lista de tarefas

# Ainda continua havendo uma caixa de texto convidando-a a acrescentar
# item. Ela insere "Use peacock feathers to make a fly" (Usar penas de
# para fazer um fly)

# A página é atualizada novamente e agora mostra os dois itens em sua lista

# Edith se pergunta se o site lembrará de sua lista. Então ela nota
# que o site gerou um URL único para ela -- há um pequeno
# texto explicativo para isso.

# Ela acessa esse URL e sua lista de tarefas continua lá.

# Satisfeita, ela volta a dormir
browser.quit()