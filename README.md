Para construir o ambiente use o comando "python -m virtualenv {nomedoambiente}" 
#(note que este comando é para a base linux, para windows use no lugar de virtualenv => venv)

# Para instalar as dependencias use o comando "pip install requirements.txt".
#### Sua aplicação está pronta para execução !!! #####




# Certifique-se de que está no diretório do file main.py
# Inicie o serviço com o input:
    "uvicorn main:app --reload"
# acesse http://127.0.0.1:8000/docs#/



##### METODOS ######
# Get => retorna lista de Todos os objetos
# Get_by_Buscador_&_comparador => (Utiliza um paramentro de busca {&comparador})
    # Parametros no DB
        # "breed"
        # "location_of_origin"
        # "coat_lenght" = 1;2;3;4;5;6;...
        # "body_type"   = "Pequeno , Medio , Grande"
        # "pattern"     = True or False


# Este é um software desenvolvido para processo seletivo
# &copy
