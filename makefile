FILES :=                      \
    .gitignore                \
    .travis.yml               \
    app.py                    \
    app.yaml                  \
    books.json                \
    create_db.py              \
    models.py                 \
    requirements.txt          \
    makefile                  \
    test.py                   \

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

models.html:
	$(PYDOC) -w models

IDB3.log:
	git log > IDB3.log

IDB2.log:
	git log > IDB2.log

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

test:
	coverage run test.py
