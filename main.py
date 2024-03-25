from database import Database
from bookModel import booksModel

db = Database(database="relatorio5", collection="books")
bookModel = booksModel(database=db)

def create_book():
    print("Um livro será criado!")
    titulo = input("Qual o título do livro? ")
    autor = input("Quem é o autor do livro? ")
    ano = int(input("Qual o ano de publicação do livro? "))
    preco = float(input("Qual o preço do livro? "))
    bookModel.create_book(titulo, autor, ano, preco)
    print("Livro criado!")

def read_book_by_id():
    book_id = input("Entre com o ID do livro que deseja buscar ")
    book = bookModel.read_book_by_id(book_id)
    if book:
        print({book})
    else:
        print("Hmm, não existe um livro com esse ID.")

def update_book():
    print("Um livro será atualizado!")
    book_id = input("Qual o ID do livro que você deseja atualizar? ")
    titulo = input("Qual o novo título do livro? ")
    autor = input("Quem é o novo autor do livro? ")
    ano = int(input("Qual o novo ano de publicação do livro? "))
    preco = float(input("Qual o novo preço do livro? "))

    updated_data = {}
    updated_data["titulo"] = titulo
    updated_data["autor"] = autor
    updated_data["ano"] = int(ano)
    updated_data["preco"] = float(preco)

    bookModel.update_book(book_id, **updated_data)
    print("Atualização feita com sucesso!")

def delete_book():
    book_id = input("Qual o ID do livro que você deseja deletar? ")        
    bookModel.delete_book(book_id)

def main_menu():
    while True:
        print("\nEntre com uma opção:")
        print("1. Criar livro")
        print("2. Buscar livro pelo ID")
        print("3. Atualizar livro")
        print("4. Apagar livro")
        print("5. Sair")

        op = input("\n Digite o número referente a opção escolhida: ")

        if op == '1':
            create_book()
        elif op == '2':
            read_book_by_id()
        elif op == '3':
            update_book()
        elif op == '4':
            delete_book()
        elif op == '5':
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main_menu()