# DMS

    .
    ├── cmd
    ├── internal       
    │   ├── app        
    │   │   ├── api
    │   │   ├── warehouse
    │   │   └── worker
    │   └── converter
    ├── pkg
    │   ├── ftools
    │   │   ├── fconf
    │   │   ├── fdb
    │   │   ├── flog
    │   │   └── fmigrate
    │   ├── http_checker
    │   │   ├── health
    │   │   └── live
    │   ├── magento-worker
    │   └── model
    │       ├── additional
    │       ├── assignment
    │       ├── atc
    │       ├── brand
    │       ├── catalog
    │       ├── city
    │       ├── company
    │       ├── contraindication
    │       ├── country
    │       ├── direction
    │       ├── dms
    │       ├── drug
    │       ├── drug_additional
    │       ├── history
    │       ├── job
    │       ├── magento
    │       ├── media
    │       ├── release_form
    │       ├── schema
    │       ├── statistic
    │       ├── swagger
    │       ├── warehouse
    │       ├── warehouse_drug
    │       ├── warehouse_group
    │       ├── warehouse_group_drug
    │       └── Default.go
    ├── temp
    ├── amount.go
    ├── Base_ID.xlsx
    ├── country.go
    ├── image.go
    ├── inkar.go
    ├── main.go
    ├── Makefile
    ├── go.mod
    └── Список 9 тыщ


1. Fiber
    * [fiber git](github.com/gofiber/fiber/v2)
    * [fiber cors](github.com/gofiber/fiber/v2/middleware/cors)
    * [fiber pprof](github.com/gofiber/fiber/v2/middleware/pprof)
2. Fast http
    * [fast http git](github.com/valyala/fasthttp)
3. fast json parser
    * [lib](github.com/valyala/fastjson)
4. gorm
    * [lib](gorm.io/gorm)


1. Makefile
    * [habr makefile](https://habr.com/ru/post/461467/)
2. Swagger
4. Postgres
5. AMQP Rabbit
    * [amqp](github.com/streadway/amqp)
6. Work with Excell
    * [doca](https://xuri.me/excelize/ru/base/installation.html#install) 
    * [excelize](https://github.com/360EntSecGroup-Skylar/excelize) 
    * Read data From Excell adn Update DB Table 
7. Work with Hash Go
8. Strings go pkg
    * [strings lib](https://golang.org/pkg/strings/)
9. Golang Applications Directory Structure
10. strconv
    * [Converter](https://replit.com/@Avutzhan/DMSConverter#main.go)
    * [convert tutorial](https://golangify.com/string-in-number#:~:text=ParseInt()%20%D0%B8%20ParseFloat()%20%D0%B4%D0%BB%D1%8F%20%D0%BA%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%B0%D1%86%D0%B8%D0%B8%20%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8%20%D0%B2%20%D1%87%D0%B8%D1%81%D0%BB%D0%BE&text=%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F%20ParseFloat%20%D0%BA%D0%BE%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%B8%D1%80%D1%83%D0%B5%D1%82%20%D1%81%D1%82%D1%80%D0%BE%D0%BA%D1%83%20%D0%B2%20%D1%87%D0%B8%D1%81%D0%BB%D0%BE%20%D0%B2%D0%B5%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%82%D0%B8%D0%BF%D0%B0%20float.) 
    * [strconv](https://golang.org/pkg/strconv/)
12. UUID 
    * [uuid git](https://github.com/satori/go.uuid) 
13. sync go pkg
    * [lib](https://golang.org/pkg/sync/)
14. img to base64
    * [lib](https://github.com/polds/imgbase64)
    
### Старая версия
1. CMD точки входа
2. Models
3. CRUD
4. Parsers
5. Excell parser

### Новая версия
1. CMD точка входа
2. Internal приложухи отдельные со своим роутингом моделями
    * api - cruds по лекарствам создают очереди
        * connect to db
        * run migrations
        * run cors
        * use pprof and history
        * use swagger
        * mount routes
    * warehouse - круд инфо по складам создает очереди
        * connect to db
        * run cors
        * use pprof and history
        * mount routes
    * worker - интеграция с магенто лекарства склады остатки слушает очереди и обрабатывает их 
        * connect to db
        * run cors
        * use pprof and history
        * mount routes
    
3. PKG
    * ftools
        * fconf конфиги 
        * fdb соединение с базой
        * flog логирование
        * fmigrate миграции
    * magento-worker хелперы для internal/worker
    * model все модели

4. amount.go узнать количество лекарств
5. country вывести какие то данные о country
6. image.go что то связанное с картинками
7. inkar.go чтение excell файлов и обновление лекарств
8. main.go публикуем в реббит какие то данные по лекарствам
