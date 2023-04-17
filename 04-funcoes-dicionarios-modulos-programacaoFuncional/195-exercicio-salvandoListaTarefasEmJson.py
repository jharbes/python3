# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar

# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']

# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def printarTarefas():
    print('TAREFAS:')
    if len(todoList)<1:
        print('Não há tarefas para serem listadas!')
    else:
        for task in todoList:
            print(task)
    print()

todoList=[]
refazerList=[]


while True:
    print('Comandos: listar, desfazer, refazer, fim')
    tarefa=input('Digite uma tarefa ou comando: ')
    print()
    if tarefa=='listar':
        printarTarefas()
    elif tarefa=='desfazer':
        if len(todoList)<1:
            print('Não há tarefa para desfazer!\n')
        else:
            refazerList.append(todoList.pop())
            printarTarefas()
    elif tarefa=='refazer':
        if len(refazerList)<1:
            print('Não há tarefa para refazer!\n')
        else:
            todoList.append(refazerList.pop())
            printarTarefas()
    elif tarefa=='fim':
        break
    else:
        todoList.append(tarefa)
        printarTarefas()