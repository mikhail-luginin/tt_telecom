# TT_Telecom (backend)

Данный репозиторий содержит в себе техническое задание для компании "К Телеком".

***

Инструкция по установке
    
    (python version 3.11)

    pip install virtualenv
    git clone https://github.com/mikhail-luginin/tt_telecom
    cd tt_telecom
    python -m virtualenv venv
    source venv/bin/activate

    pip install -r requirements.txt
    
    cp .env.template .env

# ToDo

***

Для дальнейшего использования приложения необходимо будет сделать оптимизацию запросов при помощи JOIN'ов. И в случае их использования прописать в отдельном файле функции возвращающие QuerySet'ы, чтобы пользоваться ими без постоянного повторения методов select_related или же prefetch_related.
